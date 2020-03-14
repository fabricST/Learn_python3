# Создайте наборы тестов на написанные функции из прошлого домашнего задания:
# 	•	Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный,
# и False иначе.

import unittest
from Learn_python3.Home_Work_3.H_W3_P6 import is_year_leap, triangle, correct


class TestYearTriagle(unittest.TestCase):

    def test_year(self):
        a = is_year_leap(2020)
        self.assertTrue(a)

# Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами.
# Если треугольник существует, вернёт True, иначе False.

    def test_triangle(self):
        b = triangle(2, 9, 5)
        self.assertTrue(b)

# Функция принимает три числа a, b, c.Функция должна определить, существует ли треугольник с такими сторонами и
# если существует, то возвращает тип треугольника Equilateral triangle(равносторонний),
# Isosceles triangle(равнобедренный), Versatile triangle(разносторонний) или не треугольник(Not a triangle).

    def test_correct_equilateral(self):
        a = correct(3, 3, 3)
        self.assertEqual(a, "Equilateral triangle")

    def test_correct_Versatile(self):
        b = correct(3, 4, 7)
        self.assertEqual(b, "Versatile triangle")

    def test_correct_Isosceles(self):
        c = correct(3, 3, 8)
        self.assertEqual(c, "Isosceles triangle")


if __name__ == '__main__':
    unittest.main()

