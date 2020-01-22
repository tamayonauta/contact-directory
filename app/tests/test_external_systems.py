import unittest

from external_systems.identification_system import IdentificationSystem
from external_systems.police_system import PoliceSystem
from external_systems.rating_system import RatingSystem


class RatingSystemTestCase(unittest.TestCase):

    def test_get_score(self):
        score = RatingSystem._get_score(person="Person")
        min_score = RatingSystem.get_min_score()
        max_score = RatingSystem.get_max_score()

        self.assertIn(score, range(min_score, max_score + 1))


class PoliceSystemTestCase(unittest.TestCase):

    def test_get_positive_criminal_record(self):
        person = {"id_number": "123456789"}
        criminal_record = PoliceSystem._get_criminal_record(person)

        self.assertTrue(criminal_record)

    def test_get_negative_criminal_record(self):
        person = {"id_number": "123456780"}
        criminal_record = PoliceSystem._get_criminal_record(person)

        self.assertFalse(criminal_record)

    def test_get_criminal_record_without_param(self):
        person = {}
        criminal_record = PoliceSystem._get_criminal_record(person)

        self.assertIsNone(criminal_record)

    def test_get_criminal_record_with_invalid_param(self):
        person = {"id_number": ""}
        criminal_record = PoliceSystem._get_criminal_record(person)

        self.assertIsNone(criminal_record)


class IdentificationSystemTestCase(unittest.TestCase):

    def test_get_personal_data(self):
        person = {"id_number": "1000000"}
        personal_data = IdentificationSystem._get_personal_data(person)

        self.assertGreaterEqual(len(personal_data), 1)

    def test_get_personal_data_with_same_data(self):
        person = {
            "id_type": "CC",
            "id_number": "1000000",
            "id_exp_date": "2001-01-11",
            "full_name": "John Doe"
        }
        personal_data = IdentificationSystem._get_personal_data(person)

        self.assertDictEqual(personal_data, person)

    def test_get_personal_data_with_different_data(self):
        person = {
            "id_type": "CC",
            "id_number": "1000000",
            "id_exp_date": "2001-01-11",
            "full_name": "Andrew Doe"
        }
        personal_data = IdentificationSystem._get_personal_data(person)

        self.assertCountEqual(personal_data, person)

    def test_get_personal_data_not_exists(self):
        person = {"id_number": "9000000"}
        personal_data = IdentificationSystem._get_personal_data(person)

        self.assertIsNone(personal_data)

    def test_get_invalid_personal_data(self):
        person = {}
        personal_data = IdentificationSystem._get_personal_data(person)

        self.assertIsNone(personal_data)


if __name__ == "__main__":
    unittest.main()
