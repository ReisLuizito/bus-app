import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


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

# Exemplo de uso:
# send_notification_email("email_usuario@example.com", "123", 10)
