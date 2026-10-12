def pi_hesaplama(terim_sayısı):
    toplam = 0
    payda = 1
    isaret = 1

    for i in range(terim_sayısı):
        toplam += isaret * (4 / payda)
        payda += 2
        isaret *= -1
    return toplam

print("6 terimli pi değeri:", pi_hesaplama(6))
print("7 terimli pi değeri:", pi_hesaplama(7))
