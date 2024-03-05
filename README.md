Dieses Projekt dient dazu einen Flask-Server als Docker Container zu betreiben. Ziel ist es bei einer Feuerwehralarmierung an einem Werktag 
zwischen 7 und 15 Uhr automatisiert eine Mail an Arbeitskollegen (oder sonst wen) zu versenden um diese über die Abwesenheit zu informieren. 
Wird die URL zum Flask-Server aufgerufen, so wird automatisch die vorgefertigte Mail über ein bestehendes Mailkonto via SMTP verschickt. 
Der Flask Server wird mittels HTTPS angesprochen, ein NGINX Reverse Proxy leitet die Anfragen dann intern weiter. Dazu ist es vorab notwendig,
ein entsprechendes Zertifikat für die SSL-Verschlüsselung zu besitzen. In meinem Fall nutze ich let's encrypt (eine kleine Anleitung findet
sich z.B. hier: https://www.inmotionhosting.com/support/website/ssl/lets-encrypt-ssl-ubuntu-with-certbot/). 
Das Skript kann dann z.B. in der Feuersoftware Connect Oberfläche als Benutzer-Webhook eingebunden werden (idealerweise bei Status "Ich komme").
Das Skript sendet innerhalb einer Stunde nur eine Mail (falls man mal mehrfach auf den Zusagen Button drückt).

Um dieses Tool selbst zu betreiben sind einige kleine Anpassungen zwingend notwendig:

app.py
1. Anpassen des eigenen Mailkontos (YOUR_MAILSERVER, YOUR_LOGIN_USERNAME, YOUR_LOGIN_PASSWORD)
2. Anpassen des Mailtextes und der Mailadressen(YOUR NAME, YOUR MAIL ADDRESS, RECIPIENT1, RECIPIENT2)
3. Anpassen der eigenen URL (YOUR_URL_SUFFIX)

nginx.conf
1. Anpassen des eigenen Server-Namens (YOUR_SERVER_NAME)
2. Anpassen des Pfades zu den eigenen SSL-Zertifikaten (YOUR_PATH)


Nachdem die eigenen Änderungen umgesetzt wurden kann das System mittels `docker compose up -d` als Kommandozeilenbefehl gestartet werden. Läuft alles korrekt 
versendet der Server automatisch die Mail, wenn die URL https://SERVERNAME/sendmail/YOUR_URL_SUFFIX aufgerufen wird.

