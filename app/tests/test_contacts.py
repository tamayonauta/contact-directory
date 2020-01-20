import unittest
from datetime import date

from contacts.contact import Contact


class ContactTestCase(unittest.TestCase):

    def test_create_contact(self):
        new_contact = Contact(
            id_type="Cédula",
            id_number="1000000",
            id_exp_date=date(2000, 3, 31),
            full_name="John Doe",
            email="john@mail.com",
            phone_number="1234567890"
        )

        self.assertIsInstance(new_contact, Contact)


if __name__ == "__main__":
    unittest.main()
