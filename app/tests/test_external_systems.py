import unittest

from external_systems.identification_system import IdentificationSystem
from external_systems.police_system import PoliceSystem
from external_systems.rating_system import RatingSystem


class RatingSystemTestCase(unittest.TestCase):

    def test_get_score(self):
        score = RatingSystem.get_score(person="Person")
        min_score = RatingSystem.get_min_score()
        max_score = RatingSystem.get_max_score()

        self.assertIn(score, range(min_score, max_score + 1))


class PoliceSystemTestCase(unittest.TestCase):

    def test_get_positive_criminal_record(self):
        person = {"id_number": "123456789"}
        criminal_record = PoliceSystem.get_criminal_record(person)

        self.assertTrue(criminal_record)

    def test_get_negative_criminal_record(self):
        person = {"id_number": "123456780"}
        criminal_record = PoliceSystem.get_criminal_record(person)

        self.assertFalse(criminal_record)

    def test_get_criminal_record_without_param(self):
        person = {}
        criminal_record = PoliceSystem.get_criminal_record(person)

        self.assertIsNone(criminal_record)

    def test_get_criminal_record_with_invalid_param(self):
        person = {"id_number": ""}
        criminal_record = PoliceSystem.get_criminal_record(person)

        self.assertIsNone(criminal_record)


class IdentificationSystemTestCase(unittest.TestCase):

    def test_get_person_data(self):
        person = {"id_number": "1000000"}
        person_data = IdentificationSystem.get_person_data(person)

        self.assertGreaterEqual(len(person_data), 1)

    def test_get_person_data_with_same_data(self):
        person = {
            "id_type": "CC",
            "id_number": "1000000",
            "id_exp_date": "2001-01-11",
            "full_name": "John Doe"
        }
        person_data = IdentificationSystem.get_person_data(person)

        self.assertDictEqual(person_data, person)

    def test_get_person_data_with_different_data(self):
        person = {
            "id_type": "CC",
            "id_number": "1000000",
            "id_exp_date": "2001-01-11",
            "full_name": "Andrew Doe"
        }
        person_data = IdentificationSystem.get_person_data(person)

        self.assertCountEqual(person_data, person)

    def test_get_person_data_not_exists(self):
        person = {"id_number": "9000000"}
        person_data = IdentificationSystem.get_person_data(person)

        self.assertDictEqual(person_data, {})

    def test_get_invalid_person_data(self):
        person = {}
        person_data = IdentificationSystem.get_person_data(person)

        self.assertDictEqual(person_data, {})


if __name__ == "__main__":
    unittest.main()
