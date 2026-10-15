def gorev_kaydi(baslik, *adimlar, oncelik="normal", **ekler):
    metin = f"[{oncelik.upper()}] {baslik}\n"

    for sira, adim in enumerate(adimlar,start=1):
        metin += f"{sira}. {adim}\n"

    for anahtar, deger in ekler.items():
        metin += f"{anahtar}: {deger}\n"


    return metin

if __name__ == "__main__":

    gorev_adımları = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ek_bilgiler = {"sorumlu": "Ayşe"}
    sonuc = gorev_kaydi("Kara deliğe atla" , *gorev_adımları , oncelik = "yüksek" , **ek_bilgiler) 

    print(sonuc)



def yakit_ekle(miktar, depo=None):
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo

print(yakit_ekle(10))
print(yakit_ekle(20))
