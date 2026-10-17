import json
import os
import time

def galaksi_kur(gezegenler, baglantilar, baslangic, **kwargs):
    if baslangic not in gezegenler:
        raise ValueError("Başlangıç gezegeni gezegenler listesinde bulunamadı!")

    yakit = kwargs.get("yakit", 50)

    return  {
    "gezegenler": gezegenler,
    "baglantilar": baglantilar,
    "baslangic": baslangic,
    "yakit": yakit   
    }


def hamle_sayaci():
    sayac = 0
    def say():
        nonlocal sayac
        sayac += 1
        return sayac
    return say

def en_bagli_gezegenler(galaksi):
    baglantilar = galaksi["baglantilar"]
    gezegenler = galaksi["gezegenler"]
    siralama = sorted(gezegenler, key=lambda g: (-len(baglantilar.get(g, [])), g))
    return siralama


def sure_olc(fonksiyon):
    def sarmalayici(*args, **kwargs):
        baslangic_zamani = time.time()  
        sonuc = fonksiyon(*args, **kwargs)  
        bitis_zamani = time.time()  
        gecen_sure = bitis_zamani - baslangic_zamani
        print(f"[{fonksiyon.__name__}] Çalışma süresi: {gecen_sure:.6f} saniye")
        return sonuc
    return sarmalayici


if __name__ == "__main__":

    hamle_al = hamle_sayaci()
    toplam_hamle = 0
    for _ in range(13):
        toplam_hamle = hamle_al()

    
    dosya_dizini = os.path.dirname(os.path.abspath(__file__))
    dosya_yolu = os.path.join(dosya_dizini, "galaksi.json")

    with open(dosya_yolu, "r", encoding="utf-8") as dosya:
        veri = json.load(dosya)

    g = galaksi_kur(**veri)
    en_bagli_gezegenler = sure_olc(en_bagli_gezegenler)
    sirali_gezegenler = en_bagli_gezegenler(g)

    print("Başlangıç konumu: ",g["baslangic"], "Yakıt: ",g["yakit"])
    print(f"Oyunu {toplam_hamle} hamlede bitirdin!")
    print(sirali_gezegenler)

    