gun = int(input("Gün:"))
saat = int(input("Saat:"))
dakika = int(input("Dakika:"))
saniye = int(input("Saniye:"))

toplam_dakika = dakika * 60
toplam_saat = saat * 3600
toplam_gun = gun * 86400

toplam_saniye = saniye + toplam_dakika + toplam_saat + toplam_gun
print("Toplam saniye: ", toplam_saniye)
