import unittest

from external_systems.identification_system import IdentificationSystem
from external_systems.police_system import PoliceSystem
from external_systems.rating_system import RatingSystem


class RatingSystemTestCase(unittest.TestCase):

    def test_get_score(self):
        data = {"id_number": "1000000"}
        min_score = RatingSystem.get_min_score()
        max_score = RatingSystem.get_max_score()
        score = RatingSystem._get_score(data)

        self.assertIn(score, range(min_score, max_score + 1))


class PoliceSystemTestCase(unittest.TestCase):

    def test_get_positive_criminal_record(self):
        data = {"id_number": "1000001"}
        criminal_record = PoliceSystem._get_criminal_record(data)

        self.assertTrue(criminal_record)

    def test_get_negative_criminal_record(self):
        data = {"id_number": "1000000"}
        criminal_record = PoliceSystem._get_criminal_record(data)

        self.assertFalse(criminal_record)

    def test_get_criminal_record_without_param(self):
        data = {}
        criminal_record = PoliceSystem._get_criminal_record(data)

        self.assertIsNone(criminal_record)

    def test_get_criminal_record_with_invalid_param(self):
        data = {"id_number": ""}
        criminal_record = PoliceSystem._get_criminal_record(data)

        self.assertIsNone(criminal_record)


class IdentificationSystemTestCase(unittest.TestCase):

    def test_get_personal_data(self):
        data = {"id_number": "1000000"}
        personal_data = IdentificationSystem._get_personal_data(data)

        self.assertGreaterEqual(len(personal_data), 1)

    def test_get_personal_data_with_same_data(self):
        data = {
            "id_type": "CC",
            "id_number": "1000000",
            "id_exp_date": "2001-01-11",
            "full_name": "John Doe"
        }
        personal_data = IdentificationSystem._get_personal_data(data)

        self.assertDictEqual(personal_data, data)

    def test_get_personal_data_with_different_data(self):
        data = {
            "id_type": "CC",
            "id_number": "1000000",
            "id_exp_date": "2001-01-11",
            "full_name": "Andrew Doe"
        }
        personal_data = IdentificationSystem._get_personal_data(data)

        self.assertCountEqual(personal_data, data)

    def test_get_personal_data_not_exists(self):
        data = {"id_number": "9000000"}
        personal_data = IdentificationSystem._get_personal_data(data)

        self.assertIsNone(personal_data)

    def test_get_invalid_personal_data(self):
        data = {}
        personal_data = IdentificationSystem._get_personal_data(data)

        self.assertIsNone(personal_data)


if __name__ == "__main__":
    unittest.main()
