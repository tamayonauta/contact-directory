from .contact import Contact


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
        self._add_temp_contact(temp_contact)

    def _add_temp_contact(self, temp_contact):
        self._temp_contacts.append(temp_contact)
