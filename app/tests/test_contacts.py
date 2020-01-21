import unittest
from datetime import date

from contacts.contact import Contact
from contacts.directory import Directory


class ContactTestCase(unittest.TestCase):

    def test_create_contact(self):
        new_contact = Contact(
            id_type="CC",
            id_number="1000000",
            id_exp_date=date(2001, 1, 11),
            full_name="John Doe",
            email="john@mail.com",
            phone_number="1234567890"
        )

        self.assertIsInstance(new_contact, Contact)


class DirectoryTestCase(unittest.TestCase):

    def test_get_score(self):
        directory = Directory()
        person = {}
        score = directory._get_score(person=person)

        self.assertIsInstance(score, int)

    def test_get_criminal_record(self):
        directory = Directory()
        person = {"id_number": "1000000"}
        criminal_record = directory._get_criminal_record(person=person)

        self.assertIsInstance(criminal_record, bool)

    def test_get_person_data(self):
        directory = Directory()
        person = {"id_number": "1000000"}
        person_data = directory._get_person_data(person=person)

        self.assertIsInstance(person_data, dict)


if __name__ == "__main__":
    unittest.main()
