from celery import Celery
from bus_data import update_redis_with_bus_data

app = Celery('tasks', broker='pyamqp://guest@localhost//', backend='rpc')


@app.task
def update_bus_data():
    update_redis_with_bus_data()
