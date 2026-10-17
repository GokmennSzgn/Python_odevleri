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

def hedef_menusu(hedefler: list[str]) -> str:
    metin = "Nereye gitmek istersin:\n"
    for i, hedef in enumerate(hedefler):
        metin += f"[{i+1}]. {hedef}\n"
    return metin

print(envanter_metni(True, False, True))
print(envanter_metni(False, False, False))
print(hedef_menusu(["dünya", "mars", "jüpiter","sirius","orion"]))