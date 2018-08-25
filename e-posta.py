# !/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText


def epostagonder(gonderen,sifre,kime,baslik,icerik):
    print("Gönderilecek Mail Hazırlanıyor, Lütfen Bekleyiniz.")
    Gonderilecek_adres = [kime]
    Baslik = baslik
    icerik = icerik
    Gonderen_adres = gonderen
    Gonderen_sifre = sifre
    #'efsclhmuujkbtzkl'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(Gonderen_adres, Gonderen_sifre)


    mail = MIMEText(icerik, 'html', 'utf-8')
    mail['From'] = Gonderen_adres
    mail['Subject'] = Baslik
    mail['To'] = ','.join(Gonderilecek_adres)

    mail = mail.as_string()
    print("Lütfen bekleyiniz. Mail gönderiliyor..")

    try:
        server.sendmail(Gonderen_adres, Gonderilecek_adres, mail)
        print ('Mail Başarıyla Gönderildi')
    except:
        print ('Mail Gönderirken Bir Sorun Oluştur!')



