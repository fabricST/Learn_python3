# Задания из класса про работу с файлами на слайдах 4, 8, 9, 10:
# 1. Кто не успел доделываем / тем, кто успел: воспользуйтесь другим способом для записи в файл (кто сделал с помощью
# методов – делают с помощью print, кто сделал с помощью print – делают с помощью методов)
# 2. А теперь воспользуйтесь менеджером контекста для файлов (with … as).


a = open("/Users/fabric/PycharmProjects/Home_Work_python/Learn_python3/Home_Work_4/H_W4_P1.py")
data = a.read()
print(data)
a.close()


# Записать в текстовый файл вашу песню “la-la-la”.
with open("/Users/fabric/PycharmProjects/Home_Work_python/Learn_python3/Home_Work_4/H_W4_P1.py", "r") as fr:
    data = fr.read()
with open("la-la-la.py", "w") as fw:
    fw.write(data)

# Прочитать и вывести на экран код файла, в котором вы создавали класс Person
read = open("/Users/fabric/PycharmProjects/Home_Work_python/Learn_python3/Home_Work_5/H_W5_P1_1.py", "r")
data = read.read()
print(data)
read.close()

# Задание: считываем построчно строки из файла и выводим строки, добавляя в конец этих строк восклицательный знак
one_line = open("/Users/fabric/PycharmProjects/Home_Work_python/Learn_python3/Home_Work_4/H_W4_P1.py", "r")
data = one_line.readline()
for line in one_line:
    print(line.rstrip() + "!")
one_line.close()

# Записываем “Number: строка из файла” из одного файла в другой. Не забываем закрывать файлы
with open('first_file.txt', 'w',) as f:
    f.write("Number: строка из файла")
with open('first_file.txt', 'r') as f:
    data = f.readlines()
with open('second_file.txt', 'w') as f:
    f.writelines(data)
f.close()
