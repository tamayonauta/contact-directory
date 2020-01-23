from abc import ABC
from abc import abstractmethod

from .helpers import get_criminal_record
from .helpers import get_personal_data
from .helpers import get_score


class Validator(ABC):

    @abstractmethod
    def validate(self):
        pass


class PersonalDataValidator(Validator):

    @classmethod
    def validate(cls, person):
        personal_data = get_personal_data(person)
        return cls._is_personal_data_valid(person, personal_data)

    @staticmethod
    def _is_personal_data_valid(person, personal_data):
        if (
            personal_data is None or
            person.id_type != personal_data['id_type'] or
            person.id_number != personal_data['id_number'] or
            person.id_exp_date != personal_data['id_exp_date'] or
            person.full_name.lower() != personal_data['full_name'].lower()
        ):
            return False

        return True


class CriminalRecordValidator(Validator):

    @classmethod
    def validate(cls, person):
        criminal_record = get_criminal_record(person)
        return cls._is_criminal_record_valid(criminal_record)

    @staticmethod
    def _is_criminal_record_valid(criminal_record):
        return True if not criminal_record else False


class ScoreValidator(Validator):
    _MIN_SCORE_ACCEPTED = 60

    @classmethod
    def validate(cls, person):
        score = get_score(person)
        return cls._is_score_valid(score)

    @classmethod
    def _is_score_valid(cls, score):
        return True if score >= cls._MIN_SCORE_ACCEPTED else False
