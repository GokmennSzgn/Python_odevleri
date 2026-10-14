import json

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
    

if __name__ == "__main__":
    with open("Hafta_3/uzay_oyunu/galaksi.json", "r", encoding="utf-8") as dosya:
        veri = json.load(dosya)

    g = galaksi_kur(**veri)
    
    #print(g["baslangic"], g["yakit"])
    print(g["gezegenler"],
          g["baglantilar"],
          g["baslangic"],
          g["yakit"])
   
