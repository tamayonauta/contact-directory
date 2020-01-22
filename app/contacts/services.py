from unittest.mock import patch

import requests

from external_systems.identification_system import IdentificationSystem
from external_systems.police_system import PoliceSystem
from external_systems.rating_system import RatingSystem


class RatingSystemService:
    _GET_SCORE_URL = "https://rating-system.dev/score/"

    def __init__(self):
        pass

    def get_score(self, person):
        """
        Mock request of the _get_score method
        """
        # TODO: This method should delete when the system is already working
        # TODO: Use the _get_score method instead this method

        with patch("requests.post") as mock_post:
            score = RatingSystem.get_score(person=person)

            # Configure the mock to return a response with status code 200
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = score

            # Call the function, which will send a request to the server
            response = self._get_score(person=person)

        return response

    def _get_score(self, person):
        data = self._format_score_data(person)
        response = send_post_request(self._GET_SCORE_URL, data)

        return response

    def _format_score_data(self, person):
        data = {"id_number": person['id_number']}
        return data

    def _serialize_score(self, response):
        return serialize_response(response, key="score")


class PoliceSystemService:
    _GET_CRIMINAL_RECORD_URL = "https://police-system.dev/criminal-record/"

    def __init__(self):
        pass

    def get_criminal_record(self, person):
        """
        Mock request of the _get_criminal_record method
        """
        # TODO: This method should delete when the system is already working
        # TODO: Use the _get_criminal_record method instead this method

        with patch("requests.post") as mock_post:
            criminal_record = PoliceSystem.get_criminal_record(person=person)

            # Configure the mock to return a response with status code 200
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = criminal_record

            # Call the function, which will send a request to the server
            response = self._get_criminal_record(person=person)

        return response

    def _get_criminal_record(self, person):
        data = self._format_criminal_record_data(person)
        response = send_post_request(self._GET_CRIMINAL_RECORD_URL, data)

        return response

    def _format_criminal_record_data(self, person):
        data = {"id_number": person['id_number']}
        return data

    def _serialize_criminal_record(self, response):
        return serialize_response(response, key="criminal_record")


class IdentificationSystemService:
    _GET_PERSONAL_DATA_URL = "https://identification-system.dev/personal-data/"

    def __init__(self):
        pass

    def get_personal_data(self, person):
        """
        Mock request of the _get_personal_data method
        """
        # TODO: This method should delete when the system is already working
        # TODO: Use the _get_personal_data method instead this method

        with patch("requests.post") as mock_post:
            personal_data = IdentificationSystem.get_personal_data(
                person=person
            )

            # Configure the mock to return a response with status code 200
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = personal_data

            # Call the function, which will send a request to the server
            response = self._get_personal_data(person=person)

        return response

    def _get_personal_data(self, person):
        data = self._format_personal_data(person)
        response = send_post_request(self._GET_PERSONAL_DATA_URL, data)

        return response

    def _format_personal_data(self, person):
        data = {"id_number": person['id_number']}
        return data

    def _serialize_personal_data(self, response):
        return serialize_response(response)


# Utils

def send_post_request(url, data):
    """
    Send POST request
    """

    response = requests.post(url=url, data=data)

    if response.ok:
        return response
    else:
        return None


def serialize_response(response, key=None):
    """
    Get body response formatted
    """

    if response is None:
        raise ValueError("Could not get content")

    body = response.json()

    if key and key in body:
        return body[key]

    return body
