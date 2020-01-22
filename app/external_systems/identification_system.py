from .data import PERSONAL_DATA


class IdentificationSystem:

    @classmethod
    def get_personal_data(cls, data):
        personal_data = cls._get_personal_data(data)
        return personal_data

    @classmethod
    def _get_personal_data(cls, data):
        if not len(data) or "id_number" not in data:
            return None

        for personal_data in PERSONAL_DATA:
            if personal_data['id_number'] == data['id_number']:
                return personal_data

        return None
