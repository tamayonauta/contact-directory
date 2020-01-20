class Contact:
    ID_TYPES = {
        "cc": "Cédula",
        "ce": "Cédula de extranjeria",
        "pp": "Pasaporte"
    }

    def __init__(
        self,
        id_type,
        id_number,
        id_exp_date,
        full_name,
        email,
        phone_number
    ):
        self._id_type = id_type
        self._id_number = id_number
        self._id_exp_date = id_exp_date
        self._full_name = full_name
        self._email = email
        self._phone_number = phone_number

    @property
    def id_type(self):
        return self._id_type

    @property
    def id_number(self):
        return self._id_number

    @property
    def id_exp_date(self):
        return self._id_exp_date

    @property
    def full_name(self):
        return self._full_name

    @property
    def email(self):
        return self._email

    @property
    def phone_number(self):
        return self._phone_number
