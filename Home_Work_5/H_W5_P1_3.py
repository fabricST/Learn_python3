from Learn_python3.Home_Work_5.H_W5_P1_2 import Employee
# ITEmployee (наследуемся от Employee)
# 1. Реализовать метод добавления одного навыка в новое свойство skills (список) новым методом add_skill
# (см. презентацию).
# 2. * Реализовать метод добавления нескольких навыков в новое свойство skills (список) новым методом add_skills.
# Тут можно выбрать разные подходы: или аргумент один и он список навыков, которым вы расширяете список-свойство skill,
# или вы принимаете неопределённое количество аргументов, и все их добавляете в список-свойство skill


class ITEmployee(Employee):

    def __init__(self, full_name, birth_year, position, experience, salary):
        Employee.__init__(self, full_name, birth_year, position, experience, salary)
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)
        return self.skills

    def add_skills(self, *skills):
        for i in skills:
            self.skills.append(i)
        return self.skills

    def __str__(self):
        return f"Person with fullname  {self.full_name},  birth years {self.birth_years}, " \
               f"position {self.position}, salary {self.salary}, experience {self.experience}"


if __name__ == '__main__':

    it = ITEmployee("Nata Titiu", 1985, "Engineer", 5, 2320)
    it.add_skill("Qa")
    it.add_skills("Sql", "Node", "Php")

    print(it.add_skill("Sql"))
    print(it.get_name())
