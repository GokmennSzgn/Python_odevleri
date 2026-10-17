from itertools import islice


def test_yakit_ekle(miktar, depo=[]):
 depo.append(miktar)
 return depo

print(test_yakit_ekle(10))
print(test_yakit_ekle(20))



def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b 

g = fibonacci()

birinci_dilim = list(islice(g, 5))
print("Birinci islice çağrısı:", birinci_dilim)

ikinci_dilim = list(islice(g, 5))
print("İkinci islice çağrısı:", ikinci_dilim)



