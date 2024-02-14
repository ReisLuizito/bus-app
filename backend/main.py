from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

onibus_data = []
ponto_data = []
horario_data = []


@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de ônibus do Rio de Janeiro"}


class Onibus(BaseModel):
    ordem: str
    linha: str


class Ponto(BaseModel):
    latitude: float
    longitude: float


class HorarioPartida(BaseModel):
    hora_partida: str


@app.post("/cadastrar-onibus")
def cadastrar_onibus(onibus: Onibus):
    onibus_data.append(onibus)
    return {"message": "Ônibus cadastrado com sucesso"}


@app.post("/cadastrar-ponto")
def cadastrar_ponto(ponto: Ponto):
    ponto_data.append(ponto)
    return {"message": "Ponto cadastrado com sucesso"}


@app.post("/cadastrar-horario-partida")
def cadastrar_horario_partida(horario: HorarioPartida):
    horario_data.append(horario)
    return {"message": "Horário de partida cadastrado com sucesso"}
