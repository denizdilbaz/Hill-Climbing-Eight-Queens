# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 21:09:13 2022

@author: 05414015011
"""

import random
import time
import pandas as pd
import numpy as np

liste = [0,0,0,0,0,0,0,0]                                   # etkin gösterim için 8'lik dizi
komsuHList = [0,0,0,0,0,0,0,0]

def TahtayaYerlestir():
    for x in range(8):                  
        liste[x] = random.randint(1,8)
    
def anlikDurum():  # anlık kaç eleman birbirini yiyor.
    h = 0
    for a in range(8):                                             #bütün elemanların diğer elemanları yeme durumu için iç içe for döngüsü
        for x in range(8):
            if (x != a):                                           # elemanı kendisiyle karşılaştıramayız
                if (liste[x] == liste[a]):                         # yan yana yenilenler
                    h += 1
                elif (abs(liste[x] - liste[a]) == abs(x - a)):     # çapraz yenilebilenler
                    h += 1 
            else :
                continue   
    return int(h/2)    #h birbirlerini yiyebilen çiftler olduğu için 2ye böldüm

def enIyiKomsu(a):
    asil_deger = liste[a]
    enIyi = 999999999
    for x in range(8):
        if (x == asil_deger - 1 ):            # eğer kendi yerinde ise continue
            continue
        liste[a] = x + 1                    
        sonuc = anlikDurum()                #her döngüde sonucu alıyoruz 
        liste[a] = asil_deger
        if(sonuc < enIyi):
            enIyi = sonuc
            EnIyiKonum = x + 1
    return EnIyiKonum            


def enIyiKomsuHListesiniOlustur():
    for y in range(8):    
        nodeKonumu = y
        enIyiKomsusu = enIyiKomsu(nodeKonumu)
        a = liste[y]
        liste[y] = enIyiKomsusu
        h = anlikDurum()
        komsuHList[y] = h
        liste[y] = a


def hamleYaptir():
    enIyiKomsuHListesiniOlustur()
    minimum = min(komsuHList)
    indeksler = []
    i = 0
    for x in komsuHList:
        if (x == minimum):
            indeksler.append(i)
        i += 1
     
    sayi = random.randint(0,len(indeksler)-1)
    konum = indeksler[sayi]
    a = enIyiKomsu(konum)
    return konum,a


def anaAlgo():              
    hamle_sayisi = 0                                
    random_start_sayisi = 0
    TahtayaYerlestir()
    h = anlikDurum()                             
    print("Başlangıç",h)
    while(h > 0):
        index,c = hamleYaptir()
        a = liste[index]
        liste[index] = c
        sonuc = anlikDurum()
        liste[index] = a
        if (sonuc > h  or (hamle_sayisi > 100 and h==1) ):     # bazen h = 1 olduğunda ve en iyi değerler devamlı birbirini takip eden döngü haline geldiğinde daha kötü hamleye simulated annealingdeki gibi izin vermediği için daha iyi çözüm bulamayıp takılabiliyor. Fazla hamle sayısında da takılıyorsa random restart
            print("Yeni Tahta Oluşturuluyor")
            TahtayaYerlestir()
            h = anlikDurum()
            random_start_sayisi += 1
            hamle_sayisi = 0
        else:
            liste[index] = c
            hamle_sayisi += 1
            h = sonuc
            print("H:",h," dizi:",liste)
    print("Hamle Sayisi:",hamle_sayisi," Random Start Sayisi:",random_start_sayisi)
    return hamle_sayisi,random_start_sayisi






veriler = pd.DataFrame(np.arange(45).reshape(15,3),columns=["Hamle Sayısı","Random start sayısı","Süre"])
for x in range(15):
    baslangıc_zamani = time.time()
    hamle_sayisi,random_start_sayisi = anaAlgo()
    sure = (time.time() - baslangıc_zamani)
    sure = "{:.2f}".format(sure)
    veriler.loc[x]= [hamle_sayisi,random_start_sayisi,sure]
print("---------------------------------------------------")
print(veriler)
print("---------------------------------------------------")


    
    
    
    
    
    
    
    
    
    
    