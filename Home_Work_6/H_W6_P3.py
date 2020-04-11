# Записывает в новый файл все слова в алфавитном порядке из другого файла с текстом. Каждое слово на новой строке.
# Рядом со словом укажите сколько раз оно встречалось в текст

from Learn_python3.Home_Work_4.H_W4_P3 import not_symbols

with open("Draft_for_home.txt", "r", encoding="utf-8") as f:
    for Draft_for_home in f:
        data = Draft_for_home.split()
data = [not_symbols(x) for x in data]
dataa = sorted(data)
last = {i: data.count(i) for i in dataa}
with open("file_for_past.txt", "w", encoding="utf-8") as fr:
    for data, k in last.items():
        last = data + ' ' + str(k)
        print(last, end='\n', file=fr)
f.close()
