from .contact import Contact
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

        if response is None:
            raise Exception("No se pudo obtener el puntaje")

        body = response.json()
        score = body['score']

        return score
