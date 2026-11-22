
import math

class Kesir:
    """Sadeleştirilmiş rasyonel sayıyı (pay/payda) temsil eden sınıf."""

    def __init__(self, pay, payda=1):
        """Pay ve paydayı alıp işaretini düzenler ve en sade haline getirir."""
        if payda == 0:
            raise ZeroDivisionError("Payda sıfır olamaz.")

        if payda < 0:
            pay = -pay
            payda = -payda

        ortak = math.gcd(abs(pay), abs(payda))
        self.pay = pay // ortak
        self.payda = payda // ortak

    def __str__(self):
        """Kesri okunabilir metin ('pay/payda' veya payda 1 ise 'pay') olarak döndürür."""
        if self.payda == 1:
            return str(self.pay)
        return f"{self.pay}/{self.payda}"

    def __float__(self):
        """Kesrin ondalıklı sayı karşılığını döndürür."""
        return self.pay / self.payda

    def __add__(self, diger):
        """İki kesri toplayıp yeni ve sade bir Kesir nesnesi döndürür."""
        if not isinstance(diger, Kesir):
            return NotImplemented
        yeni_pay = self.pay * diger.payda + diger.pay * self.payda
        yeni_payda = self.payda * diger.payda
        return Kesir(yeni_pay, yeni_payda)

    def __sub__(self, diger):
        """İki kesrin farkını alıp yeni ve sade bir Kesir nesnesi döndürür."""
        if not isinstance(diger, Kesir):
            return NotImplemented
        yeni_pay = self.pay * diger.payda - diger.pay * self.payda
        yeni_payda = self.payda * diger.payda
        return Kesir(yeni_pay, yeni_payda)

    def __mul__(self, diger):
        """İki kesri çarpıp yeni ve sade bir Kesir nesnesi döndürür."""
        if not isinstance(diger, Kesir):
            return NotImplemented
        return Kesir(self.pay * diger.pay, self.payda * diger.payda)

    def __truediv__(self, diger):
        """İki kesri bölüp yeni ve sade bir Kesir nesnesi döndürür."""
        if not isinstance(diger, Kesir):
            return NotImplemented
        if diger.pay == 0:
            raise ZeroDivisionError("Sıfıra bölme yapılamaz.")
        return Kesir(self.pay * diger.payda, self.payda * diger.pay)

    def __eq__(self, diger):
        """İki kesrin eşitliğini çapraz çarpımla sınar."""
        if not isinstance(diger, Kesir):
            return NotImplemented
        return self.pay * diger.payda == diger.pay * self.payda

    def __lt__(self, diger):
        """Mevcut kesrin diğerinden küçük olup olmadığını çapraz çarpımla sınar."""
        if not isinstance(diger, Kesir):
            return NotImplemented
        return self.pay * diger.payda < diger.pay * self.payda

    def __le__(self, diger):
        """Mevcut kesrin diğerinden küçük veya eşit olup olmadığını çapraz çarpımla sınar."""
        if not isinstance(diger, Kesir):
            return NotImplemented
        return self.pay * diger.payda <= diger.pay * self.payda


if __name__ == "__main__":
    print(Kesir(6, 8) == Kesir(3, 4))
    print(Kesir(3, 4) / Kesir(3, 8))

    # (a) n=2..10 çarpımı: prod (1 - 1/n) = 1/10
    carpim = Kesir(1, 1)
    for n in range(2, 11):
        terim = Kesir(1, 1) - Kesir(1, n)
        carpim = carpim * terim
    print(f"Çarpım: {carpim}")

    # (b) Yalnızca '<' kullanarak en büyük kesri bulma (liste kullanmadan)
    k1 = Kesir(3, 7)
    k2 = Kesir(5, 12)
    k3 = Kesir(2, 5)
    k4 = Kesir(4, 9)
    k5 = Kesir(3, 8)

    en_buyuk = k1
    if en_buyuk < k2:
        en_buyuk = k2
    if en_buyuk < k3:
        en_buyuk = k3
    if en_buyuk < k4:
        en_buyuk = k4
    if en_buyuk < k5:
        en_buyuk = k5

    print(f"En büyük: {en_buyuk}")