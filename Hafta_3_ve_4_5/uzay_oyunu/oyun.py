from dekoratorler import log_cagri


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

@log_cagri
def hedef_menusu(hedefler: list[str],hiz=3) -> str:
    metin = "Nereye gitmek istersin:\n"
    for i, hedef in enumerate(hedefler):
        metin += f" [{i+1}].{hedef}\n"
    return metin


#print(envanter_metni(True, False, True))
#print(envanter_metni(False, False, False))
#print(hedef_menusu(["dünya", "mars", "jüpiter","sirius","orion"]))
print(hedef_menusu(['dünya', 'mars', 'jüpiter','sirius','orion'], hiz=3))
