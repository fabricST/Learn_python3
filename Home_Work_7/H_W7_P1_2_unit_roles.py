import unittest
import requests

# Создаём наборы CRUD (create, read, update, delete) тестов, используя unittest (как позитивные, так и негативные)
# для тестирования нашего приложения. Проверяем статус код и тело ответа.


class Create_read_roles(unittest.TestCase):

    def setUp(self):
        self.book_for_roles = {"title": "Roles_book",
                               "author": "Eugene"
                               }
        self.book_url = "http://pulse-rest-testing.herokuapp.com/books/"
        created_books_for_roles = requests.post(self.book_url, data=self.book_for_roles)
        rol_book = created_books_for_roles.json()
        self.book_id = rol_book['id']
        self.data = {"name": "Some name of the role",
                     "type": "comedy",
                     "level": 3,
                     "book": self.book_url + str(rol_book['id'])
                     }

        self.rol_url = "http://pulse-rest-testing.herokuapp.com/roles/"

        self.update_data = {"name": "Some name of the roles or DELETE ALL BOOKS",
                            "type": "comedy or horror",
                            "level": 5,
                            "book": self.book_url + str(rol_book['id'])
                            }

    def test_create_roles(self):
        send_data = requests.post(self.rol_url, data=self.data)
        self.assertEqual(201, send_data.status_code)
        self.roles = send_data.json()
        self.roles_ID = self.roles["id"]
        self.roles.pop("id")
        self.assertEqual(self.roles, self.data)

    def test_read_roles(self):
        send_data = requests.post(self.rol_url, data=self.data)
        self.assertEqual(201, send_data.status_code)
        self.roles = send_data.json()
        self.roles_ID = self.roles["id"]
        get_data = requests.get(self.rol_url + str(self.roles["id"]))
        self.assertEqual(200, get_data.status_code)
        self.g = get_data.json()
        self.assertEqual(self.g, self.roles)

    def tearDown(self):
        de_rol = requests.delete(self.rol_url + str(self.roles_ID))
        de_book = requests.delete(self.book_url + str(self.book_id))


if __name__ == "__main__":
    unittest.main()


class Update_Delete_roles(unittest.TestCase):

    def setUp(self):
        self.book_for_roles = {"title": "Roles_book",
                               "author": "Eugene"
                               }
        self.book_url = "http://pulse-rest-testing.herokuapp.com/books/"

        created_books_for_roles = requests.post(self.book_url, data=self.book_for_roles)
        rol_book = created_books_for_roles.json()
        self.book_id = rol_book['id']

        self.data = {"name": "Some name of the role",
                     "type": "comedy",
                     "level": 3,
                     "book": self.book_url + str(rol_book['id'])
                     }
        self.rol_url = "http://pulse-rest-testing.herokuapp.com/roles/"
        Precondition_for_update = requests.post(self.rol_url, data=self.data)
        self.roles = Precondition_for_update.json()
        self.roles_id = self.roles["id"]

        self.update_data = {"name": "Some name of the role after update",
                            "type": "comedy or not",
                            "level": 7,
                            "book": self.book_url + str(rol_book['id'])
                            }

    def test_update_roles(self):
        update_data = requests.put(self.rol_url + str(self.roles_id), data=self.update_data)
        self.assertEqual(200, update_data.status_code)
        self.got_update = update_data.json()
        self.got_update_id = self.got_update["id"]
        self.got_update.pop('id')
        self.assertEqual(self.update_data, self.got_update)

    def test_delete_roles(self):
        del_precondition = requests.delete(self.rol_url + str(self.roles_id))
        self.assertEqual(204, del_precondition.status_code)
        print(del_precondition.status_code)

    def tearDown(self):
        clear_roles = requests.delete(self.rol_url + str(self.roles_id))
        clear_book = requests.delete(self.book_url + str(self.book_id))


if __name__ == "__main__":
    unittest.main()
