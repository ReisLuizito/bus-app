from fastapi import FastAPI
from pydantic import BaseModel
import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import asyncio
from traveltimepy import TravelTimeSdk
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
sdk = TravelTimeSdk("8097a90e", "90bf31f1a51cfd508e0d50b0f6ef69a7")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

onibus_data = []
ponto_data = []
horario_data = []


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
        return {"linhas": list(linhas)}
    else:
        return {"error": "Erro ao obter as linhas de ônibus"}
