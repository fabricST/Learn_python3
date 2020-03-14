from Learn_python3.Home_Work_5.H_W5_P1_1 import Person
# Employee (наследуемся от Person) (добавляются свойства: должность, опыт работы, зарплата)
# ** (только для продвинутых) Можете в конструкторе проверить, что в опыт работы и зарплата не отрицательные 😊
# Реализовать новые методы:
# 	•	возвращает должность с приставкой, которая зависит от опыта работы: Junior—менее 3 лет, Middle — от 3 до 6 лет,
#       Senior — больше 6 лет.  Т.е. метод должен вернуть позицию с приставкой Junior/Middle/Senior <position>. Если,
#       например у вас объект имел должность programmer с опытом 2 года, метод должен вернуть “Junior programmer”.
# 	•	метод, который увеличивает зарплату на сумму, которую вы передаёте аргументом.


class Employee(Person):

    def __init__(self, full_name, birth_year, position, experience, salary):
        Person.__init__(self, full_name, birth_year)
        self.position = position
        self.experience = experience
        self.salary = salary

    def get_position(self):
        a = self.position + " " + "Junior"
        b = self.position + " " + "Middle"
        c = self.position + " " + "Senior"
        if self.experience <= 3:
            return a
        elif self.experience <= 6:
            return b
        else:
            return c

    def rise_salary(self, x):
        salary = self.salary + x
        return salary

    def __str__(self):
        return f"Person with fullname  {self.full_name},  birth years  {self.birth_years}, " \
               f"position {self.position}, salary {self.salary}, experience {self.experience}"


if __name__ == '__main__':

    p = Employee("Eugene St", 1987, "Qa manager", 7, 2300)
    print("Ваша зарплата составляет:", p.rise_salary(20))
    print(p.get_position())
    print("В 2030 году вам будет:", p.age_in(2030), "года")
