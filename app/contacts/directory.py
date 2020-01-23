from .contact import Contact
from .contact import Person
from .exceptions import PersonValidationError
from .utils import run_parallel_validators
from .utils import run_score_validator


class Directory:

    def __init__(self):
        self._persons = []  # person = candidate to be contact
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

        # Save person
        self._save_person(person)
        # Validate person
        print("Validando información...")
        self._validate_person(person)
        # Save contact
        self._save_contact(person)

    def _show_contact(self, contact):
        print("==========")
        print(contact)
        print("==========")

    def _validate_person(self, person):
        validation_results = run_parallel_validators(person)

        # Check personal data validation
        if not validation_results[0]:
            raise PersonValidationError(
                "Datos incorrectos de acuerdo al Sistema de Identificación"
            )

        # Check criminal record validation
        if not validation_results[1]:
            raise PersonValidationError(
                "El prospecto tiene antecedentes judiciales de acuerdo al "
                "Sistema de la Policía"
            )

        # Check score validation
        score_validation_result = run_score_validator(person)
        if not score_validation_result:
            raise PersonValidationError(
                f"El puntaje es insuficiente de acuerdo al "
                "Sistema de Calificación"
            )

    def _is_person_exists(self, new_person):
        for person in self._persons:
            if person.id_number == new_person.id_number:
                return True

        return False

    def _save_person(self, person):
        self._persons.append(person)

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
