
ALFABE = "abcçdefgğhıijklmnoöprsştuüvyz"


def _tr_kucuk_karakter(ch):
    """Tek bir karakteri Türkçe kurallarına göre küçük harfe çevirir."""
    if ch == "İ":
        return "i"
    if ch == "I":
        return "ı"
    if ch == "Ç":
        return "ç"
    if ch == "Ğ":
        return "ğ"
    if ch == "Ö":
        return "ö"
    if ch == "Ş":
        return "ş"
    if ch == "Ü":
        return "ü"
    return ch.lower()


def _tr_buyuk_karakter(ch):
    """Tek bir karakteri Türkçe kurallarına göre büyük harfe çevirir."""
    if ch == "i":
        return "İ"
    if ch == "ı":
        return "I"
    if ch == "ç":
        return "Ç"
    if ch == "ğ":
        return "Ğ"
    if ch == "ö":
        return "Ö"
    if ch == "ş":
        return "Ş"
    if ch == "ü":
        return "Ü"
    return ch.upper()


class TrKelime:
    """Türkçe alfabe sırasına göre karşılaştırma ve dönüşüm yapan kelime sınıfı."""

    def __init__(self, metin):
        """Gelen metni Türkçe kurala göre küçük harfe çevirip saklar."""
        kucuk_metin = ""
        for ch in metin:
            kucuk_metin += _tr_kucuk_karakter(ch)
        self._metin = kucuk_metin

    def __str__(self):
        """Kelimenin küçük harfli metin temsilini döndürür."""
        return self._metin

    def __len__(self):
        """Kelimedeki karakter sayısını döndürür."""
        return len(self._metin)

    def __getitem__(self, indeks):
        """İndeks veya dilim erişimini destekler."""
        return self._metin[indeks]

    def __contains__(self, alt_metin):
        """Verilen alt metnin (veya karakterin) Türkçe küçük haliyle kelimede olup olmadığını döndürür."""
        if not isinstance(alt_metin, str):
            return False
        aranan = ""
        for ch in alt_metin:
            aranan += _tr_kucuk_karakter(ch)
        return aranan in self._metin

    def __eq__(self, diger):
        """İki TrKelime nesnesinin eşitliğini denetler."""
        if not isinstance(diger, TrKelime):
            return NotImplemented
        return self._metin == diger._metin

    def __lt__(self, diger):
        """Kelimeleri ALFABE sırasına göre karşılaştırır; ön ekse kısa olan küçüktür."""
        if not isinstance(diger, TrKelime):
            return NotImplemented

        uzunluk_1 = len(self._metin)
        uzunluk_2 = len(diger._metin)
        sinir = uzunluk_1 if uzunluk_1 < uzunluk_2 else uzunluk_2

        for i in range(sinir):
            c1 = self._metin[i]
            c2 = diger._metin[i]
            if c1 != c2:
                idx1 = ALFABE.find(c1)
                idx2 = ALFABE.find(c2)
                if idx1 != -1 and idx2 != -1:
                    return idx1 < idx2
                return c1 < c2

        return uzunluk_1 < uzunluk_2

    def buyuk(self):
        """Kelimenin Türkçe kurallarına göre büyük harfli halini döndürür."""
        buyuk_metin = ""
        for ch in self._metin:
            buyuk_metin += _tr_buyuk_karakter(ch)
        return buyuk_metin


if __name__ == "__main__":
    print("çay < dağ (TR):", TrKelime("çay") < TrKelime("dağ"), "| Python:", "çay" < "dağ")
    print("ılık < iğne (TR):", TrKelime("ılık") < TrKelime("iğne"), "| Python:", "ılık" < "iğne")
    print("ördek < pasta (TR):", TrKelime("ördek") < TrKelime("pasta"), "| Python:", "ördek" < "pasta")
    print(TrKelime("Işık") == TrKelime("ışık"))

    k = TrKelime("İSTANBUL")
    print(k, len(k), "tan" in k, k.buyuk())