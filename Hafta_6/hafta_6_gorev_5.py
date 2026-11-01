
gizli_kelime = "KOŞUL"
tahminler = ""
hata_sayisi = 0
maks_hata = 6

while hata_sayisi < maks_hata:
    # 1. Her turda kelimenin o anki durumunu ve hata sayısını göster
    gosterim = ""
    tamamlandi_mi = True
    
    # Kelimedeki harfleri sırayla kontrol ediyoruz (liste kullanmadan string üzerinde)
    for i in range(len(gizli_kelime)):
        harf = gizli_kelime[i]
        bulundu = False
        
        # Daha önce tahmin edilen harfler arasında var mı?
        for j in range(len(tahminler)):
            if tahminler[j] == harf:
                bulundu = True
                break
                
        if bulundu:
            gosterim += harf + " "
        else:
            gosterim += "_ "
            tamamlandi_mi = False
            
    print(f"\n{gosterim.strip()} (hata: {hata_sayisi}/{maks_hata})")
    
    # Kelime tamamen bilindiyse döngüden çık
    if tamamlandi_mi:
        print("Kazandınız!")
        break
        
    # 2. Kullanıcıdan harf alma
    giris = input("Harf: ").strip()
    
    # Tek harf kontrolü
    if len(giris) != 1:
        print("Lütfen yalnızca tek bir harf giriniz.")
        continue
        
    # Türkçe büyük harf duyarlılığı (İpucu: "i".upper() sorununu çözmek için)
    if giris == 'i':
        harf_buyuk = 'İ'
    elif giris == 'ı':
        harf_buyuk = 'I'
    else:
        harf_buyuk = giris.upper()
        
    # 3. Daha önce denenmiş harf kontrolü
    daha_once_denendi = False
    for i in range(len(tahminler)):
        if tahminler[i] == harf_buyuk:
            daha_once_denendi = True
            break
            
    if daha_once_denendi:
        print("Bu harfi zaten denediniz.")
        continue
        
    # Tahmin edilen harfi biriktiriyoruz
    tahminler += harf_buyuk
    
    # 4. Harf kelimede var mı?
    var_mi = False
    for i in range(len(gizli_kelime)):
        if gizli_kelime[i] == harf_buyuk:
            var_mi = True
            break
            
    if not var_mi:
        hata_sayisi += 1

else:
    # 6 hata dolduğunda (while döngüsü break ile kırılmadığında) çalışır
    print(f"\nKaybettiniz! Gizli kelime: {gizli_kelime}")