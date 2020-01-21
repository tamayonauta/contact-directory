class PoliceSystem:
    # Last digits that has criminal record
    _CRIMINAL_RECORD_CHOICES = (1, 5, 9)

    @classmethod
    def get_criminal_record(cls, person):
        criminal_record = cls._get_criminal_record(person)
        return {"criminal_record": criminal_record}

    @classmethod
    def _get_criminal_record(cls, person):
        if not len(person) or "id_number" not in person:
            return None

        try:
            if int(person['id_number'][-1]) in cls._CRIMINAL_RECORD_CHOICES:
                return True

            return False
        except IndexError:
            return None
