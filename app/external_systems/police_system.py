class PoliceSystem:

    @classmethod
    def get_criminal_record(cls, data):
        criminal_record = cls._get_criminal_record(data)
        return {"criminal_record": criminal_record}

    @classmethod
    def _get_criminal_record(cls, data):
        """
        All odd numbers has criminal record
        """

        if not len(data) or "id_number" not in data:
            return None

        try:
            if int(data['id_number'][-1]) % 2 != 0:
                return True

            return False
        except IndexError:
            return None
