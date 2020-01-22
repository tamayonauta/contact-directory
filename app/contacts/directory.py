from .contact import Contact
from .contact import Person
from .exceptions import PersonValidationError
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
                self._show_contact(contact)

    def add(
        self,
        id_type,
        id_number,
        id_exp_date,
        full_name,
        email,
        phone_number
    ):
        try:
            self._add_contact(
                id_type=id_type,
                id_number=id_number,
                id_exp_date=id_exp_date,
                full_name=full_name,
                email=email,
                phone_number=phone_number
            )
        except PersonValidationError as err:
            print(err)
            print("No se pudo agregar el contacto")
        else:
            print("Se ha agregado el contacto exitosamente")

    def _add_contact(
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

        # Validate if person already exists
        if self._is_person_exists(person):
            raise PersonValidationError("El prospecto ya existe")

        self._save_person(person)

        # Get personal data
        personal_data = get_personal_data(person)
        # Validate personal data
        if not self._is_personal_data_valid(person, personal_data):
            raise PersonValidationError(
                "Datos incorrectos de acuerdo al Sistema de Identificación"
            )

        # Get criminal record
        criminal_record = get_criminal_record(person)
        # Validate criminal record
        if not self._is_criminal_record_valid(criminal_record):
            raise PersonValidationError(
                "El prospecto tiene antecedentes judiciales de acuerdo al "
                "Sistema de la Policía"
            )

        # Get score
        score = get_score(person)
        # Validate score
        if not self._is_score_valid(score):
            raise PersonValidationError(
                f"El puntaje ({score}) es insuficiente de acuerdo al Sistema "
                "de Calificación"
            )

        # Save contact into directory
        self._save_contact(person)

    def _show_contact(self, contact):
        print("==========")
        print(contact)
        print("==========")

    def _is_person_exists(self, new_person):
        for person in self._persons:
            if person.id_number == new_person.id_number:
                return True

        return False

    def _save_person(self, person):
        self._persons.append(person)

    def _is_personal_data_valid(self, person, personal_data):
        if (
            personal_data is None or
            person.id_type != personal_data['id_type'] or
            person.id_number != personal_data['id_number'] or
            person.id_exp_date != personal_data['id_exp_date'] or
            person.full_name.lower() != personal_data['full_name'].lower()
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
