__author__ = 'anton'

import unittest
from src.car import Car
import math


class CarTests(unittest.TestCase):
    def testCanSetupCar(self):
        car = Car(radius=100, alpha=0, speed=0.1)

        self.assertEqual(100, car.radius)
        self.assertEqual(0, car.alpha)
        self.assertEqual(0.1, car.speed)

    def testCanMoveCar(self):
        car = Car(alpha=0, speed=math.pi / 2, speed_limit=10)

        car.move()

        self.assertEqual(math.pi / 2, car.alpha)

    def testCanMoveCarTwice(self):
        car = Car(alpha=0, speed=1)

        car.move()
        car.move()

        self.assertEqual(0 + 1 + 1, car.alpha)

    def testCanGetCarCoordinates(self):
        car = Car(radius=100, alpha=0)

        self.assertEqual(100, car.x)
        self.assertEqual(0, car.y)

    def testCanGetMovedCarCoordinates(self):
        car = Car(radius=100, alpha=0, speed=math.pi / 6)

        car.move()

        self.assertAlmostEqual(100 * math.sqrt(3) / 2, car.x, 5)
        self.assertAlmostEqual(100 * 1 / 2, car.y, 5)

    def testCarHas0LapsByDefault(self):
        car = Car()

        self.assertEqual(0, car.laps)

    def testCarHas1LapsAfterCrossing0(self):
        car = Car(alpha=2 * math.pi - 1, speed=2, speed_limit=2)

        car.move()

        self.assertEqual(1, car.laps)

    def testCarHas2LapsAfterCrossing0Twice(self):
        car = Car(alpha=0.01, speed=math.pi, speed_limit=10)

        car.move()
        car.move()
        car.move()
        car.move()

        self.assertEqual(2, car.laps)

    def testCanGetDistanceToPreviousCar(self):
        car = Car(radius=100, alpha=0)
        anotherCar = Car(radius=100, alpha=math.pi / 2)

        car.previous_car = anotherCar

        self.assertAlmostEqual(100 * math.sqrt(2), car.distance_to_previous_car)

    def testDecelerateWhenDistanceToPreviousCarIsSmall(self):
        car = Car(radius=100, alpha=0, speed=0.1)
        anotherCar = Car(radius=100, alpha=0.5, speed=0.1)
        car.previous_car = anotherCar

        car.move()

        self.assertAlmostEqual(0.08, car.speed)

    def testContinueDecelerateWhenDistanceToPreviousCarIsSmall(self):
        car = Car(radius=100, alpha=0, speed=0.1)
        anotherCar = Car(radius=100, alpha=0.5, speed=0.1)
        car.previous_car = anotherCar

        car.move()
        anotherCar.move()
        car.move()
        anotherCar.move()

        self.assertAlmostEqual(0.06, car.speed)

    def testAccelerateWhenDistanceToPreviousCarIsBig(self):
        car = Car(radius=100, alpha=0, speed=1, speed_limit=2)
        anotherCar = Car(radius=100, alpha=math.pi, speed=1)
        car.previous_car = anotherCar

        car.move()

        self.assertAlmostEqual(1.2, car.speed)

    def testCarHasNumber(self):
        car = Car(number=1)

        self.assertEqual(1, car.number)

    def testStopWhenCrash(self):
        car = Car(radius=100, alpha=0, speed=1)
        anotherCar = Car(radius=100, alpha=0.01, speed=1)
        car.previous_car = anotherCar

        car.move()

        self.assertAlmostEqual(0, car.speed)

    def testCarHasColor(self):
        car = Car(color=(0.1, 1, 1))

        self.assertEqual("#ff9900", car.color)

