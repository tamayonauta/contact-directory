import unittest
from datetime import date

from contacts.contact import Person
from contacts.directory import Directory


class ValidationsTestCase(unittest.TestCase):

    def test_is_score_valid(self):
        directory = Directory()
        score = 60
        result = directory._is_score_valid(score)

        self.assertTrue(result)

    def test_is_not_score_valid(self):
        directory = Directory()
        score = 59
        result = directory._is_score_valid(score)

        self.assertFalse(result)

    def test_is_criminal_record_valid(self):
        directory = Directory()
        criminal_record = False
        result = directory._is_criminal_record_valid(criminal_record)

        self.assertTrue(result)

    def test_is_not_criminal_record_valid(self):
        directory = Directory()
        criminal_record = True
        result = directory._is_criminal_record_valid(criminal_record)

        self.assertFalse(result)

    def test_is_personal_data_valid(self):
        directory = Directory()
        person = Person(
            id_type="CC",
            id_number="1000000",
            id_exp_date=date(2001, 1, 11),
            full_name="John Doe",
            email="john@mail.com",
            phone_number="1234567890"
        )
        personal_data = {
            "id_type": "CC",
            "id_number": "1000000",
            "id_exp_date": "2001-01-11",
            "full_name": "John Doe"
        }
        result = directory._is_personal_data_valid(person, personal_data)

        self.assertTrue(result)

    def test_is_not_personal_data_valid(self):
        directory = Directory()
        person = Person(
            id_type="CC",
            id_number="1000000",
            id_exp_date=date(2001, 1, 11),
            full_name="John Doe",
            email="john@mail.com",
            phone_number="1234567890"
        )
        personal_data = {
            "id_type": "CC",
            "id_number": "1000000",
            "id_exp_date": "2001-01-11",
            "full_name": "Jean Smith"
        }
        result = directory._is_personal_data_valid(person, personal_data)

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
