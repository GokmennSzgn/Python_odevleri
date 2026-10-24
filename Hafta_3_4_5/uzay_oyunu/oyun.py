from dekoratorler import log_cagri
import json 
from pathlib import Path
from komutlar import KOMUTLAR


def envanter_metni(credits:bool, engines: bool, copilot:bool) -> str:
    metin = "Sende: "
    if credits:
        metin += "Bol kredi,"
    else:
        metin += "Kredi yok,"
    if engines:
        metin += "güçlü motor,"
    else:
        metin += "motor yok,"
    if copilot:
        metin += "yetenekli bir yardımcı pilot"
    else:
        metin += "yardımcı pilot yok"
    return metin

#@log_cagri
def hedef_menusu(hedefler: list[str],hiz=3) -> str:
    metin = "Nereye gitmek istersin:\n"
    for i, hedef in enumerate(hedefler):
        metin += f" [{i+1}].{hedef}\n"
    return metin

dosya_yolu = Path(__file__).parent / "galaksi.json"
with open(dosya_yolu,"r",encoding="utf-8") as dosya:
    veri = json.load(dosya)


gezegen_listesi = veri["gezegenler"]
sonuc = hedef_menusu(gezegen_listesi, hiz=3)


#print(envanter_metni(True, False, True))
#print(envanter_metni(False, False, False))
#print(hedef_menusu(["dünya", "mars", "jüpiter","sirius","orion"]))
print(sonuc)


durum = {
    "konum": "dünya",
    "baglantilar": {
        "dünya": ["mars", "sirius", "orion", "jüpiter"]
    },
    "credits": 100,
    "engines": 2,
    "copilot": "robot"
}

# 2. KOMUTLAR sözlüğünden 'yardim' komutunu çekip çalıştıralım
if "yardim" in KOMUTLAR:
    fonk, aciklama = KOMUTLAR["yardim"]
    print("--- YARDIM KOMUTU ÇIKTISI ---")
    print(fonk(durum))

# 3. KOMUTLAR sözlüğünden 'harita' komutunu çekip çalıştıralım
if "harita" in KOMUTLAR:
    fonk, aciklama = KOMUTLAR["harita"]
    print("\n--- HARİTA KOMUTU ÇIKTISI ---")
    print(fonk(durum))
