from pydantic import BaseModel


class Onibus(BaseModel):
    ordem: str
    linha: str


class Ponto(BaseModel):
    latitude: float
    longitude: float


class HorarioPartida(BaseModel):
    hora_partida: str
