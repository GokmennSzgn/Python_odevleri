# Açıklama: Görev 5 - Hedefi Vur Oyunu


import math
import random
import tkinter as tk
from tkinter import messagebox


class HedefOyunu:
    
    def __init__(self, genislik=420, yukseklik=260, yaricap=20, sure=30):
        
        self.genislik = genislik
        self.yukseklik = yukseklik
        self.r = yaricap
        self.puan = 0
        self.kalan_sure = sure
        self.x = genislik // 2
        self.y = yukseklik // 2
        self.hedef_tasi()

    def hedef_tasi(self):
        
        self.x = random.randint(self.r + 5, self.genislik - self.r - 5)
        self.y = random.randint(self.r + 5, self.yukseklik - self.r - 5)

    def isabet_mi(self, x, y):
        
        return math.hypot(x - self.x, y - self.y) <= self.r

    def isabet_isle(self):
        
        self.puan += 1
        self.hedef_tasi()

    def saniye_azalt(self):
        
        if self.kalan_sure > 0:
            self.kalan_sure -= 1
        return self.kalan_sure > 0


class HedefiVurPenceresi:
    
    def __init__(self):
        self.p = tk.Tk()
        self.p.title("Hedefi Vur")
        self.oyun = HedefOyunu()
        self.zamanlayici_id = None

        self.durum_label = tk.Label(self.p, text="", font=("TkDefaultFont", 11, "bold"))
        self.durum_label.grid(row=0, column=0, padx=8, pady=(8, 4))

        self.tuval = tk.Canvas(
            self.p,
            width=self.oyun.genislik,
            height=self.oyun.yukseklik,
            bg="white",
        )
        self.tuval.grid(row=1, column=0, padx=8, pady=(0, 8))

        self.tuval.bind("<Button-1>", self.tikla)
        self.ekrani_guncelle()
        self.zamanlayici_id = self.p.after(1000, self.zamanlayici_adimi)

    def ekrani_guncelle(self):
        
        self.durum_label.config(text=f"Puan: {self.oyun.puan}  Süre: {self.oyun.kalan_sure} sn")
        self.tuval.delete("all")
        self.tuval.create_oval(
            self.oyun.x - self.oyun.r,
            self.oyun.y - self.oyun.r,
            self.oyun.x + self.oyun.r,
            self.oyun.y + self.oyun.r,
            fill="orange",
            outline="black",
            width=2,
        )

    def tikla(self, olay):
        if self.oyun.kalan_sure <= 0:
            return
        if self.oyun.isabet_mi(olay.x, olay.y):
            self.oyun.isabet_isle()
            self.ekrani_guncelle()

    def zamanlayici_adimi(self):
        
        devam = self.oyun.saniye_azalt()
        if devam:
            self.oyun.hedef_tasi()
            self.ekrani_guncelle()
            self.zamanlayici_id = self.p.after(1000, self.zamanlayici_adimi)
        else:
            self.ekrani_guncelle()
            if self.zamanlayici_id is not None:
                self.p.after_cancel(self.zamanlayici_id)
                self.zamanlayici_id = None
            messagebox.showinfo("Oyun Bitti", f"Süre doldu!\nToplam Puanınız: {self.oyun.puan}")

    def baslat(self):
        self.p.mainloop()


if __name__ == "__main__":
    HedefiVurPenceresi().baslat()