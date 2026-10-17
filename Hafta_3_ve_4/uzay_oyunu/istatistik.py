
from functools import reduce
from functools import partial
import json
from pathlib import Path


mevcut_dizin = Path(__file__).resolve().parent  
json_yolu = mevcut_dizin / "galaksi.json"  
with open(json_yolu, "r", encoding="utf-8") as f:
        galaksi_verisi = json.load(f)

gezegenler = list(galaksi_verisi["baglantilar"].keys())
baglantilar = galaksi_verisi["baglantilar"]


# 1. YOL: map, filter ve reduce ile Çözüm

# a) Gezegen adlarının büyük harfli listesi (map ile)
buyuk_harf_map = list(map(str.upper, gezegenler))

# b) En az iki bağlantısı olan gezegenler (filter ile)
en_az_iki_baglanti_filter = list(
    filter(lambda g: len(baglantilar[g]) >= 2, gezegenler)
)

# c) Toplam bağlantı sayısı (reduce ile)
toplam_baglanti_reduce = reduce(
    lambda toplam, g: toplam + len(baglantilar[g]), gezegenler, 0
)

# 2. YOL: Liste Üreteci ve sum ile Çözüm

# a) Gezegen adlarının büyük harfli listesi Liste üreteci ile
buyuk_harf_liste = [g.upper() for g in gezegenler]

# b) En az iki bağlantısı olan gezegenler (iste üreteci ile
en_az_iki_baglanti_liste = [
    g for g, komsular in baglantilar.items() if len(komsular) >= 2
]

# c) Toplam bağlantı sayısı sum ile
toplam_baglanti_sum = sum(len(komsular) for komsular in baglantilar.values())


# PARTIAL İLE FONKSİYON TÜRETME

def yolculuk_suresi(mesafe: int, hiz: int):
    return mesafe / hiz

# functools.partial kullanarak hız sabitini 3 olarak ayarlıyoruz
hizli_yolculuk = partial(yolculuk_suresi, hiz=3)


# OKUNABİLİRLİK DEĞERLENDİRMESİ YORUM SATIRI
"""
Hangi yazımı daha okunaklı buluyorum?
-----------------------------------------------------------------
Yorum: Liste üreteçleri (List Comprehensions) ve sum fonksiyonu, 
map, filter ve reduce fonksiyonlarına kıyasla çok daha doğal, 
Pythonik ve okunabilirdir. Özellikle lambda ifadeleriyle karmaşıklaşabilen 
yapılar, liste üreteçlerinde tek satırda ve çok daha anlaşılır bir dille ifade edilebilir.
"""

if __name__ == "__main__":
    print("Büyük Harfli Gezegenler (Liste Üreteci):", buyuk_harf_liste)
    print("En Az 2 Bağlantısı Olanlar:", en_az_iki_baglanti_liste)
    print("Toplam Bağlantı Sayısı:", toplam_baglanti_sum)
    print("Hızlı Yolculuk (90 km, hız=3):", hizli_yolculuk(90))