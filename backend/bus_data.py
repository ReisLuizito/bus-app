import requests
import redis


def get_bus_data():
    url = "https://dados.mobilidade.rio/gps/sppo?dataInicial=2024-01-29+15:40:00&dataFinal=2024-01-29+15:43:00"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve erro na requisição
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Erro ao obter os dados dos ônibus:", e)
        return None


def update_redis_with_bus_data():
    bus_data = get_bus_data()

    if bus_data:
        r = redis.Redis(host='localhost', port=6379, db=0)
        for bus in bus_data:
            if all(key in bus for key in ["ordem", "latitude", "longitude", "datahora", "velocidade", "linha"]):
                bus_info = {
                    "latitude": bus["latitude"],
                    "longitude": bus["longitude"],
                    "datahora": bus["datahora"],
                    "velocidade": bus["velocidade"],
                    "linha": bus["linha"]
                }
                r.hset(bus["ordem"], mapping=bus_info)
            else:
                print("Dados incompletos para o ônibus:", bus)


update_redis_with_bus_data()
