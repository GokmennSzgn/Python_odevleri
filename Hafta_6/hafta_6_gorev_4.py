

# --- A KISMI: Tek bir n sayısı için Collatz zinciri ---
n_giris = int(input("n: "))
gecici_n = n_giris
adim_sayisi = 0
en_yuksek_deger = gecici_n

while gecici_n > 1:
    # Ulaşılan en yüksek değeri takip ediyoruz
    if gecici_n > en_yuksek_deger:
        en_yuksek_deger = gecici_n
        
    # Kuralı koşullu ifadeyle tek satırda yazıyoruz (Çiftse n/2, tekse 3n+1)
    gecici_n = gecici_n // 2 if gecici_n % 2 == 0 else 3 * gecici_n + 1
    adim_sayisi += 1

print(f"{n_giris}->1: {adim_sayisi} adım, en yüksek değer {en_yuksek_deger}")


# --- B KISMI: Üst sınıra kadar en uzun zinciri bulan iç içe döngüler ---
ust_sinir = int(input("Üst sınır: "))

en_uzun_zincir_uzunlugu = 0
en_uzun_baslangic = 0

# 1'den üst sınıra kadar tüm sayıları tek tek deniyoruz (Dış döngü)
for sayi in range(1, ust_sinir + 1):
    aktif_sayi = sayi
    mevcut_adim = 0
    
    # Her sayının 1'e ulaşana kadar döneceği iç döngü
    while aktif_sayi > 1:
        aktif_sayi = aktif_sayi // 2 if aktif_sayi % 2 == 0 else 3 * aktif_sayi + 1
        mevcut_adim += 1
        
    # Eğer bu sayının zinciri şimdiye kadarkilerin en uzunundansa kaydediyoruz
    if mevcut_adim > en_uzun_zincir_uzunlugu:
        en_uzun_zincir_uzunlugu = mevcut_adim
        en_uzun_baslangic = sayi

print(f"1-{ust_sinir} arasında en uzun zincir: {en_uzun_baslangic} ({en_uzun_zincir_uzunlugu} adım)")