import turtle
import random
import time

# Funktion zum Zeichnen eines Herzens an einer Position
def draw_heart_at(x, y, size=1.0, color="red"):
    heart = turtle.Turtle()
    heart.speed(0)
    heart.color(color)
    heart.penup()
    heart.goto(x, y)
    heart.pendown()
    heart.begin_fill()

    heart.left(50)
    heart.forward(133 * size)
    heart.circle(50 * size, 200)
    heart.right(140)
    heart.circle(50 * size, 200)
    heart.forward(133 * size)

    heart.end_fill()
    heart.hideturtle()

# Funktion zum Schreiben
def write_text(x, y, text, size=20):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.hideturtle()
    t.goto(x, y)
    t.write(text, align="center", font=("Arial", size, "bold"))

# Feste Herzen
draw_heart_at(-200, 0, size=1.0)
write_text(-200, 120, "Ich liebe dich", 20)

draw_heart_at(150, 0, size=1.0)
write_text(150, 120, "für immer", 20)

# 1 Sekunde warten, bevor die unendliche Schleife startet
time.sleep(1)

# Unendlich viele Herzen danach
while True:
    x = random.randint(-300, 300)
    y = random.randint(-250, 250)
    size = random.uniform(0.3, 0.7)  # kleine zufällige Herzgröße

    draw_heart_at(x, y, size=size, color="pink")
    write_text(x, y + size * 120, "und immer", size=int(12 * size))

    time.sleep(0.3)  # kleine Pause, damit es schön nacheinander kommt

turtle.done()
