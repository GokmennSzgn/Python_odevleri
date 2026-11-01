
temel_no = "453914880343646"
bulunan_hane = -1

# 0'dan 9'a kadar olan rakamları sırayla deneyelim
for hane in range(10):
    # Aday numarayı oluşturuyoruz (15 hanenin sonuna hane ekleniyor)
    aday = temel_no + str(hane)
    toplam = 0
    uzunluk = len(aday)
    
    # Luhn algoritması: Sağdan sola doğru haneleri işleme
    for i in range(uzunluk - 1, -1, -1):
        rakam = int(aday[i])
        
        # Sağdan sayıldığında çift pozisyonda olanları (sağdan 2., 4., 6...) 2 ile çarpıyoruz
        # (uzunluk - i) ifadesi karakterin sağdan kaçıncı sırada olduğunu verir (1 tabanlı)
        if (uzunluk - i) % 2 == 0:
            rakam *= 2
            # Eğer 2 katı 9'dan büyükse rakamları topla (10-9 kuralı ile aynı hesaptır)
            if rakam > 9:
                rakam -= 9
                
        toplam += rakam
        
    # Eğer toplam 10'a tam bölünüyorsa bulduk demektir
    if toplam % 10 == 0:
        bulunan_hane = hane
        break  # İlk geçerli olanda break ile çıkıyoruz

print(f"Kontrol hanesi: {bulunan_hane}")