# Входные данные
# Пользователь вводит строку.
# Выходные данные
# Воспользуйтесь одним print(), но при этом выводите с новой строки:
# 	•	Сначала выведите третий символ этой строки.
# 	•	Во второй строке выведите предпоследний символ этой строки.
# 	•	В третьей строке выведите первые пять символов этой строки.
# 	•	В четвертой строке выведите всю строку, кроме последних двух символов.
# 	•	В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0,
#      	поэтому символы выводятся, начиная с первого символа).
# 	•	В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# 	•	В седьмой строке выведите все символы в обратном порядке.
# 	•	В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# 	•	В девятой строке выведите все символы строки через один в обратном порядке, начиная с предпоследнего.
# 	•	В десятой строке выведите все символы в обратном порядке без первого и последнего элемента.
# 	•	Ну, и напоследок выведите длину данной строки.

a = input("Enter some text:")
print(a[3], a[-2], a[:5], a[:-2], a[0::2], a[1::2], a[::-1], a[::-2], a[-2::-2], a[-2:0:-1], len(a), sep="\n")






