import random


class RatingSystem:
    _MIN_SCORE = 0
    _MAX_SCORE = 100

    @classmethod
    def get_min_score(cls):
        return cls._MIN_SCORE

    @classmethod
    def get_max_score(cls):
        return cls._MAX_SCORE

    @classmethod
    def get_score(cls, person):
        score = random.randint(cls._MIN_SCORE, cls._MAX_SCORE)
        return score
