
import time
from functools import wraps
from typing import Callable, Any
from functools import lru_cache
import functools


# Hafta 5 - Görev 1: Süre ölçen dekoratörümüz
def sure_olc(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        baslangic = time.perf_counter()
        sonuc = func(*args, **kwargs)
        bitis = time.perf_counter()
        sure = bitis - baslangic
        print(f"{func.__name__}: {sure:.4f} sn")
        return sonuc
    return wrapper

# Hafta 4'ten kalan Önbelleksiz Rota Sayacı Fonksiyonu (Örnek Galaksi Yapısı ile)
def rota_sayaci_onbelleksiz(baglantilar):
    def rota_sayisi(gezegen, adim):
        if adim == 0:
            return 1
        toplam = 0
        for komsu in baglantilar.get(gezegen, []):
            toplam += rota_sayisi(komsu, adim - 1)
        return toplam
    return rota_sayisi



def say(func: Callable[..., Any]) -> Callable[..., Any]:
    
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        wrapper.cagri += 1  
        return func(*args, **kwargs)
    
    wrapper.cagri = 0
    return wrapper


# Örnek 1: Yalnızca @say
@say
def fib_1(n: int) -> int:
    if n < 2:
        return n
    return fib_1(n - 1) + fib_1(n - 2)

# Örnek 2: @say üstte, @lru_cache altta
@say
@lru_cache(maxsize=None)
def fib_2(n: int) -> int:
    if n < 2:
        return n
    return fib_2(n - 1) + fib_2(n - 2)

# Örnek 3: @lru_cache üstte, @say altta
@lru_cache(maxsize=None)
@say
def fib_3(n: int) -> int:
    if n < 2:
        return n
    return fib_3(n - 1) + fib_3(n - 2)



def log_cagri(func: Callable[..., Any]) -> Callable[..., Any]:
    
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Argümanları okunabilir bir formata getirelim (örneğin 'orion', hiz=3 gibi)
        args_str = ", ".join([repr(arg) for arg in args])
        kwargs_str = ", ".join([f"{k}={v!r}" for k, v in kwargs.items()])
        
        # Hepsini birleştirip çağrı öncesi logu basalım
        tum_argumanlar = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"-> {func.__name__}({tum_argumanlar})")
        
        # Orijinal fonksiyonu çalıştırıp sonucunu alıyoruz
        sonuc = func(*args, **kwargs)
        
        # Çağrı sonrası dönüş değerini loglayalım
        print(f"<<- {func.__name__} {sonuc!r}")
        
        return sonuc
    return wrapper




if __name__ == "__main__":
    # Örnek galaksi bağlantı ağı
    ornek_galaksi = {
        "baglantilar": {
            "dünya": ["sirius", "orion"],
            "sirius": ["orion", "kara_delik", "centauri"],
            "orion": ["centauri", "sirius"],
            "centauri": ["orion"],
            "kara_delik": ["orion"]
        }
    }

    # Fonksiyonu dekoratör ile sarmalıyoruz
    say = sure_olc(rota_sayaci_onbelleksiz(ornek_galaksi["baglantilar"]))

    
    sonuc = say("dünya", 20)
    print(f"Toplam Rota Sayısı: {sonuc}")

    #fibonacci çıktıları
    fib_1(20)
    print(f"Yalnızca @say: {fib_1.cagri}")  

    fib_2(20)
    print(f"@say üstte, @lru_cache altta: {fib_2.cagri}")  

    fib_3(20)
    print(f"@lru_cache üstte, @say altta: {fib_3.__wrapped__.cagri}")



    def sinirla(alt: int, ust: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    
        def dekorator(func: Callable[..., Any]) -> Callable[..., Any]:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                # Fonksiyona gönderilen ilk argümanı kontrol ediyoruz (*args'ın ilk elemanı)
                if args:
                    ilk_arguman = args[0]
                    
                    if not (alt <= ilk_arguman <= ust):
                        raise ValueError(f"{func.__name__}: {ilk_arguman} değeri {alt}-{ust} aralığında değil")
                
                return func(*args, **kwargs)
            
            return wrapper
        return dekorator

# --- Yakıt Harca Fonksiyonu ---
@sinirla(0, 100)
def yakit_harca(miktar: int) -> int:
    yakit = (100 - miktar)
    return f"Yakıt miktarı: {yakit}"  

print("--> yakit_harca(30)")
print(yakit_harca(30))
#print("--> yakit_harca(150)")
#print(yakit_harca(150))



def hafiza(maxsize: int | None = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:

    def dekorator(func: Callable[..., Any]) -> Callable[..., Any]:
        # Önbelleği tutacağımız sözlük (closure içinde saklanır)
        onbellek: dict[tuple[Any, ...], Any] = {}
        
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Parametreleri anahtar (key) olarak kullanabilmek için tuple yapıyoruz
            # (kwargs sözlük olduğu için hashlenemez, bu yüzden tuple'a çeviriyoruz)
            anahtar = args + tuple(sorted(kwargs.items()))
            
            # 1. Eğer sonuç önbellekte varsa, doğrudan oradan döndür 
            if anahtar in onbellek:
                return onbellek[anahtar]
            
            # 2. Sonuç önbellekte yoksa, orijinal fonksiyonu çalıştır ve sonucu al
            sonuc = func(*args, **kwargs)
            
            # 3. maxsize sınırı var mı ve önbellek doldu mu kontrol et
            if maxsize is not None and len(onbellek) >= maxsize:
                # Sözlükteki ilk (en eski) anahtarı al ve sil 
                en_eski_anahtar = next(iter(onbellek))
                del onbellek[en_eski_anahtar]
            
            # 4. Yeni sonucu önbelleğe kaydet
            onbellek[anahtar] = sonuc
            return sonuc
            
        return wrapper
    return dekorator


