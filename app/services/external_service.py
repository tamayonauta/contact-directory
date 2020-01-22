from unittest.mock import patch

from external_systems.identification_system import IdentificationSystem
from external_systems.police_system import PoliceSystem
from external_systems.rating_system import RatingSystem

from .utils import send_post_request
from .utils import serialize_response
from .utils import simulate_request_latency


class RatingSystemService:
    _GET_SCORE_URL = "https://rating-system.dev/score/"

    def format_score_data(self, person):
        data = {"id_number": person.id_number}
        return data

    def serialize_score(self, response):
        return serialize_response(response, key="score")

    def get_score(self, data):
        """
        Mock request of the _get_score method
        """
        # TODO: This method should delete when the system is already working
        # TODO: Use the _get_score method instead this method

        with patch("requests.post") as mock_post:
            score = RatingSystem.get_score(data)

            # Configure the mock to return a response with status code 200
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = score

            # Simulate request latency
            simulate_request_latency()

            # Call the function, which will send a request to the server
            response = self._get_score(data)

        return response

    def _get_score(self, data):
        response = send_post_request(self._GET_SCORE_URL, data)
        return response


class PoliceSystemService:
    _GET_CRIMINAL_RECORD_URL = "https://police-system.dev/criminal-record/"

    def format_criminal_record_data(self, person):
        data = {"id_number": person.id_number}
        return data

    def serialize_criminal_record(self, response):
        return serialize_response(response, key="criminal_record")

    def get_criminal_record(self, data):
        """
        Mock request of the _get_criminal_record method
        """
        # TODO: This method should delete when the system is already working
        # TODO: Use the _get_criminal_record method instead this method

        with patch("requests.post") as mock_post:
            criminal_record = PoliceSystem.get_criminal_record(data)

            # Configure the mock to return a response with status code 200
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = criminal_record

            # Simulate request latency
            simulate_request_latency()

            # Call the function, which will send a request to the server
            response = self._get_criminal_record(data)

        return response

    def _get_criminal_record(self, data):
        response = send_post_request(self._GET_CRIMINAL_RECORD_URL, data)
        return response


class IdentificationSystemService:
    _GET_PERSONAL_DATA_URL = "https://identification-system.dev/personal-data/"

    def format_personal_data(self, person):
        data = {"id_number": person.id_number}
        return data

    def serialize_personal_data(self, response):
        return serialize_response(response)

    def get_personal_data(self, data):
        """
        Mock request of the _get_personal_data method
        """
        # TODO: This method should delete when the system is already working
        # TODO: Use the _get_personal_data method instead this method

        with patch("requests.post") as mock_post:
            personal_data = IdentificationSystem.get_personal_data(data)

            # Configure the mock to return a response with status code 200
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = personal_data

            # Simulate request latency
            simulate_request_latency()

            # Call the function, which will send a request to the server
            response = self._get_personal_data(data)

        return response

    def _get_personal_data(self, data):
        response = send_post_request(self._GET_PERSONAL_DATA_URL, data)
        return response
