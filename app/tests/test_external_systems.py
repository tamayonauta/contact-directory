import unittest

from external_systems.rating_system import RatingSystem


class RatingSystemTestCase(unittest.TestCase):

    def test_get_score(self):
        score = RatingSystem.get_score(person="Person")
        min_score = RatingSystem.get_min_score()
        max_score = RatingSystem.get_max_score()

        self.assertIn(score, range(min_score, max_score + 1))


if __name__ == "__main__":
    unittest.main()
