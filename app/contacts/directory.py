from .contact import Person
from .helpers import get_criminal_record
from .helpers import get_personal_data
from .helpers import get_score


class Directory:

    def __init__(self):
        self._persons = []
        self._contacts = []

    @property
    def persons(self):
        return self._persons

    def add(
        self,
        id_type,
        id_number,
        id_exp_date,
        full_name,
        email,
        phone_number
    ):
        person = Person(
            id_type=id_type,
            id_number=id_number,
            id_exp_date=id_exp_date,
            full_name=full_name,
            email=email,
            phone_number=phone_number
        )
        self._save_person(person)

        # Get personal data
        personal_data = get_personal_data(person)
        # TODO: Validate personal data
        if not self._is_personal_data_valid(personal_data):
            return False

        # Get criminal record
        criminal_record = get_criminal_record(person)
        # TODO: Validate criminal record
        if not self._is_criminal_record_valid(criminal_record):
            return False

        # Get score
        score = get_score(person)
        # TODO: Validate score
        if not self._is_score_valid(score):
            return False

        # TODO: Save contact into directory
        self._save_contact(person)

        return True

    def _save_person(self, person):
        self._persons.append(person)

    def _is_personal_data_valid(self, personal_data):
        return True

    def _is_criminal_record_valid(self, criminal_record):
        return True

    def _is_score_valid(self, score):
        return True

    def _save_contact(self, person):
        self._contacts.append(person)
