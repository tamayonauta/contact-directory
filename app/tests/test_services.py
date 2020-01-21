import unittest

from contacts.services import PoliceSystemService
from contacts.services import RatingSystemService


class RatingSystemServiceTestCase(unittest.TestCase):

    def test_get_score(self):
        person = {}
        rating_system_service = RatingSystemService()
        response = rating_system_service.get_score(person=person)

        self.assertEqual(response.status_code, 200)


class PoliceSystemServiceTestCase(unittest.TestCase):

    def test_get_score(self):
        person = {}
        police_system_service = PoliceSystemService()
        response = police_system_service.get_criminal_record(person=person)

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
