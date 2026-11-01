
cümle = input("Cümle giriniz: ")


harf_sayisi = 0
sesli_sayisi = 0
sessiz_sayisi = 0
rakam_sayisi = 0
kelime_sayisi = 0
kelimede_miyiz = False
ters_cumle = ""
sadece_harfler = ""
kucuk_harfler_str = "abcçdefgğhıijklmnoöprsştuüvyzAEIİOÖUÜABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

for index in range(len(cümle)):
    # 1. Ters çevirme için karakter al
    karakter = cümle[len(cümle) - 1 - index]
    ters_cumle += karakter
    
    # 2. Analiz için o anki karakteri al
    k = cümle[index]
    
    # Harf kontrolü (Türkçe karakterleri de kapsayacak şekilde basitçe alfabe kontrolü)
    if ('a' <= k <= 'z') or ('A' <= k <= 'Z') or k in "çğışöüÇĞİŞÖÜâîûÂÎÛ":
        harf_sayisi += 1
        
        # Sesli / Sessiz ayrımı
        if k in "aelioöuüAEIİOÖUÜâîûÂÎÛ":
            sesli_sayisi += 1
        else:
            sessiz_sayisi += 1
            
        # Palindrom için küçük harfe çevirip biriktir
        # (Türkçe 'I' ve 'i' dönüşümlerine dikkat ederek basit lower kullanımı)
        k_kucuk = k.lower()
        if k_kucuk == 'i':
            sadece_harfler += 'i'
        elif k_kucuk == 'ı':
            sadece_harfler += 'ı'
        else:
            sadece_harfler += k_kucuk
            
    elif '0' <= k <= '9':
        rakam_sayisi += 1
        
    # Kelime Sayma Mantığı (Bayrak - Flag Kullanımı)
    # Eğer karakter boşluk değilse ve kelimenin içinde değilsek, yeni bir kelime başlıyor demektir.
    if k != " ":
        if not kelimede_miyiz:
            kelimede_miyiz = True
            kelime_sayisi += 1
    else:
        kelimede_miyiz = False

# Palindrom Kontrolü
# Sadece harflerin birleştirilmiş hali ile onun tersinin aynı olup olmadığına bakıyoruz
duz_harfler = sadece_harfler
ters_harfler = ""
for i in range(len(sadece_harfler)):
    ters_harfler += sadece_harfler[len(sadece_harfler) - 1 - i]

palindrom_mu = (duz_harfler == ters_harfler) and (len(duz_harfler) > 0)

# --- 4. ÇIKTI ---
print(f"Cümle: {cümle}")
print(f"Harf: {harf_sayisi} Sesli: {sesli_sayisi} Sessiz: {sessiz_sayisi} Rakam: {rakam_sayisi} Kelime: {kelime_sayisi}")
print(f"Ters: {ters_cumle}")
if palindrom_mu:
    print("Palindrom")
else:
    print("Palindrom değil")
#print(f"Rakam: {rakam_sayisi} Kelime: {kelime_sayisi}")