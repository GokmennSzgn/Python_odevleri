# Ad Soyad: [Adınız Soyadınız]
# Numara: [Öğrenci Numaranız]
# Tarih: 2026-11-28
# Açıklama: Bonus - Kesir Hesap Makinesi

from pathlib import Path
import sys
import tkinter as tk
from tkinter import messagebox

sys.path.append(str(Path(__file__).resolve().parent.parent))
from Hafta_8.hafta_8_gorev_4 import Kesir


class KesirHesapMakinesi:

    def __init__(self):
        """Pencere ve bileşenleri oluşturur."""
        self.p = tk.Tk()
        self.p.title("Kesir Hesap Makinesi")

        tk.Label(self.p, text="1. Kesir").grid(row=0, column=0, padx=6, pady=6)
        self.p1 = tk.Entry(self.p, width=6)
        self.p1.grid(row=0, column=1, padx=2, pady=6)
        tk.Label(self.p, text="/").grid(row=0, column=2)
        self.d1 = tk.Entry(self.p, width=6)
        self.d1.grid(row=0, column=3, padx=2, pady=6)

        tk.Label(self.p, text="2. Kesir").grid(row=1, column=0, padx=6, pady=6)
        self.p2 = tk.Entry(self.p, width=6)
        self.p2.grid(row=1, column=1, padx=2, pady=6)
        tk.Label(self.p, text="/").grid(row=1, column=2)
        self.d2 = tk.Entry(self.p, width=6)
        self.d2.grid(row=1, column=3, padx=2, pady=6)

        tk.Button(self.p, text="+", width=4, command=lambda: self.hesapla("+")).grid(row=2, column=0, padx=3, pady=6)
        tk.Button(self.p, text="-", width=4, command=lambda: self.hesapla("-")).grid(row=2, column=1, padx=3, pady=6)
        tk.Button(self.p, text="*", width=4, command=lambda: self.hesapla("*")).grid(row=2, column=2, padx=3, pady=6)
        tk.Button(self.p, text="/", width=4, command=lambda: self.hesapla("/")).grid(row=2, column=3, padx=3, pady=6)

        self.sonuc = tk.Label(self.p, text="Sonuç: -", fg="blue")
        self.sonuc.grid(row=3, column=0, columnspan=4, padx=6, pady=8)

    def _kesir_al(self, pay_kutu, payda_kutu):
        return Kesir(int(pay_kutu.get().strip()), int(payda_kutu.get().strip()))

    def hesapla(self, islem):
        try:
            k1 = self._kesir_al(self.p1, self.d1)
            k2 = self._kesir_al(self.p2, self.d2)

            if islem == "+":
                cikti = k1.__toplama__(k2)
            elif islem == "-":
                cikti = k1.__çıkarma__(k2)
            elif islem == "*":
                cikti = k1.__çarpma__(k2)
            else:
                cikti = k1.__bölme__(k2)

            self.sonuc.config(text=f"Sonuç: {cikti}")
        except ValueError:
            messagebox.showerror("Hata", "Tüm kutulara tam sayı girin.")
        except ZeroDivisionError as hata:
            messagebox.showerror("Hata", str(hata))

    def baslat(self):
        self.p.mainloop()


if __name__ == "__main__":
    KesirHesapMakinesi().baslat()