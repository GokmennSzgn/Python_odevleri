
RAKAM = "0123456789ABCDEF"

def onluktan(n, taban):
    """Onluk tabandaki tam sayıyı (n) istenen tabana (2-16) çevirip metin döndürür."""
    if not (2 <= taban <= 16):
        raise ValueError("Taban 2 ile 16 arasında olmalıdır.")
    if n == 0:
        return "0"

    isaret = "-" if n < 0 else ""
    deger = abs(n)
    sonuc = ""

    # Kalanları RAKAM tablosundan alıp sonucun başına ekliyoruz
    while deger > 0:
        kalan = deger % taban
        sonuc = RAKAM[kalan] + sonuc
        deger //= taban

    return isaret + sonuc


def onluga(metin, taban):
    """Verilen tabandaki metni Horner yöntemiyle onluk tabana çevirir."""
    if not (2 <= taban <= 16):
        raise ValueError("Taban 2 ile 16 arasında olmalıdır.")

    temiz = metin.strip().upper()
    if len(temiz) == 0:
        raise ValueError("Boş metin dönüştürülemez.")

    isaret = -1 if temiz.startswith("-") else 1
    baslangic = 1 if temiz[0] in "+-" else 0
    sonuc = 0

    # Horner yöntemi: sonuç = sonuç * taban + basamak_degeri
    for i in range(baslangic, len(temiz)):
        deger = RAKAM.find(temiz[i])
        if deger < 0 or deger >= taban:
            raise ValueError(f"'{temiz[i]}' karakteri {taban} tabanı için geçersiz.")
        sonuc = sonuc * taban + deger

    return isaret * sonuc


if __name__ == "__main__":
    print(onluktan(2026, 2))
    print(onluktan(2026, 8))
    print(onluktan(2026, 16))
    print(onluga("7ea", 16))
    print(onluga("11111101010", 2))
    print(onluga("3752", 8))