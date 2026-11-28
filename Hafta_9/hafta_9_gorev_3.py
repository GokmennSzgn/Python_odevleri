# Açıklama: Görev 3 - Vigenère Arayüzü

import tkinter as tk
from tkinter import messagebox

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from Hafta_8.hafta_8_gorev_3 import vigenere

class VigenerePenceresi:
    
    def __init__(self):
        
        self.p = tk.Tk()
        self.p.title("Vigenère")

        tk.Label(self.p, text="Metin").grid(row=0, column=0, padx=8, pady=6, sticky="w")
        self.metin_entry = tk.Entry(self.p, width=24)
        self.metin_entry.grid(row=0, column=1, columnspan=2, padx=8, pady=6)

        tk.Label(self.p, text="Anahtar").grid(row=1, column=0, padx=8, pady=6, sticky="w")
        self.anahtar_entry = tk.Entry(self.p, width=24)
        self.anahtar_entry.grid(row=1, column=1, columnspan=2, padx=8, pady=6)

        self.sifrele_btn = tk.Button(self.p, text="Şifrele", command=self.sifrele)
        self.sifrele_btn.grid(row=2, column=1, padx=4, pady=6, sticky="ew")

        self.coz_btn = tk.Button(self.p, text="Çöz", command=self.coz)
        self.coz_btn.grid(row=2, column=2, padx=4, pady=6, sticky="ew")

        self.sonuc_label = tk.Label(self.p, text="", fg="blue")
        self.sonuc_label.grid(row=3, column=0, columnspan=3, padx=8, pady=8)

        self.p.bind("<Return>", self._enter_ile_sifrele)

    def _anahtar_gecerli_mi(self, anahtar):
        
        if not anahtar or not anahtar.isalpha():
            messagebox.showerror("Hata", "Anahtar boş olamaz ve yalnızca harflerden oluşmalıdır.")
            return False
        return True

    def _calistir_islem(self, yon):
        
        metin = self.metin_entry.get()
        anahtar = self.anahtar_entry.get().strip()

        if not self._anahtar_gecerli_mi(anahtar):
            return

        sonuc = vigenere(metin, anahtar, yon)
        self.sonuc_label.config(text=sonuc)

    def sifrele(self):
        self._calistir_islem(1)

    def coz(self):
        self._calistir_islem(-1)

    def _enter_ile_sifrele(self, olay):
        self.sifrele()

    def baslat(self):
        self.p.mainloop()


if __name__ == "__main__":
    VigenerePenceresi().baslat()