from .data import PERSONS_DATA


class IdentificationSystem:

    @classmethod
    def get_person_data(cls, person):
        if not len(person) or "id_number" not in person:
            return {}

        for person_data in PERSONS_DATA:
            if person['id_number'] == person_data['id_number']:
                return person_data

        return {}
