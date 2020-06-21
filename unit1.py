import turtle


def c_key():
    turtle.clear()
    turtle.home()


def f_key():
    turtle.fd(100)


window = turtle.Screen()
window.title("hello turtle")
turtle.shape("turtle")
turtle.bgcolor('lightgreen')  # Цвет фона экрана

turtle.onkeypress(c_key, "c")
turtle.onkeypress(f_key, "f")

turtle.speed(1)  # Скорость ползания черепахи по экрану можно регулировать 1 очень медлено, 10 очень быстро
print("В начале работы черепаха находится:", turtle.position())
turtle.fd(100)
print("fd это то же самое что forward только короче, двигает черепашку вперед. Сейчас ее координаты:", turtle.position())
turtle.pensize(10)  # Размер пера черепахи
turtle.rt(45)
print("rt это то же самое что right только короче, поворачивает черепашку вправо на определнный угол. Но черепашка просто поворачивается, но не двигается."
      " Сейчас ее координаты:", turtle.position())
turtle.bk(100)
turtle.pensize(1)  # Вернем размер пера в обычное состоние
print("bk это то же самое что backward или back только короче, двигает черепашку назад. Сейчас ее координаты:", turtle.position())
turtle.pencolor("blue")
turtle.lt(45)
print("lt это то же самое что left только короче, поворачивает черепашку влево на определнный угол. Но черепашка просто поворачивается, но не двигается."
      " Сейчас ее координаты:", turtle.position())
turtle.fd(100)
print("И опять черепашка едет вперед, ее координаты:", turtle.position())
turtle.goto(300, 300)
print("Черепашку можно просто перемещать на координаты (x,y). Сейчас ее координаты:", turtle.position())
turtle.setx(200)
print("Черепашку можно перемещать только по оси Х. Сейчас ее координаты:", turtle.position())
turtle.sety(200)
print("Черепашку можно перемещать только по оси Y. Сейчас ее координаты:", turtle.position())
turtle.color("black", "red")  # Установить цвет заливки
turtle.begin_fill()  # Начало заливки
turtle.circle(80)
print("Рисуем оружность некоторого размера из центра. Обрати внимание координаты черепахи не изменились:", turtle.position())
turtle.end_fill()  # Конец заливки
turtle.home()
print("Черепашку можно возвратить в цент экрана ( домой ). Сейчас ее координаты:", turtle.position())
turtle.write("Могу еще писать на экране")

window.listen()   # Смотрим за событиями, напрмер какие клавиши нажаты
window.mainloop()  # Постоянный цикл обработки событий
