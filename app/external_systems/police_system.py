class PoliceSystem:
    # Last digits that has criminal record
    _CRIMINAL_RECORD_CHOICES = (1, 5, 9)

    @classmethod
    def get_criminal_record(cls, data):
        criminal_record = cls._get_criminal_record(data)
        return {"criminal_record": criminal_record}

    @classmethod
    def _get_criminal_record(cls, data):
        if not len(data) or "id_number" not in data:
            return None

        try:
            if int(data['id_number'][-1]) in cls._CRIMINAL_RECORD_CHOICES:
                return True

            return False
        except IndexError:
            return None
