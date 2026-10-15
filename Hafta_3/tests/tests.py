
def test_yakit_ekle(miktar, depo=[]):
 depo.append(miktar)
 return depo

print(test_yakit_ekle(10))
print(test_yakit_ekle(20))
