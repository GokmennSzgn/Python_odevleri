
def onluktan_romaya(sayi):
    """1-3999 arasındaki onluk tam sayıyı Roma rakamı metnine çevirir."""
    if not (1 <= sayi <= 3999):
        raise ValueError("Roma rakamı dönüşümü için sayı 1 ile 3999 arasında olmalıdır.")

    kalan = sayi
    roma = ""

    while kalan >= 1000:
        roma += "M"
        kalan -= 1000
    if kalan >= 900:
        roma += "CM"
        kalan -= 900
    if kalan >= 500:
        roma += "D"
        kalan -= 500
    if kalan >= 400:
        roma += "CD"
        kalan -= 400
    while kalan >= 100:
        roma += "C"
        kalan -= 100
    if kalan >= 90:
        roma += "XC"
        kalan -= 90
    if kalan >= 50:
        roma += "L"
        kalan -= 50
    if kalan >= 40:
        roma += "XL"
        kalan -= 40
    while kalan >= 10:
        roma += "X"
        kalan -= 10
    if kalan >= 9:
        roma += "IX"
        kalan -= 9
    if kalan >= 5:
        roma += "V"
        kalan -= 5
    if kalan >= 4:
        roma += "IV"
        kalan -= 4
    while kalan >= 1:
        roma += "I"
        kalan -= 1

    return roma


def _roma_tek_deger(ch):
    """Tek bir Roma karakterinin onluk değerini döndürür; geçersizse -1 verir."""
    if ch == "I":
        return 1
    if ch == "V":
        return 5
    if ch == "X":
        return 10
    if ch == "L":
        return 50
    if ch == "C":
        return 100
    if ch == "D":
        return 500
    if ch == "M":
        return 1000
    return -1


def romadan_onluga(roma_metin):
    """Roma rakamı metnini (ör. 'XLII') onluk tam sayıya (42) çevirir."""
    metin = roma_metin.strip().upper()
    if len(metin) == 0:
        raise ValueError("Boş Roma rakamı dönüştürülemez.")

    toplam = 0
    onceki_deger = 0

    # Sağdan sola ilerleyerek küçük değer öndeyse çıkar, büyük/eşitse ekle
    for i in range(len(metin) - 1, -1, -1):
        deger = _roma_tek_deger(metin[i])
        if deger == -1:
            raise ValueError(f"Geçersiz Roma karakteri: {metin[i]}")

        if deger < onceki_deger:
            toplam -= deger
        else:
            toplam += deger
            onceki_deger = deger

    return toplam


if __name__ == "__main__":
    print(onluktan_romaya(2026))
    print(onluktan_romaya(1994))
    print(romadan_onluga("XLII"))