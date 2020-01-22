from .data import PERSONAL_DATA


class IdentificationSystem:

    @classmethod
    def get_personal_data(cls, person):
        personal_data = cls._get_personal_data(person)
        return personal_data

    @classmethod
    def _get_personal_data(cls, person):
        if not len(person) or "id_number" not in person:
            return None

        for personal_data in PERSONAL_DATA:
            if personal_data['id_number'] == person['id_number']:
                return personal_data

        return None
