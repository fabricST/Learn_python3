# Создать классы
# 1) Прямоугольная площадка (пример: комната) (свойства: две стороны).
# Методы:
# 	•	вычисляем площадь,
# 	•	вычисляем периметр.


class Room:

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def square(self, a, b):
        self.a = a * b
        return self.a

    def perimetr(self, a, b):
        self.a = (a + b) * 2
        return self.a


s = Room()
print(s.square(3, 4))
print(s.perimetr(3, 4))

# 2) Точка на карте (свойства: X, Y).
# Методы:
# 	•	Нужно вычислить расстояние до начала координат,
# 	•	* вычисляется расстояние между точкой и другой точкой экземпляром этого же класса
# 	•	**  перевод в другие системы координат

# Пока не понимаю как решить задание

# 3) Студент (свойства: имя-фамилия, специальность, год начала обучения, список оценок – при создании объекта,
# по умолчанию, пустой список).
# Методы:
# 	•	Добавить новую оценку в свойство списка оценок
# 	•	Посчитать средний балл,
# 	•	Посчитать сколько лет учится уже студент.


class Student:

    def __init__(self, full_name, specialty, start_studies):
        self.full_name = full_name
        self.specialty = specialty
        self.start_studies = start_studies
        self.points = []

    def add_new_point(self, *x):
        for i in x:
            self.points.append(i)
        return self.points

    def grade_avarege(self):
        try:
            mean = sum(self.points) / len(self.points)
            return mean
        except ZeroDivisionError:
            return f'Grades list is empty. Please, add grades'

    def time(self, current=2020):
        number = current - self.start_studies
        return number

    def __str__(self):
        return f'Student: full name - {self.full_name}, specialty - {self.specialty}, ' \
               f'start_studies - {self.start_studies}'


new = Student("Vasya Pypkin", "Qa", 1930)
print(new.add_new_point(5, 3, 4, 5))
print(new.grade_avarege())
print(new.time())
