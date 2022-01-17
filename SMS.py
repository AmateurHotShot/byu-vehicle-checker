import smtplib
from email.message import EmailMessage


def sendSMS(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['to'] = to

    user = "joepooleiot@gmail.com"
    msg['from'] = user
    password = "qxgfwrbpknqtukmt"
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

if __name__ == "__main__":
    sendSMS("", "testing this out", "5034535511@tmomail.net")