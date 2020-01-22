from .contact import Contact
from .services import IdentificationSystemService
from .services import PoliceSystemService
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
        score = rating_system_service._serialize_score(response)

        return score

    def _get_criminal_record(self, person):
        police_system_service = PoliceSystemService()
        response = police_system_service.get_criminal_record(person=person)
        criminal_record = police_system_service._serialize_criminal_record(
            response
        )

        return criminal_record

    def _get_personal_data(self, person):
        identification_system_service = IdentificationSystemService()
        response = identification_system_service.get_personal_data(
            person=person
        )
        personal_data = identification_system_service._serialize_personal_data(
            response
        )

        return personal_data
