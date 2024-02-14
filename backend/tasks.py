from celery import Celery
from bus_data import obter_dados_onibus

app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def obter_dados_periodicamente():
    data = obter_dados_onibus()
    # Processar os dados ou armazenar no Redis, conforme necessário
