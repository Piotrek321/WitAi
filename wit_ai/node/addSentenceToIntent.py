#!/usr/bin/env python
#-*- coding: utf-8 -*-
import pycurl
import cStringIO
import json



def czyZawiera(tablica, doPorownania):

    indeks =[]

    for y in range(len(doPorownania)):
        for x in range(len(tablica)):
            if (doPorownania[y] in tablica[x]):
                indeks.append(x)


    if(len(indeks) == 1):
        return indeks
    elif(len(indeks) == 0):
        return znajdzPrawdopodobny(doPorownania)







def dodajNoweZdanie(jakaFunkcja, kierunek):
    i = 0
    jakaFunkcja = jakaFunkcja.title()
    jakaFunkcja = jakaFunkcja.split()

    indeks = []
    poszukiwanaFunkcja = "NULL"


    indeks = czyZawiera(funkcjeBezNawiasow, jakaFunkcja)



    if(indeks):
        poszukiwanaFunkcja = funkcjeBezNawiasow[indeks[0]]
        print "poszukiwanaFunkcja: " + str(poszukiwanaFunkcja)
        return poszukiwanaFunkcja


funkcjeBezNawiasow = ['Zrob Kolko', 'Wyswietl Dane' ,'Reset',
                    'Skasuj Historie Komend', 'Pokaz Funkcje','Pokaz Kolory',
                    'Stop', 'Nic', 'Ktorym Steruje', 'Wyswietl Historie Komend',
                    'Zmien Kolor','Skrec', 'Szybciej','Wolniej',
                    'Zmien Kontrole','Przywolaj Zolwia', 'Powtorz Komendy', 'Jedz']


z= 'Zrób kółko'
c= dodajNoweZdanie(z, 'a')


curl_header = ["Authorization: Bearer THAKYMA767MXNDXJOZXDUBGHGFIRW5ER",
                 "Content-Type: application/json"]
curl_url_0 = "https://api.wit.ai/intents/"
curl_url_1 = c
curl_url_1 = curl_url_1.replace(" ", "")
curl_url_2 = "/expressions?v=20150626"

curl_url = curl_url_0+str(curl_url_1)+curl_url_2

zdanie = "HEHEHEHEHEHE"


data = json.dumps( {"body":zdanie})
c = pycurl.Curl()
c.setopt(pycurl.URL, curl_url)
c.setopt(pycurl.HTTPHEADER,curl_header)
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, data)

c.perform()
