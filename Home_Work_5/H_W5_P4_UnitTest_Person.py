import unittest
from Learn_python3.Home_Work_5.H_W5_P1_3 import ITEmployee


class TestItEmployee(unittest.TestCase):

    def setUp(self):
        self.test = ITEmployee("Eugene Storchak", 1987, "Qa Engineer", 5, 1850)

    def test_name(self):
        a = self.test.get_name()
        self.assertEqual(a, "Eugene")

    def test_surname(self):
        a = self.test.get_surname()
        self.assertEqual(a, "Storchak")

    def test_age_in(self):
        a = self.test.age_in(2020)
        self.assertEqual(a, 33)

    def test_get_position(self):
        a = self.test.get_position()
        self.assertEqual(a, "Qa Engineer Middle")

    def test_rise_salary(self):
        a = self.test.rise_salary(150)
        self.assertEqual(a, 2000)

    def test_add_skill(self):
        a = self.test.add_skill("Node")
        self.assertEqual(a, ["Node"])

    def test_add_skills(self):
        a = self.test.add_skills("Sql", "PhP", "Node")
        self.assertEqual(a, ["Sql", "PhP", "Node"])


if __name__ == "__main__":
    unittest.main()
