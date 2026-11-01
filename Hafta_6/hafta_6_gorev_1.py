
import math

# --- 1. GİRDİ ---
print("Lütfen üçgenin kenar uzunluklarını giriniz:")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# --- 2. DOĞRULA VE DÜZENLE ---
# Kenarların pozitif olup olmadığını ve en uzun kenarın 'a' olmasını sağlıyoruz
# (Büyükten küçüğe sıralama mantığı - liste kullanmadan)
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
# Bu aşamadan sonra 'a' kesinlikle en büyük (en uzun) kenardır.

# Hata kontrolü: Kenarlar pozitif mi ve üçgen eşitsizliği sağlanıyor mu? (a < b + c)
if a <= 0 or b <= 0 or c <= 0 or a >= b + c:
    print("HATA: Girilen kenarlar pozitif değil veya üçgen eşitsizliği sağlanmıyor!")
else:
    # --- 3. İŞLE ---
    
    # A) Kenarlarına göre tür belirleme
    if a == b == c:
        kenar_turu = "Eşkenar"
    elif a == b or b == c or a == c:
        kenar_turu = "İkizkenar"
    else:
        kenar_turu = "Çeşitkenar"
        
    # B) Çevre ve Alan (Heron Formülü) hesaplama
    cevre = a + b + c
    u = cevre / 2
    alan = math.sqrt(u * (u - a) * (u - b) * (u - c))
    
    # C) En büyük açı hesaplama (a en uzun kenar olduğu için karşısındaki açı en büyüktür)
    # cos(alpha) = (b^2 + c^2 - a^2) / (2 * b * c)
    kosinus_degeri = (b**2 + c**2 - a**2) / (2 * b * c)
    
    # Küsürat hatalarını önlemek için kosinüs değerini [-1, 1] aralığında sınırlandırıyoruz
    if kosinus_degeri > 1.0:
        kosinus_degeri = 1.0
    elif kosinus_degeri < -1.0:
        kosinus_degeri = -1.0
        
    aci_radyan = math.acos(kosinus_degeri)
    en_buyuk_aci = math.degrees(aci_radyan)
    
    # D) Açı türüne göre sınıflandırma (math.isclose kullanarak dik açı kontrolü)
    if math.isclose(en_buyuk_aci, 90.0, abs_tol=1e-9):
        aci_turu = "Dik açılı"
    elif en_buyuk_aci < 90.0:
        aci_turu = "Dar açılı"
    else:
        aci_turu = "Geniş açılı"
        
    # --- 4. ÇIKTI ---
    print(f"Tür: {kenar_turu}, {aci_turu}")
    print(f"Çevre: {cevre:.2f} Alan: {alan:.2f} En büyük açı: {en_buyuk_aci:.2f}°")