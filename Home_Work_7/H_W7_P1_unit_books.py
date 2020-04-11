import unittest
import requests
from HtmlTestRunner import HTMLTestRunner

# Создаём наборы CRUD (create, read, update, delete) тестов, используя unittest (как позитивные, так и негативные)
# для тестирования нашего приложения. Проверяем статус код и тело ответа.


class CRUD_Books(unittest.TestCase):

    def setUp(self):
        self.data_book = {
            "title": "My book",
            "author": "Eugene St"
        }
        create = requests.post("http://pulse-rest-testing.herokuapp.com/books/", data=self.data_book)
        self.data = create.json()
        self.book_id = self.data['id']

    def test_create(self):
        create_request = requests.post("http://pulse-rest-testing.herokuapp.com/books/", data=self.data_book)
        self.assertEqual(201, create_request.status_code)
        self.got_book = create_request.json()
        self.book_id = self.got_book['id']
        self.got_book.pop('id')
        self.assertEqual(self.data_book, self.got_book)

    def test_read(self):
        send = requests.get("http://pulse-rest-testing.herokuapp.com/books/")
        self.assertEqual(200, send.status_code)
        c = send.json()
        self.assertIn(self.data, c)

    def test_update(self):
        send_update_data = requests.put("http://pulse-rest-testing.herokuapp.com/books/" + str(self.data['id']), data={
            "title": "The book that not bad",
            "author": "Eugene"
        })
        self.assertEqual(200, send_update_data.status_code)
        self.got_data = send_update_data.json()
        got_updated_data = requests.get("http://pulse-rest-testing.herokuapp.com/books/" + str(self.data['id']))
        self.assertEqual(200, send_update_data.status_code)
        self.f = got_updated_data.json()
        self.assertEqual(self.got_data, self.f)

    def test_delete(self):
        send_delete_request = requests.delete("http://pulse-rest-testing.herokuapp.com/books/" + str(self.data['id']))
        self.assertEqual(204, send_delete_request.status_code)

    def tearDown(self):
        x = requests.delete("http://pulse-rest-testing.herokuapp.com/books/" + str(self.data['id']))
        x2 = requests.delete("http://pulse-rest-testing.herokuapp.com/books/" + str(self.book_id))


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="./"))
