from .contact import Contact
from .contact import Person
from .helpers import get_criminal_record
from .helpers import get_personal_data
from .helpers import get_score


class Directory:
    _MIN_SCORE_ACCEPTED = 60

    def __init__(self):
        self._persons = []
        self._contacts = []

    @property
    def persons(self):
        return self._persons

    @property
    def contacts(self):
        return self._contacts

    def show(self):
        if not self._contacts:
            print("No hay contactos")
        else:
            for contact in self._contacts:
                self.show_contact(contact)

    def show_contact(self, contact):
        print("==========")
        print(contact)
        print("==========")

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
        # Validate personal data
        if not self._is_personal_data_valid(person, personal_data):
            return False

        # Get criminal record
        criminal_record = get_criminal_record(person)
        # Validate criminal record
        if not self._is_criminal_record_valid(criminal_record):
            return False

        # Get score
        score = get_score(person)
        # Validate score
        if not self._is_score_valid(score):
            return False

        # Save contact into directory
        self._save_contact(person)

        return True

    def _save_person(self, person):
        self._persons.append(person)

    def _is_personal_data_valid(self, person, personal_data):
        if (
            personal_data is None or
            person.id_type != personal_data['id_type'] or
            person.id_number != personal_data['id_number'] or
            person.id_exp_date != personal_data['id_exp_date'] or
            person.full_name != personal_data['full_name']
        ):
            return False

        return True

    def _is_criminal_record_valid(self, criminal_record):
        return True if not criminal_record else False

    def _is_score_valid(self, score):
        return True if score >= self._MIN_SCORE_ACCEPTED else False

    def _save_contact(self, person):
        contact = Contact(
            id_type=person.id_type,
            id_number=person.id_number,
            id_exp_date=person.get_id_exp_date(),
            full_name=person.full_name,
            email=person.email,
            phone_number=person.phone_number
        )
        self._contacts.append(contact)
