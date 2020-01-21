from .contact import Contact
from .services import IdentificationSystemService
from .services import PoliceSystemService
from .services import serialize_response
from .services import RatingSystemService


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

        return True

    def _save_temp_contact(self, temp_contact):
        self._temp_contacts.append(temp_contact)

    def _get_score(self, person):
        rating_system_service = RatingSystemService()
        response = rating_system_service.get_score(person=person)
        score = serialize_response(response, key="score")

        return score

    def _get_criminal_record(self, person):
        police_system_service = PoliceSystemService()
        response = police_system_service.get_criminal_record(person=person)
        criminal_record = serialize_response(response, key="criminal_record")

        return criminal_record

    def _get_person_data(self, person):
        identification_system_service = IdentificationSystemService()
        response = identification_system_service.get_person_data(person=person)
        person_data = serialize_response(response)

        return person_data
