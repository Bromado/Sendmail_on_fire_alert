from flask import Flask
from flask_mail import Mail, Message
from datetime import datetime, timedelta
import pytz
import os

app = Flask(__name__)

# Konfigurieren der Mail-Einstellungen
app.config['MAIL_SERVER'] = 'YOUR_MAILSERVER'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'YOUR_LOGIN_USERNAME'
app.config['MAIL_PASSWORD'] = 'YOUR_LOGIN_PASSWORD'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

LAST_EMAIL_FILE = "last_email_sent.txt"

def save_last_email_time(time):
    with open(LAST_EMAIL_FILE, 'w') as file:
        file.write(time.strftime("%Y-%m-%d %H:%M:%S"))

def load_last_email_time():
    if os.path.exists(LAST_EMAIL_FILE):
        with open(LAST_EMAIL_FILE, 'r') as file:
            time_str = file.read().strip()
            if time_str:
                return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=pytz.timezone('Europe/Berlin'))
    return None

def can_send_email():
    last_email_time = load_last_email_time()
    if last_email_time is None:
        return True
    now = datetime.now(pytz.timezone('Europe/Berlin'))
    return now - last_email_time >= timedelta(hours=1)

def is_weekday_and_time():
    timezone = pytz.timezone('Europe/Berlin')
    now = datetime.now(timezone)
    return now.weekday() < 5 and 7 <= now.hour < 15


@app.route('/sendmail/YOUR_URL_SUFFIX')
def send_mail():
    timezone = pytz.timezone('Europe/Berlin')
    now = datetime.now(timezone)
    if is_weekday_and_time() and can_send_email():
      zeitstempel=now.strftime("%d.%m.%Y")
      zeitstempel_uhrzeit=now.strftime("%H:%M")
      msg = Message('Information Feuerwehreinsatz YOUR NAME', 
                    sender='YOUR MAIL ADDRESS', 
                    recipients=['RECIPIENT1','RECIPIENT2'])
      msg.body = 'Liebe Kolleginnen und Kollegen,\n\nIch wurde soeben am '+zeitstempel+' um '+zeitstempel_uhrzeit+' Uhr zu einem dringenden Feuerwehreinsatz gerufen und muss daher das Home Office verlassen. Ich werde mein Bestes tun, um so schnell wie möglich wieder zur Arbeit zurückzukehren. Vielen Dank für euer Verständnis und eure Unterstützung.\n\nViele Grüße\nYOUR NAME\n\n(Dies ist eine automatisch versandte E-Mail.)'
      mail.send(msg)
      save_last_email_time(datetime.now(pytz.timezone('Europe/Berlin')))
      return 'E-Mail gesendet!'
    else:
        return 'E-Mail wird nur werktags zwischen 7 und 15 Uhr gesendet.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345, debug=True)
