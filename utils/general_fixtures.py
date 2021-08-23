import pytest
import requests

from client.client import HttpClient
from data.general_constants import *


@pytest.fixture(scope="session")
def client(env):
    client = HttpClient(env)
    return client


@pytest.fixture()
def bearer_token():
    url = AUTH_ROUTE

    payload = GRANT_TYPE
    headers = {
        'authorization': BASIC_KEY,
        'content-type': 'application/x-www-form-urlencoded'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        response.raise_for_status()
        parsed_body = response.json()
        token = 'Bearer ' + parsed_body["access_token"]
        return {"Authorization": token}
    except Exception as e:
        print(e)
        raise Exception('Failed to acquire token') from e
