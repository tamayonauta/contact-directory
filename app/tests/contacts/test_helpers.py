import unittest
from datetime import date

from contacts.contact import Person
from contacts.helpers import get_criminal_record
from contacts.helpers import get_personal_data
from contacts.helpers import get_score


class GetPersonalDataTestCase(unittest.TestCase):

    def test_get_personal_data(self):
        person = Person(
            id_type="CC",
            id_number="1000000",
            id_exp_date=date(2001, 1, 11),
            full_name="John Doe",
            email="john@mail.com",
            phone_number="1234567890"
        )
        personal_data = get_personal_data(person=person)

        self.assertIsInstance(personal_data, dict)

    def test_get_invalid_personal_data(self):
        person = Person(
            id_type="CC",
            id_number="",
            id_exp_date=date(2001, 1, 11),
            full_name="John Doe",
            email="john@mail.com",
            phone_number="1234567890"
        )
        personal_data = get_personal_data(person=person)

        self.assertIsNone(personal_data)


class GetCriminalRecordTestCase(unittest.TestCase):

    def test_get_criminal_record(self):
        person = Person(
            id_type="CC",
            id_number="1000000",
            id_exp_date=date(2001, 1, 11),
            full_name="John Doe",
            email="john@mail.com",
            phone_number="1234567890"
        )
        criminal_record = get_criminal_record(person=person)

        self.assertIsInstance(criminal_record, bool)

    def test_get_invalid_criminal_record(self):
        person = Person(
            id_type="CC",
            id_number="",
            id_exp_date=date(2001, 1, 11),
            full_name="John Doe",
            email="john@mail.com",
            phone_number="1234567890"
        )
        criminal_record = get_criminal_record(person=person)

        self.assertIsNone(criminal_record)


class GetScoreTestCase(unittest.TestCase):

    def test_get_score(self):
        person = Person(
            id_type="CC",
            id_number="1000000",
            id_exp_date=date(2001, 1, 11),
            full_name="John Doe",
            email="john@mail.com",
            phone_number="1234567890"
        )
        score = get_score(person=person)

        self.assertIsInstance(score, int)


if __name__ == "__main__":
    unittest.main()
