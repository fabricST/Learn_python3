# # Пишем функцию, которая попросит ввести число. Пока он не введёт правильно, просите его ввести.
# Функция возвращает введённое число.
# def number():
#  while True:
#      b = input("Enter 0nly the number 3: ")
#      if b == "3":
#        print("correct")
#        return b
#        break
#      else:
#          b
# number()

# Пишем функцию, которая попросит пользователя ввести слово (строка без пробелов в середине,
# а вначале и в конце пробелы могут быть
def word():
 while True:
    words = input("Enter words: ") .strip()
    if ' ' not in words:
        print(words)
        return words
        break
word()

# # # Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
# def is_year_leap(a):
#  if (a % 4 == 0) and (a % 100 != 0) or (a % 400 == 0):
#     return True
#  else:
#     print("False")
#     return False
#
# is_year_leap(2024)

# # Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами.
# # Если треугольник существует, вернёт True, иначе False.
# def triangle (a, b, c):
#  if (c >= (a + b)) or (b >= (a + c)) or (a >= (b + c)):
#      return True
#  else:
#      return False
# triangle(2, 4, 8)

# Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами и если
# существует, то возвращает тип треугольника Equilateral triangle (равносторонний), Isosceles triangle (равнобедренный),
# Versatile triangle (разносторонний) или не треугольник (Not a triangle).

#
# def correct (a,b,c):
#     if a == b == c:
#         print("Equilateral triangle")
#         return "Equilateral triangle"
#     elif a == b or a == c or b == c:
#         print("Isosceles triangle")
#         return "Isosceles triangle"
#     elif (c**2 > a**2 + b**2) or (a**2 > b**2 + c**2) or (b**2 > a**2 + c**2):
#       print("Versatile triangle")
#     else:
#         print("Impoisible triangle")
# correct()










