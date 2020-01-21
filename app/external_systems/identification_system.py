from .data import PERSONS_DATA


class IdentificationSystem:

    @classmethod
    def get_person_data(cls, person):
        person_data = cls._get_person_data(person)
        return person_data

    @classmethod
    def _get_person_data(cls, person):
        if not len(person) or "id_number" not in person:
            return None

        for person_data in PERSONS_DATA:
            if person['id_number'] == person_data['id_number']:
                return person_data

        return None
