# Açıklama: Görev 1 - Sıcaklık Dönüştürücü

import tkinter as tk
from tkinter import messagebox


class SicaklikModel:
    

    def c_to_f(self, c):
        
        return c * 9 / 5 + 32

    def f_to_c(self, f):
        
        return (f - 32) * 5 / 9


class SicaklikPenceresi:
    
    def __init__(self, model):
        
        self.model = model
        self.p = tk.Tk()
        self.p.title("Sıcaklık")

        self.giris = tk.Entry(self.p, width=16)
        self.giris.grid(row=0, column=0, columnspan=2, padx=8, pady=8)

        tk.Button(self.p, text="°C → °F", command=self.cevir_f).grid(row=1, column=0, padx=4, pady=4)
        tk.Button(self.p, text="°F → °C", command=self.cevir_c).grid(row=1, column=1, padx=4, pady=4)

        self.sonuc = tk.Label(self.p, text="", fg="blue")
        self.sonuc.grid(row=2, column=0, columnspan=2, padx=8, pady=8)

    def _oku(self):
        
        try:
            return float(self.giris.get().strip().replace(",", "."))
        except ValueError:
            messagebox.showerror("Hata", "Geçerli bir sayı girin.")
            return None

    def cevir_f(self):
        
        c = self._oku()
        if c is not None:
            f = self.model.c_to_f(c)
            self.sonuc.config(text=f"{c:.2f} °C = {f:.2f} °F")

    def cevir_c(self):
        
        f = self._oku()
        if f is not None:
            c = self.model.f_to_c(f)
            self.sonuc.config(text=f"{f:.2f} °F = {c:.2f} °C")

    def baslat(self):
        
        self.p.mainloop()


if __name__ == "__main__":
    SicaklikPenceresi(SicaklikModel()).baslat()
