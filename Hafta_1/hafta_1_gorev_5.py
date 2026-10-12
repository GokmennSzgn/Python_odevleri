import turtle as t

# Ev çizimi:
t.color("black", "lightblue")
t.begin_fill()

for _ in range(4):
    t.forward(100)
    t.left(90)

t.end_fill()

# Çatı çizimi:
t.left(90)
t.forward(100)
t.right(90)

t.color("black", "red")
t.begin_fill()

t.left(60)
t.forward(100)
t.right(120)
t.forward(100)

t.end_fill()

t.penup()
t.goto(150, 50)
t.pendown()

t.color("darkblue")
t.write("Gökmennin Evi", font=("Arial", 16, "bold"))

t.hideturtle()
t.done()

