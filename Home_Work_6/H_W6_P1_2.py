import requests


# Второй скрипт:
# •тоже самое с ролями. Здесь немного поинтересней, т.к. есть связка с книгой, которая уже должна существовать. Создайте
# книгу заранее в этом же скрипте, не надейтесь на книги, которые вы видите, их кто-то другой может удалить.

new_book_for_roles = {"title": "Rol_book",
                      "author": "Eugene St"
                      }
book_url = "http://pulse-rest-testing.herokuapp.com/books/"

created_books_for_roles = requests.post(book_url, data=new_book_for_roles)
rol_book = created_books_for_roles.json()
rol_book['id']

# создать роль
rol_url = "http://pulse-rest-testing.herokuapp.com/roles/"
rol_data = {
    "name": "Surprise",
    "type": "Horror",
    "level": "1",
    "book": book_url + str(rol_book['id'])
}
d = requests.post(rol_url, data=rol_data)
rol = d.json()
rol["id"]

# проверить что роль доступна по ссылке GET/roles/[id]
check_current_rol = requests.get(rol_url + str(rol['id']))
re = check_current_rol.json()
assert rol == re

# Проверяете, что она есть в списке ролей по запросу GET /roles/
check_all_rol = requests.get(rol_url)
check_rol = check_all_rol.json()
assert rol in check_rol

# Изменяете данные этой книги методом PUT /roles/[id]/
update_rol_info = {"name": "Surprise Update",
                   "type": "Horror or not",
                   "level": "1",
                   "book": book_url + str(rol_book['id'])
                   }
change_rol_info = requests.put(rol_url + str(rol["id"]), data=update_rol_info)
update_rol = change_rol_info.json()

# Проверьте, что она изменилась и доступна по ссылке /roles/[id]/
check_info = requests.get(rol_url + str(rol["id"]))
check = check_info.json()
assert update_rol == check

# Проверяете, что она есть в списке ролей по GET /roles/ с новыми данными.
check_update_roles = requests.get(rol_url)
check_e = check_update_roles.json()
assert update_rol in check_e

# Удаление приготовленой книги и роли
r3 = requests.delete(book_url + str(rol_book['id']))
r4 = requests.delete(rol_url + str(rol["id"]))
print(r4.status_code)
