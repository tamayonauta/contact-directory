from services.external_service import IdentificationSystemService
from services.external_service import PoliceSystemService
from services.external_service import RatingSystemService


def get_personal_data(person):
    """
    Get personal data of the person
    """

    identification_system_service = IdentificationSystemService()
    data = identification_system_service.format_personal_data(person)
    response = identification_system_service.get_personal_data(data)
    personal_data = identification_system_service.serialize_personal_data(
        response
    )

    return personal_data


def get_criminal_record(person):
    """
    Get criminal record of the person
    """

    police_system_service = PoliceSystemService()
    data = police_system_service.format_criminal_record_data(person)
    response = police_system_service.get_criminal_record(data)
    criminal_record = police_system_service.serialize_criminal_record(
        response
    )

    return criminal_record


def get_score(person):
    """
    Get score of the person
    """

    rating_system_service = RatingSystemService()
    data = rating_system_service.format_score_data(person)
    response = rating_system_service.get_score(data)
    score = rating_system_service.serialize_score(response)

    return score
