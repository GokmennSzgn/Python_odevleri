

tc = input("T.C. kimlik no: ")

# 11 karakter mi, hepsi rakam mı ve ilk hane '0' değil mi?
if len(tc) != 11 or not tc.isdigit() or tc[0] == '0':
    print("GEÇERSİZ")
else:
    
    T = 0
    C = 0
    
    # İlk 9 haneyi döngü ile geziyoruz (index 0'dan 8'e kadar)
    for i in range(9):
        rakam = int(tc[i])
        # i sıfır tabanlı olduğu için:
        # i = 0, 2, 4, 6, 8 -> 1., 3., 5., 7., 9. haneler (Tekler - T)
        # i = 1, 3, 5, 7    -> 2., 4., 6., 8. haneler (Çiftler - Ç)
        if i % 2 == 0:
            T += rakam
        else:
            C += rakam
            
    # Kontrol hanelerinin hesaplanması
    h10 = (7 * T - C) % 10
    h11 = (T + C + h10) % 10
    
    # Numara içindeki gerçek 10. ve 11. haneler (index 9 ve 10)
    gercek_h10 = int(tc[9])
    gercek_h11 = int(tc[10])
    
    
    # Örnek çıktı biçimine uyarak sonuçları yazdırıyoruz
    if h10 == gercek_h10 and h11 == gercek_h11:
        print(f"Tek: {T} Çift: {C} 10. hane: {gercek_h10} 11. hane: {gercek_h11} → GEÇERLİ")
    else:
        print("GEÇERSİZ")