import requests


def obter_dados_onibus():
    url = "https://dados.mobilidade.rio/gps/sppo?dataInicial=2024-01-29+15:40:00&dataFinal=2024-01-29+15:43:00"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Falha ao obter os dados. Código de status:", response.status_code)
        return None


def processar_dados_onibus(data):
    if data:
        # Processar os dados aqui (exemplo: adicionar um timestamp aos dados)
        for bus in data:
            # Exemplo de adição de timestamp
            bus['timestamp'] = '2024-01-29 15:45:00'
        return data
    else:
        return None
