from itertools import islice
from uzay_oyunu.dekoratorler import sure_olc
from uzay_oyunu.dekoratorler import log_cagri
import functools
from uzay_oyunu.dekoratorler import hafiza


def test_yakit_ekle(miktar, depo=[]):
 depo.append(miktar)
 return depo

print(test_yakit_ekle(10))
print(test_yakit_ekle(20))


def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b 

g = fibonacci()

birinci_dilim = list(islice(g, 5))
print("Birinci islice çağrısı:", birinci_dilim)

ikinci_dilim = list(islice(g, 5))
print("İkinci islice çağrısı:", ikinci_dilim)



def test_sure_olc_koruma_ve_sonuc():
    @sure_olc
    def ornek_fonksiyon(x: int, carpfan: int = 2) -> int:
        """Örnek docstring"""
        return x * carpfan

    # İsim ve docstring korunuyor mu?
    assert ornek_fonksiyon.__name__ == "ornek_fonksiyon"
    assert ornek_fonksiyon.__doc__ == "Örnek docstring"

    # Adlı argüman ve sonuç doğru dönüyor mu?
    sonuc = ornek_fonksiyon(5, carpfan=3)
    assert sonuc == 15


def test_log_cagri():
    @log_cagri
    def test_yolculuk(gezegen: str, hiz: int = 3) -> str:
        return f"{gezegen} hiz={hiz}"

    donus = test_yolculuk('orion', hiz=3)   
    assert donus == "orion hiz=3"
    assert test_yolculuk.__name__ == "test_yolculuk"


#Hafta 5 bonus görev hafıze testleri:

def test_hafiza_ve_lru_cache_karsilastirma():
    # 1. Kendi hafiza dekoratörümüzle bir test fonksiyonu
    @hafiza(maxsize=3)
    def topla_hafiza(a: int, b: int) -> int:
        return a + b

    # 2. Python'un resmi lru_cache dekoratörüyle aynı işi yapan fonksiyon
    @functools.lru_cache(maxsize=3)
    def topla_lru(a: int, b: int) -> int:
        return a + b

    # Sonuçların aynı olup olmadığını test ediyoruz
    parametreler = [(2, 3), (5, 10), (2, 3), (1, 1), (5, 10)]
    
    for a, b in parametreler:
        sonuc_hafiza = topla_hafiza(a, b)
        sonuc_lru = topla_lru(a, b)
        
        # Her iki yöntem de aynı matematiksel sonucu vermeli
        assert sonuc_hafiza == sonuc_lru
        
    # Önbellek kapasitesi (maxsize=3) aşıldığında eski girdileri silme mantığı test ediliyor
    # Yeni çağrılar hata vermeden doğru çalışmaya devam etmeli
    assert topla_hafiza(100, 200) == 300
    assert topla_lru(100, 200) == 300