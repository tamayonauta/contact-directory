import unittest
from datetime import date

from contacts.contact import Contact
from contacts.contact import Person


class PersonTestCase(unittest.TestCase):

    def test_create_person(self):
        data = {
            "id_type": "CC",
            "id_number": "1000000",
            "id_exp_date": date(2001, 1, 11),
            "full_name": "John Doe",
            "email": "john@mail.com",
            "phone_number": "1234567890"
        }
        person = Person(**data)

        self.assertIsInstance(person, Person)
        self.assertEqual(person.id_type, data["id_type"])
        self.assertEqual(person.id_number, data["id_number"])
        self.assertEqual(
            person.id_exp_date,
            data["id_exp_date"].strftime(Person.DATE_FORMAT)
        )
        self.assertEqual(person.full_name, data["full_name"])
        self.assertEqual(person.email, data["email"])
        self.assertEqual(person.phone_number, data["phone_number"])


class ContactTestCase(unittest.TestCase):

    def test_create_contact(self):
        data = {
            "id_type": "CC",
            "id_number": "1000000",
            "id_exp_date": date(2001, 1, 11),
            "full_name": "John Doe",
            "email": "john@mail.com",
            "phone_number": "1234567890"
        }
        contact = Contact(**data)

        self.assertIsInstance(contact, Contact)
        self.assertEqual(contact.id_type, data["id_type"])
        self.assertEqual(contact.id_number, data["id_number"])
        self.assertEqual(
            contact.id_exp_date,
            data["id_exp_date"].strftime(Person.DATE_FORMAT)
        )
        self.assertEqual(contact.full_name, data["full_name"])
        self.assertEqual(contact.email, data["email"])
        self.assertEqual(contact.phone_number, data["phone_number"])
        self.assertTrue(contact.is_accepted)


if __name__ == "__main__":
    unittest.main()
