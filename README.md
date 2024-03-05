Dieses Projekt dient dazu einen Flask-Server als Docker Container zu betreiben. Ziel ist es bei einer Feuerwehralarmierung an einem Werktag 
zwischen 7 und 15 Uhr automatisiert eine Mail an Arbeitskollegen (oder sonst wen) zu versenden um diese über die Abwesenheit zu informieren. 
Wird die URL zum Flask-Server aufgerufen, so wird automatisch die vorgefertigte Mail über ein bestehendes Mailkonto via SMTP verschickt. 
Der Flask Server wird mittels HTTPS angesprochen, ein NGINX Reverse Proxy leitet die Anfragen dann intern weiter. Dazu ist es vorab notwendig,
ein entsprechendes Zertifikat für die SSL-Verschlüsselung zu besitzen. In meinem Fall nutze ich let's encrypt (eine kleine Anleitung findet
sich z.B. hier: https://www.inmotionhosting.com/support/website/ssl/lets-encrypt-ssl-ubuntu-with-certbot/). 
