import requests

url = "https://dados.mobilidade.rio/gps/sppo?dataInicial=2024-01-29+15:40:00&dataFinal=2024-01-29+15:43:00"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Aqui você pode processar os dados recebidos
else:
    print("Erro ao obter os dados dos ônibus. Status code:", response.status_code)
