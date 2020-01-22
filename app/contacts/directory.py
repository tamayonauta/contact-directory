from .contact import Contact
from .helpers import get_criminal_record
from .helpers import get_personal_data
from .helpers import get_score


class Directory:

    def __init__(self):
        self._temp_contacts = []
        self._contacts = []

    @property
    def temp_contacts(self):
        return self._temp_contacts

    def add(
        self,
        id_type,
        id_number,
        id_exp_date,
        full_name,
        email,
        phone_number
    ):
        temp_contact = Contact(
            id_type=id_type,
            id_number=id_number,
            id_exp_date=id_exp_date,
            full_name=full_name,
            email=email,
            phone_number=phone_number
        )
        self._save_temp_contact(temp_contact)

        # Get personal data
        personal_data = get_personal_data(temp_contact)
        # TODO: Validate personal data
        if not self._is_personal_data_valid(personal_data):
            return False

        # Get criminal record
        criminal_record = get_criminal_record(temp_contact)
        # TODO: Validate criminal record
        if not self._is_criminal_record_valid(criminal_record):
            return False

        # Get score
        score = get_score(temp_contact)
        # TODO: Validate score
        if not self._is_score_valid(score):
            return False

        # TODO: Save contact into directory
        self._save_contact(temp_contact)

        return True

    def _save_temp_contact(self, temp_contact):
        self._temp_contacts.append(temp_contact)

    def _is_personal_data_valid(self, personal_data):
        return True

    def _is_criminal_record_valid(self, criminal_record):
        return True

    def _is_score_valid(self, score):
        return True

    def _save_contact(self, temp_contact):
        self._contacts.append(temp_contact)
