import unittest
from datetime import date

from contacts.contact import Contact
from contacts.contact import Person
from contacts.directory import Directory
from contacts.directory import PersonValidator


class PersonValidatorTestCase(unittest.TestCase):

    def test_is_score_valid(self):
        person_validator = PersonValidator()
        score = 60
        result = person_validator._is_score_valid(score)

        self.assertTrue(result)

    def test_is_not_score_valid(self):
        person_validator = PersonValidator()
        score = 59
        result = person_validator._is_score_valid(score)

        self.assertFalse(result)

    def test_is_criminal_record_valid(self):
        person_validator = PersonValidator()
        criminal_record = False
        result = person_validator._is_criminal_record_valid(criminal_record)

        self.assertTrue(result)

    def test_is_not_criminal_record_valid(self):
        person_validator = PersonValidator()
        criminal_record = True
        result = person_validator._is_criminal_record_valid(criminal_record)

        self.assertFalse(result)

    def test_is_personal_data_valid(self):
        person_validator = PersonValidator()
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
        result = person_validator._is_personal_data_valid(person, personal_data)

        self.assertTrue(result)

    def test_is_not_personal_data_valid(self):
        person_validator = PersonValidator()
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
        result = person_validator._is_personal_data_valid(person, personal_data)

        self.assertFalse(result)


class DirectoryTestCase(unittest.TestCase):

    def test_save_contact(self):
        directory = Directory()
        person = Person(
            id_type="CC",
            id_number="1000000",
            id_exp_date=date(2001, 1, 11),
            full_name="John Doe",
            email="john@mail.com",
            phone_number="1234567890"
        )
        directory._save_contact(person)
        contacts = directory.contacts

        self.assertEqual(len(contacts), 1)
        self.assertIsInstance(contacts[0], Contact)


if __name__ == "__main__":
    unittest.main()
