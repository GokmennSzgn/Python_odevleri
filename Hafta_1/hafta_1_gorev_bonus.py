import turtle as t

# Ekran ve hız ayarları
t.speed(3)
t.pensize(4) # Halkaların daha belirgin olması için çizgi kalınlığı

# 1. Mavi Halka
t.penup()
t.goto(-110, 20)
t.pendown()
t.color("blue")
t.circle(50)
t.end_fill()

# 2. Sarı Halka
t.penup()
t.goto(-55, -30)
t.pendown()
t.color("yellow")
t.circle(50)
t.end_fill()

# 3. Siyah Halka
t.penup()
t.goto(0, 20)
t.pendown()
t.color("black")
t.circle(50)
t.end_fill()

# 4. Yeşil Halka
t.penup()
t.goto(55, -30)
t.pendown()
t.color("green")
t.circle(50)
t.end_fill()

# 5. Kırmızı Halka
t.penup()
t.goto(110, 20)
t.pendown()
t.color("red")
t.circle(50)
t.end_fill()

# Kapatılış
t.hideturtle()
t.done()