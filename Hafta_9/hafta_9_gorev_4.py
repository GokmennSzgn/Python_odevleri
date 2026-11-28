# Açıklama: Görev 4 - Çizim Tahtası

import tkinter as tk


class CizimTahtasiPenceresi:

    def __init__(self):
        
        self.p = tk.Tk()
        self.p.title("Çizim Tahtası")

        self.renk_var = tk.StringVar(value="black")
        self.kalinlik_var = tk.IntVar(value=3)
        self.onceki_x = None
        self.onceki_y = None
        self.cizgi_sayisi = 0

        ust_panel = tk.Frame(self.p)
        ust_panel.grid(row=0, column=0, padx=8, pady=6, sticky="w")

        tk.Radiobutton(ust_panel, text="Siyah", variable=self.renk_var, value="black").grid(
            row=0, column=0, padx=4
        )
        tk.Radiobutton(ust_panel, text="Kırmızı", variable=self.renk_var, value="red").grid(
            row=0, column=1, padx=4
        )
        tk.Radiobutton(ust_panel, text="Mavi", variable=self.renk_var, value="blue").grid(
            row=0, column=2, padx=4
        )

        tk.Scale(
            ust_panel,
            from_=1,
            to=10,
            orient="horizontal",
            variable=self.kalinlik_var,
        ).grid(row=0, column=3, padx=6)

        tk.Button(ust_panel, text="Temizle", command=self.temizle).grid(row=0, column=4, padx=4)

        self.tuval = tk.Canvas(self.p, width=420, height=220, bg="white")
        self.tuval.grid(row=1, column=0, padx=8, pady=4)

        self.sayac_label = tk.Label(self.p, text="0 çizgi")
        self.sayac_label.grid(row=2, column=0, padx=8, pady=(2, 8))

        self.tuval.bind("<Button-1>", self.basla)
        self.tuval.bind("<B1-Motion>", self.ciz)

    def _sayac_guncelle(self):
        self.sayac_label.config(text=f"{self.cizgi_sayisi} çizgi")

    def basla(self, olay):
        self.onceki_x = olay.x
        self.onceki_y = olay.y

    def ciz(self, olay):
        if self.onceki_x is not None and self.onceki_y is not None:
            self.tuval.create_line(
                self.onceki_x,
                self.onceki_y,
                olay.x,
                olay.y,
                fill=self.renk_var.get(),
                width=self.kalinlik_var.get(),
                capstyle=tk.ROUND,
            )
            self.cizgi_sayisi += 1
            self._sayac_guncelle()

        self.onceki_x = olay.x
        self.onceki_y = olay.y

    def temizle(self):
        self.tuval.delete("all")
        self.onceki_x = None
        self.onceki_y = None
        self.cizgi_sayisi = 0
        self._sayac_guncelle()

    def baslat(self):
        self.p.mainloop()


if __name__ == "__main__":
    CizimTahtasiPenceresi().baslat()