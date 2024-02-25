import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from private_info import sender_email, receiver_email, password

def send_email(subject, body):   
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, password)

    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email Sent:")

    server.quit()
