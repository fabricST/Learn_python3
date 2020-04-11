import requests

# Тестовое приложение с REST API  http://pulse-rest-testing.herokuapp.com/
# Создаём один скрипт:
# 	•	Создаём книгу POST /books/, вы запоминаете его id.
# 	•	Проверяете, что она создалась и доступна по ссылке GET/books/[id]
# 	•	Проверяете, что она есть в списке книг по запросу GET /books/
# 	•	Изменяете данные этой книги методом PUT /books/[id]/
# 	•	Проверяете, что она изменилась и доступна по ссылке /books/[id]
# 	•	Проверяете, что она есть в списке книг по GET /books/ с новыми данными.
# 	•	Удаляете эту книгу методом DELETE /books/[id].
# Все проверки делать программно, а не глазами, т.е. проверить, что в теле response данные такие же как в вашем исходном
# словаре путём сравнения значений в словарях!!!!!

# Создаём книгу POST /books/, вы запоминаете его id.
new_book = {"title": "My book",
            "author": "Eugene St"
            }
r = requests.post("http://pulse-rest-testing.herokuapp.com/books/", data=new_book)
books = r.json()
books['id']

# Проверяете, что она создалась и доступна по ссылке GET/books/[id]
check_books = requests.get("http://pulse-rest-testing.herokuapp.com/books/" + str(books['id']))
req = check_books.json()
assert books == req

# Проверяете, что она есть в списке книг по запросу GET /books/
check_all = requests.get("http://pulse-rest-testing.herokuapp.com/books/")
check_book = check_all.json()
assert books in check_book

# Изменяете данные этой книги методом PUT /books/[id]/
new_info = {"title": "update_book_info",
            "author": "Eugene"
            }
change_book = requests.put("http://pulse-rest-testing.herokuapp.com/books/" + str(books['id']), data=new_info)
updated_books = change_book.json()

# Проверьте, что она изменилась и доступна по ссылке /books/[id]/
check_new_info = requests.get("http://pulse-rest-testing.herokuapp.com/books/" + str(books['id']))
check_new = check_new_info.json()
check_new.pop("id")
assert check_new == new_info

# Проверяете, что она есть в списке книг по GET /books/ с новыми данными.
check_update_book = requests.get("http://pulse-rest-testing.herokuapp.com/books/")
check_dict = check_update_book.json()
assert updated_books in check_dict

# Удаляете эту книгу методом DELETE /books/[id]
r2 = requests.delete("http://pulse-rest-testing.herokuapp.com/books/" + str(books['id']))
