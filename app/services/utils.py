import time

import requests


def simulate_request_latency():
    """
    Simulate request latency
    """

    SECONDS = 2
    time.sleep(SECONDS)


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
