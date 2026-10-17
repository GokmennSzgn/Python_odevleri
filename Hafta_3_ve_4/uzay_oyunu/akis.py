from itertools import islice
from itertools import takewhile
from pathlib import Path
from typing import Generator, Tuple, Iterable
from functools import lru_cache
from typing import Dict, List
import json
from pathlib import Path


def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b 

g = fibonacci()
ilk_uc = next(g), next(g), next(g)
ilk_on_iki = list(islice(fibonacci(),12))
yuzden_kucuk = list(takewhile(lambda x: x<100, fibonacci()))


def satirlari_oku(yol: str = "veri/seyir.txt") -> Generator[str, None, None]:
    
    mevcut_dizin = Path(__file__).resolve().parent
    ana_dizin = Path(__file__).resolve().parent.parent
    dosya_yolu = ana_dizin / yol

    if not dosya_yolu.exists():
        
        dosya_yolu = Path(yol)
    
    with open(dosya_yolu, "r", encoding="utf-8") as dosya:
        for satir in dosya:
            temiz_satir = satir.strip()
            if temiz_satir and not temiz_satir.startswith("#"):
                yield temiz_satir

def ayristir(satirlar: Iterable[str]) -> Generator[Tuple[str, str, int], None, None]:
    
    for satir in satirlar:
        temiz = satir.replace("->", "").replace(">", "")
        parcalar = temiz.split()
        if len(parcalar) == 3:
            kaynak, hedef, yakit_str = parcalar
            yield (kaynak, hedef, int(yakit_str))

def uzun_yolculuklar(kayitlar: Iterable[Tuple[str, str, int]], esik: int) -> Generator[str, None, None]:
    for kaynak, hedef, yakit in kayitlar:
        if yakit > esik:
            yield hedef


def rota_sayaci(baglantilar: Dict[str, List[str]]) -> Callable[[str, int], int]:
    """
    Verilen gezegen bağlantı sözlüğüne göre, @lru_cache ile optimize edilmiş 
    ve belirtilen adım sayısında yapılabilecek farklı rota sayısını hesaplayan 
    rota_sayisi fonksiyonunu döndürür.
    """
    
    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
       
        if adim == 0:
            return 1
        
        toplam_rota = 0
        
        komsular = baglantilar.get(gezegen, [])
        
        
        for komsu in komsular:
            toplam_rota += rota_sayisi(komsu, adim - 1)
            
        return toplam_rota

    return rota_sayisi


if __name__ == "__main__":

    mevcut_dizin = Path(__file__).resolve().parent  
    json_yolu = mevcut_dizin / "galaksi.json"  
    with open(json_yolu, "r", encoding="utf-8") as f:
        galaksi_verisi = json.load(f)


    toplam_yakit = sum(y for _, _, y in ayristir(satirlari_oku()))
    kayitlar = list(ayristir(satirlari_oku()))
    uzunlar = list(uzun_yolculuklar(kayitlar, 10))
    say = rota_sayaci(galaksi_verisi["baglantilar"])

    print("İlk üç terimi:",ilk_uc)
    print("İlk 12 terimi:",ilk_on_iki)
    print("Yüzden küçük terimler:",yuzden_kucuk)
    print("Toplam Yakıt:", toplam_yakit)
    print("Kayıtlar:",len(kayitlar))
    print("Uzun Yolculuk Hedefleri:", uzunlar)
    print("Dünya'dan 3, 10 ve 40 adımda rota sayıları:")
    print(say("dünya", 3),",",say("dünya", 10),",",say("dünya", 40))
    #!Fonksiyon çalışor ama istenenden farklı bir çıktı veriyor


