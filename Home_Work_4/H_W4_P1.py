# Пишем функцию, которая генерирует песню la-la-la. Функция принимает 3 аргумента:
# 1-е число – сколько строк будет в песне. По умолчанию 3 
# 2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
# 3-е число – если 0, то в конце песни (в конце последней строчки) стоит точка, если 1, то в конце стоит «!».По умолчанию 0

def song(a=3, b=3, c=0):
    d = "la-" * b
    g = (d[:-1] + '\n')*a
    if c == 0:
        song = g[:-1]+'.'
    else:
        song = g[:-1]+ '!'
    return song
if __name__ == '__main__':
    print(song(7,8,3))

