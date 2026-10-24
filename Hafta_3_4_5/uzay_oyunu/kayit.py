from typing import Generator



def gorev_kaydi(baslik, *adimlar, oncelik="normal", **ekler):
    metin = f"[{oncelik.upper()}] {baslik}\n"

    for sira, adim in enumerate(adimlar,start=1):
        metin += f"{sira}. {adim}\n"

    for anahtar, deger in ekler.items():
        metin += f"{anahtar}: {deger}\n"


    return metin


def yakit_ekle(miktar, depo=None):
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo

print(yakit_ekle(10))
print(yakit_ekle(20))


def yakit_gostergesi(yakit: int, tuketim: int):
    while yakit > 0:
        yakit -= tuketim
        if yakit < 0:
            yield 0
            break
        yield yakit
        if yakit == 0:
            break


if __name__ == "__main__":

    gorev_adımları = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ek_bilgiler = {"sorumlu": "Ayşe"}
    sonuc = gorev_kaydi("Kara deliğe atla" , *gorev_adımları , oncelik = "yüksek" , **ek_bilgiler) 
    gosterge = yakit_gostergesi(100,30)
    yakit_listesi = list(gosterge)

    try:
            while True:
                kalan_yakit = next(gosterge)
                print(f"Kalan yakıt: {kalan_yakit}")
    except StopIteration:
        print("Yakıtın bitti, uzayda sürükleniyorsun...")
                
    print(sonuc)
    print(yakit_listesi)

    