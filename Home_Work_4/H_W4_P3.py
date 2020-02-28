# Напишите функцию, которая удаляет все небуквенные символы внутри строки (ограничимся латинским алфавитом).
# Проверьте, что вы правильно закодили с помощью инструкции assert.
def not_symbols(a):
    b = ''
    for i in a:
        if i.isalpha():
            b += i
        assert b.isalpha()
    return b

if __name__ == '__main__':

    print(not_symbols("test 4444...233dsa33333333333333привет33333333 .... ,   bvbmkm nnn ......        ..."), )


# def symbols(a):
#     a = list(a)
#     for i in a:
#         if not i.isalpha() and " " and "!@#$%" :
#             a.remove(i)
#     print(a)
#
#
# symbols("Привет23Хатабыч45")


