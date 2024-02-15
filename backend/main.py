from fastapi import FastAPI
from pydantic import BaseModel
import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import asyncio
from traveltimepy import TravelTimeSdk


app = FastAPI()

onibus_data = []
ponto_data = []
horario_data = []


class LocationSearchQuery(BaseModel):
    query: str


class OnibusSelecionado(BaseModel):
    linha: str


class PontoSelecionado(BaseModel):
    latitude: float
    longitude: float


class HorarioPartidaSelecionado(BaseModel):
    hora_partida: str


def send_notification_email(user_email, bus_line, arrival_time):
    sender_email = "seu_email@gmail.com"
    receiver_email = user_email
    password = "sua_senha"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = f"Notificação de Chegada do Ônibus da Linha {
        bus_line}"

    body = f"O ônibus da linha {
        bus_line} está a caminho! Chegará em aproximadamente {arrival_time} minutos."
    message.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

# Endpoints existentes para cadastrar ônibus, ponto e horário de partida


@app.post("/selecionar-onibus")
def selecionar_onibus(onibus: OnibusSelecionado):
    # Lógica para selecionar o ônibus
    return {"message": f"Ônibus {onibus.linha} selecionado com sucesso"}


@app.post("/selecionar-ponto")
def selecionar_ponto(ponto: PontoSelecionado):
    # Lógica para selecionar o ponto
    return {"message": "Ponto selecionado com sucesso"}


@app.post("/selecionar-horario-partida")
def selecionar_horario_partida(horario: HorarioPartidaSelecionado):
    # Lógica para selecionar o horário de partida
    return {"message": "Horário de partida selecionado com sucesso"}

# Endpoint raiz


@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de ônibus do Rio de Janeiro"}


@app.post("/verificar-notificacao")
def verificar_notificacao(dados: dict):
    # Lógica para verificar a posição dos ônibus e determinar se enviar notificação
    # Substitua esta lógica com a verificação real baseada nos dados recebidos

    # Exemplo de chamada da função de envio de e-mail
    send_notification_email(
        dados["email"], dados["linha"], dados["tempo_chegada"])

    return {"message": "Verificação de notificação realizada com sucesso"}
