# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from traveltimepy import Location, Coordinates, Transportation, TravelTimeSdk
from typing import Dict, List
import requests

app = FastAPI()
sdk = TravelTimeSdk("8097a90e", "90bf31f1a51cfd508e0d50b0f6ef69a7")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Localização fixa que servirá como referência (Cristo Redentor)
reference_location = Location(
    id="reference_point", coords=Coordinates(lat=-22.9519, lng=-43.2106))


class LocationData(BaseModel):
    id: str
    coords: Coordinates


class DepartureSearchData(BaseModel):
    id: str
    departure_location_id: str
    arrival_location_ids: List[str]
    departure_time: str
    travel_time: int


@app.get("/geocoding")
async def geocoding_search(query: str, limit: int = 30):
    try:
        results = await sdk.geocoding_async(query=query, limit=limit)
        return results.features
    except Exception as e:
        return {"error": f"Erro na pesquisa de geocodificação: {str(e)}"}


@app.get("/linhas-onibus")
def listar_linhas_onibus():
    response = requests.get(
        "https://dados.mobilidade.rio/gps/sppo?dataInicial=2024-01-29+15:40:00&dataFinal=2024-01-29+15:43:00")
    if response.status_code == 200:
        linhas = set()
        data = response.json()
        for item in data:
            linhas.add(item["linha"])
        return {"linhas": list(linhas)}  # Alterado para retornar um dicionário
    else:
        return {"error": "Erro ao obter as linhas de ônibus"}


@app.get("/bus-position/{line}")
def get_bus_position(line: str):
    response_bus = requests.get(
        f"https://dados.mobilidade.rio/gps/sppo?dataInicial=2024-01-29+15:40:00&dataFinal=2024-01-29+15:43:00")
    if response_bus.status_code == 200:
        bus_data = response_bus.json()
        return bus_data
    else:
        return {"error": "Erro ao obter a posição dos ônibus da linha selecionada"}


@app.get("/bus-data/{line}")
def get_bus_data(line: str):
    response_bus = requests.get(
        f"https://dados.mobilidade.rio/gps/sppo?dataInicial=2024-01-29+15:40:00&dataFinal=2024-01-29+15:43:00")
    bus_data = response_bus.json()

    selected_buses = []
    for bus in bus_data:
        if bus["linha"] == line:
            selected_buses.append({
                "ordem": bus["ordem"],
                "latitude": bus["latitude"],
                "longitude": bus["longitude"],
                "datahora": bus["datahora"],
                "velocidade": bus["velocidade"],
                "linha": bus["linha"],
                "datahoraenvio": bus["datahoraenvio"],
                "datahoraservidor": bus["datahoraservidor"]
            })

    return selected_buses


@app.post("/calculate-travel-time")
async def calculate_travel_time(locations: List[LocationData], departure_searches: List[DepartureSearchData]):
    try:
        locations.append(reference_location)

        filter_request = {
            "locations": [{"id": loc.id, "coords": {"lat": loc.coords.lat, "lng": loc.coords.lng}} for loc in locations],
            "departure_searches": [{
                "id": dep_search.id,
                "arrival_location_ids": dep_search.arrival_location_ids,
                "departure_location_id": dep_search.departure_location_id,
                "departure_time": dep_search.departure_time,
                "travel_time": dep_search.travel_time,
                "properties": ["travel_time"],
                "transportation": {"type": "public_transport"}
            } for dep_search in departure_searches]
        }

        filter_response = await sdk.time_filter_fast_async(
            locations=filter_request["locations"],
            search_ids={filter_request["departure_searches"]
                        [0]["id"]: filter_request["departure_searches"]},
            transportation=Transportation(type="public_transport"),
            travel_time=filter_request["departure_searches"][0]["travel_time"],
            one_to_many=False
        )

        results = filter_response["results"][0]
        return results

    except Exception as e:
        return {"error": f"Erro ao calcular o tempo de viagem: {str(e)}"}
