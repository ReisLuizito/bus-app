from celery import Celery

celery = Celery('tasks', broker='pyamqp://guest@localhost//')

@celery.task
def send_notification(bus_line, email):
    
    subject = f"Notificação: Ônibus da Linha {bus_line} está chegando!"
    message = f"O ônibus da Linha {
        bus_line} está a 10 minutos ou menos de distância."
    from_email = 'seu_email@gmail.com'  
    recipient_list = [email]
