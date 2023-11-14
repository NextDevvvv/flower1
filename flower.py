import turtle
import math

def draw_flower():
    # Inisialisasi turtle
    flower = turtle.Turtle()
    flower.speed(2)

    # Fungsi untuk menggambar kelopak bunga
    def draw_petals():
        for _ in range(36):
            flower.forward(100)
            flower.right(45)
            flower.forward(100)
            flower.right(135)
            flower.forward(100)
            flower.right(45)
            flower.forward(100)
            flower.right(135)
            flower.right(10)

    # Pergi ke posisi awal
    flower.penup()
    flower.goto(0, -150)
    flower.pendown()

    # Menggambar kelopak bunga
    flower.fillcolor("red")
    flower.begin_fill()
    draw_petals()
    flower.end_fill()

    # Menggambar pusat bunga
    flower.penup()
    flower.goto(0, -150)
    flower.pendown()
    flower.fillcolor("yellow")
    flower.begin_fill()
    flower.circle(20)
    flower.end_fill()

    # Menutup jendela saat diklik
    turtle.exitonclick()

# Panggil fungsi untuk menggambar bunga
draw_flower()
