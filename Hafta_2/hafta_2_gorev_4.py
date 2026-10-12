sayı = 932
son_rakam = sayı % 10
kalan_sayı = sayı // 10
toplam = son_rakam + (kalan_sayı % 10) + (kalan_sayı // 10)
print(f"{sayı} sayısının rakamları toplamı: {toplam}")