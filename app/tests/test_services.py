import unittest

from contacts.services import RatingSystemService


class RatingSystemServiceTestCase(unittest.TestCase):

    def test_get_score(self):
        person = {}
        rating_system_service = RatingSystemService()
        response = rating_system_service.get_score(person=person)

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
