import unittest

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


if __name__ == "__main__":
    unittest.main()
