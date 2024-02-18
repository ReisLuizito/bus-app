from celery import Celery
import requests
from datetime import datetime

app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def obter_dados_onibus():
    response = requests.get('http://127.0.0.1:8000/bus-data')
    data = response.json()
    return data


@app.task
def calcular_tempo_viagem(bus_position, selected_point):

    tempo_viagem = 30
    return tempo_viagem
