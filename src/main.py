from tkinter import *
import time
import math
from src.car import Car
import random

width = 750
height = 750
isRunning = True
NUMBER_OF_CARS = 15
COLLISION_DISTANCE = 10
average_speed = 0.01
start_time = time.process_time()
max_throughput = 0


def sx(x):
    return x + width // 2


def sy(y):
    return height - (y + height // 2)


def stop(event):
    top.destroy()


top = Tk()
top.geometry('{}x{}'.format(width, height))
top.bind("<Escape>", stop)

w = Canvas(top, width=width, height=height)
w.pack()

cars = []
for i in range(NUMBER_OF_CARS, 0, -1):
    cars.append(
        Car(alpha=i * 0.05, radius=325,
            speed=random.uniform(average_speed - average_speed / 2, average_speed + average_speed / 2),
            speed_limit=average_speed * 3,
            number=NUMBER_OF_CARS - i + 1,
            color=(i / NUMBER_OF_CARS, 0.5, 1)))
for i in range(NUMBER_OF_CARS):
    cars[(i + 1) % NUMBER_OF_CARS].previous_car = cars[i]


def draw_road():
    r = 350
    w.create_oval(sx(-r), sy(-r), sx(r), sy(r), outline='gray')
    r = 300
    w.create_oval(sx(-r), sy(-r), sx(r), sy(r), outline='gray')


def draw_cars(cars):
    car_size = 20
    for car in cars:
        w.create_oval(sx(car.x - car_size // 2), sy(car.y - car_size // 2),
                      sx(car.x + car_size // 2), sy(car.y + car_size // 2),
                      fill=car.color)
        alpha_grad = car.alpha * 360 / (2 * math.pi) + car_size // 2 / 325 * 360 / (2 * math.pi)
        w.create_arc(sx(-325), sy(-325), sx(325), sy(325),
                     start=alpha_grad, extent=car.speed * 750,
                     outline='deep sky blue', style='arc')
        w.create_text(sx(car.x), sy(car.y), text=str(car.number))


def total_laps(cars):
    laps = 0
    for car in cars:
        laps += car.laps
    return laps


def draw_info(cars):
    global max_throughput
    laps = total_laps(cars)
    seconds_passed = time.process_time() - start_time
    throughput = laps / seconds_passed
    if max_throughput < throughput:
        max_throughput = throughput
    w.create_text(10, 610, text="# of cars: {}".format(NUMBER_OF_CARS), anchor='nw')
    w.create_text(10, 630, text="Laps: {}".format(laps), anchor='nw')
    w.create_text(10, 650, text="Time: {:6.1f}s".format(seconds_passed), anchor='nw')
    w.create_text(10, 670, text="Throughput: {:6.2f} laps/s".format(throughput), anchor='nw')
    w.create_text(10, 690, text="Max throughput: {:6.2f} laps/s".format(max_throughput), anchor='nw')


while isRunning:
    w.delete('all')

    for car in cars:
        car.move()

    draw_road()
    draw_cars(cars)
    draw_info(cars)

    w.update()
    w.after(1)

top.mainloop()
