saniye = int(input("Lütfen saniye cinsinden bir süre giriniz: "))

gun = saniye // 86400
kalan_saniye = saniye % 86400

saat = kalan_saniye // 3600
kalan_saniye = kalan_saniye % 3600

dakika = kalan_saniye // 60
saniye -= kalan_saniye % 60

print(f"{saniye} saniye, {gun} gün, {saat} saat, {dakika} dakika ve {kalan_saniye % 60} saniyeye eşittir.")

