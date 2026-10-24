from typing import Callable, Any

KOMUTLAR: dict[str,tuple[Callable[...,Any],str]] = {}

from typing import Callable, Any

# Kayıt tutacağımız global sözlük
KOMUTLAR: dict[str, tuple[Callable[..., Any], str]] = {}

def komut(ad: str, aciklama: str = "") -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    
    def dekorator(func: Callable[..., Any]) -> Callable[..., Any]:
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' komutu zaten tanımlı!")
        
        KOMUTLAR[ad] = (func, aciklama)
        
        return func  
    return dekorator


@komut("yardim", aciklama="komutları listeler")
def yardim_komutu(durum: dict) -> str:
    cikti = []
    for isim, (fonk, aciklama) in KOMUTLAR.items():
        cikti.append(f"{isim}: {aciklama}")
    return "\n".join(cikti)

@komut("envanter", aciklama="envanter eşyalarını gösterir")
def envanter_komutu(durum: dict) -> str:
    credits = durum.get("credits", 0)
    return f"Credits: {credits}, Konum: {durum.get('konum', 'Bilinmiyor')}"

@komut("harita", aciklama="gidebileceğin gezegenleri gösterir")
def harita_komutu(durum: dict) -> str:
    konum = durum.get("konum")
    baglantilar = durum.get("baglantilar", {})
    gidilebilir = baglantilar.get(konum, [])
    return f"Mevcut konum: {konum}. Gidebileceğin yerler: {', '.join(gidilebilir)}"

