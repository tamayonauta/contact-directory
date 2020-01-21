import requests
from unittest.mock import patch

from external_systems.police_system import PoliceSystem
from external_systems.rating_system import RatingSystem


class RatingSystemService:

    def __init__(self):
        self._URL = "https://rating-system.domain.dev"

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
        data = {"person": person}
        response = requests.post(url=self._URL, data=data)

        if response.ok:
            return response
        else:
            return None


class PoliceSystemService:

    def __init__(self):
        self._URL = "https://police-system.domain.dev"

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
        data = {"person": person}
        response = requests.post(url=self._URL, data=data)

        if response.ok:
            return response
        else:
            return None
