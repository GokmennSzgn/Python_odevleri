
def vigenere(metin, anahtar, yon=1):
    """Metni anahtar kelimeye göre şifreler (yon=1) veya çözer (yon=-1)."""
    temiz_anahtar = ""
    for ch in anahtar:
        if "A" <= ch <= "Z" or "a" <= ch <= "z":
            temiz_anahtar += ch.upper()

    if len(temiz_anahtar) == 0:
        raise ValueError("Anahtar en az bir alfabetik harf içermelidir.")

    sonuc = ""
    j = 0  # Anahtar indeksi (yalnızca harf işlendiğinde artar)
    m = len(temiz_anahtar)

    for ch in metin:
        if "A" <= ch <= "Z":
            taban = ord("A")
            p = ord(ch) - taban
            k = ord(temiz_anahtar[j % m]) - ord("A")
            yeni = (p + yon * k) % 26
            sonuc += chr(taban + yeni)
            j += 1
        elif "a" <= ch <= "z":
            taban = ord("a")
            p = ord(ch) - taban
            k = ord(temiz_anahtar[j % m]) - ord("A")
            yeni = (p + yon * k) % 26
            sonuc += chr(taban + yeni)
            j += 1
        else:
            # Harf olmayan karakterler kaydırılmaz ve anahtar ilerlemez
            sonuc += ch

    return sonuc


if __name__ == "__main__":
    sifreli = vigenere("Attack at dawn", "LEMON")
    cozulmus = vigenere(sifreli, "LEMON", -1)
    print(sifreli)
    print(cozulmus)