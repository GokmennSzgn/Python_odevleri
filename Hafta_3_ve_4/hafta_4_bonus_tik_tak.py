import time
from typing import Generator

def aralik(saniye: float) -> Generator[float, None, None]:
    baslangic = time.perf_counter()
    hedef = baslangic
    while True:
        hedef += saniye
        # Zamanın gelmesini bekleyen meşgul döngü (busy waiting)
        while time.perf_counter() < hedef:
            pass
        yield time.perf_counter() - baslangic

def bonus_zamanlayici():
    print("Zamanlayıcı başlatıldı (10 saniye sürecek)...")
    
    # 2 ve 5 saniyelik üreteçleri başlatalım
    tik_gen = aralik(2)
    tak_gen = aralik(5)
    
    # İlk değerleri alalım
    sonraki_tik = next(tik_gen)
    sonraki_tak = next(tak_gen)
    
    baslangic_zamani = time.perf_counter()
    
    while True:
        simdiki_zaman = time.perf_counter() - baslangic_zamani
        
        # 10 saniye sınırını kontrol edelim
        if simdiki_zaman >= 10.0:
            print("Süre doldu!")
            break
            
        # Hangi olay daha önce gerçekleşecekse onu yakalayalım
        if sonraki_tik <= sonraki_tak and sonraki_tik <= 10.0:
            print(f"{sonraki_tik:.1f}s -> tik")
            sonraki_tik = next(tik_gen)
        elif sonraki_tak < sonraki_tik and sonraki_tak <= 10.0:
            print(f"{sonraki_tak:.1f}s -> tak")
            sonraki_tak = next(tak_gen)

if __name__ == "__main__":
    bonus_zamanlayici()