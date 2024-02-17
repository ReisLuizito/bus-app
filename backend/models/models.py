from pydantic import BaseModel


class Onibus(BaseModel):
    ordem: str
    linha: str
    latitude: float
    longitude: float
    datahora: int
    velocidade: float


class Ponto(BaseModel):
    latitude: float
    longitude: float


class HorarioPartida(BaseModel):
    hora_partida: str
