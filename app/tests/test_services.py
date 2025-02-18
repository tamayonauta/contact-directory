import unittest

from services.external_service import IdentificationSystemService
from services.external_service import PoliceSystemService
from services.external_service import RatingSystemService


class RatingSystemServiceTestCase(unittest.TestCase):

    def test_get_score(self):
        data = {"id_number": "1000000"}
        rating_system_service = RatingSystemService()
        response = rating_system_service.get_score(data)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)


class PoliceSystemServiceTestCase(unittest.TestCase):

    def test_get_score(self):
        data = {"id_number": "1000000"}
        police_system_service = PoliceSystemService()
        response = police_system_service.get_criminal_record(data)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)


class IdentificationSystemServiceTestCase(unittest.TestCase):

    def test_get_personal_data(self):
        data = {"id_number": "1000000"}
        identification_system_service = IdentificationSystemService()
        response = identification_system_service.get_personal_data(data)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)


if __name__ == "__main__":
    unittest.main()
