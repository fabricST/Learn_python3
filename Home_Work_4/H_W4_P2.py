# Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов.
# Учитываем, что может быть повторяющиеся значения аргументов.
def order (*args):
    args = sorted(set(args))
    print(args[1])
order(1, 1, 1, 1, 1, 1, 1222, 444, 3,2,2, 455, 5)
