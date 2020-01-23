import unittest
from datetime import date

from contacts.contact import Contact
from contacts.contact import Person
from contacts.directory import Directory


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
