#!/usr/bin/python3
# coding: utf-8

from tkinter import *
from enum import Enum
import time
import random


class element_square: # Рисую квадратик со стороной d и центром x,y
    def __init__(self, self_glob, x, y, d, color):
        self.self_glob = self_glob
        self.x = x
        self.y = y
        self.d = d
        self.color = color
        if (self.d % 2) == 0:
            self.d +=1 # сторону квадрата делаю нечётной

    def draw(self):
        x = self.x - (self.d // 2) # координата левой грани квадрата
        y = self.y - (self.d // 2) # координата верхней грани квадрата
        return self.self_glob.canv.create_rectangle(x, y, x + self.d, y + self.d, fill=self.color, width=2)


class snake_body: # Двигать тело змеюки в текущую сторону на 1 шаг
# При этом тело может увеличиться (add='add') в размерах или нет
    canv = 0
    def __init__(self, window, canv_x, canv_y, canv_width, canv_height):
        self.window = window
        self.canv_x = canv_x
        self.canv_y = canv_y
        self.canv_width = canv_width
        self.canv_height = canv_height
        self.vector = self.CONST.RIGHT.value
        self.canv = Canvas(self.window, width=self.canv_width,
                                height=self.canv_height,
                                bg=self.CONST.CANVAS_BGCOLOR.value)
        self.canv.place(x=self.canv_x, y=self.canv_y)

        self.head = element_square(self, self.CONST.SNAKE_X.value,
                             self.CONST.SNAKE_Y.value,
                             self.CONST.SNAKE_THICKNESS.value,
                             self.CONST.SNAKE_HCOLOR.value)
        self.body = []
        self.body.append({'id': self.head.draw(),
                        'x': self.CONST.SNAKE_X.value,
                        'y': self.CONST.SNAKE_Y.value})
        self.step('add')
        self.step('add')
        self.step('add')
        self.step('add')

        self.window.bind('<d>',self.right)
        self.window.bind('<D>',self.right)
        self.window.bind('<Right>',self.right)
        self.window.bind('<s>',self.down)
        self.window.bind('<S>',self.down)
        self.window.bind('<Down>',self.down)
        self.window.bind('<a>',self.left)
        self.window.bind('<A>',self.left)
        self.window.bind('<Left>',self.left)
        self.window.bind('<w>',self.up)
        self.window.bind('<W>',self.up)
        self.window.bind('<Up>',self.up)

        self.window.bind('<q>',self.quit)
        self.window.bind('<e>',self.move)
        self.window.bind('<Destroy>',self.quit)

    class CONST(Enum): # Список возможных направлений движения и других констант
        RIGHT = 1
        DOWN = 2
        LEFT = 3
        UP = 4
        SNAKE_X = 370 # Координата старта змеи
        SNAKE_Y = 235 # Координата старта змеи
        SNAKE_HCOLOR = 'red' # Цвет головы змейки
        SNAKE_BCOLOR = 'green' # Цвет тела змейки
        CANVAS_BGCOLOR = '#bfcff1' # Цвет фона холста
        SNAKE_THICKNESS = 10 # Толщина тела змейки

    # обработчики клавиш изменения направления движения:
    def right(self, event):
        self.vector = self.CONST.RIGHT.value
    def down(self, event):
        self.vector = self.CONST.DOWN.value
    def left(self, event):
        self.vector = self.CONST.LEFT.value
    def up(self, event):
        self.vector = self.CONST.UP.value

    def quit(self, event): # Возможность остановить змейку (пауза)
        self.quit = 'y'

    def move(self, event):
        if self.quit != 'n':
            self.start()

    def start(self): # бесконечный цикл движения змейки
        self.quit = 'n'
        i = 0
        while i == 0:
            self.step('del')
            for x in range(0,20):
                time.sleep(0.05)
                self.window.update()
                if self.quit == 'y':
                    i = 1
                    break

    def step(self, add): # Двигать тело змеюки в текущую сторону на 1 шаг
        # При этом тело может увеличиться (add='add') в размерах или нет
        if self.vector == self.CONST.RIGHT.value:
            deltax = self.CONST.SNAKE_THICKNESS.value
            deltay = 0
        elif self.vector == self.CONST.DOWN.value:
            deltax = 0
            deltay = self.CONST.SNAKE_THICKNESS.value
        elif self.vector == self.CONST.LEFT.value:
            deltax = -self.CONST.SNAKE_THICKNESS.value
            deltay = 0
        elif self.vector == self.CONST.UP.value:
            deltax = 0
            deltay = -self.CONST.SNAKE_THICKNESS.value
        self.head.x += deltax
        self.head.y += deltay
        self.head = element_square(self, self.head.x, self.head.y,
                             self.CONST.SNAKE_THICKNESS.value,
                             self.CONST.SNAKE_HCOLOR.value)
        self.body.append({'id': self.head.draw(), 'x': self.head.x, 'y': self.head.y}) # Создал новую голову
        self.canv.itemconfig(self.body[-2]['id'],
                             fill=self.CONST.SNAKE_BCOLOR.value) # Перекрасил старую голову в тело
        if add != 'add':
            self.canv.delete(self.body[0]['id'])
            self.body.pop(0)





def main():
    root = Tk()
    root.title('Программа Змейка на питоне в графике')
    root.geometry('800x600+150+150')

    snake = snake_body(root, 30, 40, 740, 470)
    snake.start()



    root.mainloop()



if __name__ == '__main__':
    main()


