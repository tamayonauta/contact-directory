import unittest

from contacts.services import IdentificationSystemService
from contacts.services import PoliceSystemService
from contacts.services import RatingSystemService


class RatingSystemServiceTestCase(unittest.TestCase):

    def test_get_score(self):
        person = {"id_number": "1000000"}
        rating_system_service = RatingSystemService()
        response = rating_system_service.get_score(person=person)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)


class PoliceSystemServiceTestCase(unittest.TestCase):

    def test_get_score(self):
        person = {"id_number": "1000000"}
        police_system_service = PoliceSystemService()
        response = police_system_service.get_criminal_record(person=person)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)


class IdentificationSystemServiceTestCase(unittest.TestCase):

    def test_get_person_data(self):
        person = {"id_number": "1000000"}
        identification_system_service = IdentificationSystemService()
        response = identification_system_service.get_person_data(person=person)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)


if __name__ == "__main__":
    unittest.main()
