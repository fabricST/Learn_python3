# Person (два свойства: 1. теперь full_name пусть будет свойством, а не функцией (одно поле, мы ожидаем - тип строка и
# состоит из двух слов «имя фамилия»), а свойств name и surname нету, 2. год рождения).
# Реализовать методы, которые:
# 	•	выделяет только имя из full_name
# 	•	выделяет только фамилию из full_name;
# 	•	вычисляет сколько лет было/есть/исполнится в году, который передаётся параметром (obj.age_in(year));
# если не передавать параметр, по умолчанию, сколько лет в этом году;


class Person:

    def __init__(self, full_name, birth_years):
        self.full_name = full_name
        self.birth_years = birth_years

    def get_name(self):
        x = self.full_name.find(' ')
        self.name = self.full_name[:x]
        return self.name

    def get_surname(self):
        y = self.full_name.find(' ')
        self.surname = self.full_name[y+1:]
        return self.surname

    def age_in(self, year=2020):
        age = year - self.birth_years
        return age

    def __str__(self):
        return f"Person with fullname  {self.full_name}, name {self.name}, surname {self.surname}, birth years" \
               f"{self.birth_years}"


if __name__ == '__main__':

    p = Person("Сторчак Евгений", 1987)
    print(p.get_name())
    print(p.get_surname)
    print(p.age_in())
