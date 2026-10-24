from itertools import islice
from uzay_oyunu.dekoratorler import sure_olc
from uzay_oyunu.dekoratorler import log_cagri


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