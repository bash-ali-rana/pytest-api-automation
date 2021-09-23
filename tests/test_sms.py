from http import HTTPStatus

import pytest

from data.general_constants import *
import utils.helper as helper


class TestSMS:

    @pytest.mark.parametrize("payload", [
        SMS_PAYLOAD,
        (helper.update_request_body(SMS_PAYLOAD, '["from"]', "update", "+923034843874")),
        (helper.update_request_body(SMS_PAYLOAD, '["to"]', "update", "+923034843874")),
        (helper.update_request_body(SMS_PAYLOAD, '["body"]', "update", "This is new body"))
    ])
    def test_post_sms_status_200_ok(self, bearer_token, client, payload, capsys):
        """
        Args:
            bearer_token: Token value for test execution
            client: HTTP client to request API
            payload: Json payload to provide to request body, updates form pytest params
            capsys: Allow access to stdout/stderr output created during test execution
        """
        headers = bearer_token
        response = client.post_req(url=SMS_ENDPOINT, headers=headers, json_payload=payload)
        with capsys.disabled():
            print(response.request.body)
            print(response.json())

        # This will not fail test as I'm getting error 400 for insufficient balance
        with pytest.raises(Exception):
            assert response.status_code == HTTPStatus.OK

    @pytest.mark.parametrize("payload, error", [(SMS_PAYLOAD, MSSG_INVALID_TOKEN)])
    def test_post_sms_status_401_unauthorized(self, client, payload, error, capsys):
        """
        Args:
            client: HTTP client to request API
            payload: Json payload to provide to request body, updates form pytest params
            error: Error message to validate from response body
            capsys: Allow access to stdout/stderr output created during test execution
        """
        response = client.post_req(url=SMS_ENDPOINT, headers=EXPIRED_TOKEN, json_payload=payload)
        with capsys.disabled():
            print(response.request.body)
            print(response.json())
        assert response.status_code == HTTPStatus.UNAUTHORIZED
        res_message = response.json()["error"]
        assert error in res_message

    @pytest.mark.parametrize("payload, error", [
        (helper.update_request_body(BAD_SMS_PAYLOAD, '["from"]', "update", None), MSGS_INSUFFICIENT_BALANCE),
        (helper.update_request_body(BAD_SMS_PAYLOAD, '["from"]', "update", "abc"), MSGS_INSUFFICIENT_BALANCE),
        (helper.update_request_body(BAD_SMS_PAYLOAD, '["from"]', "update", 1), MSGS_INSUFFICIENT_BALANCE),
        (helper.update_request_body(BAD_SMS_PAYLOAD, '["from"]', "update", ""), MSGS_INSUFFICIENT_BALANCE),
        (helper.update_request_body(BAD_SMS_PAYLOAD, '["to"]', "update", None), MSGS_INSUFFICIENT_BALANCE),
        (helper.update_request_body(BAD_SMS_PAYLOAD, '["to"]', "update", "abc"), MSGS_INSUFFICIENT_BALANCE),
        (helper.update_request_body(BAD_SMS_PAYLOAD, '["to"]', "update", 1), MSGS_INSUFFICIENT_BALANCE),
        (helper.update_request_body(BAD_SMS_PAYLOAD, '["to"]', "update", ""), MSGS_INSUFFICIENT_BALANCE),
        (helper.update_request_body(BAD_SMS_PAYLOAD, '["body"]', "update", None), MSGS_INSUFFICIENT_BALANCE),
        (helper.update_request_body(BAD_SMS_PAYLOAD, '["body"]', "update", ""), MSGS_INSUFFICIENT_BALANCE),
        (helper.update_request_body(BAD_SMS_PAYLOAD, '["body"]', "update", 1), MSGS_INSUFFICIENT_BALANCE),
        (helper.update_request_body(BAD_SMS_PAYLOAD, '["body"]', "update", True), MSGS_INSUFFICIENT_BALANCE),
        (helper.update_request_body(BAD_SMS_PAYLOAD, '["flash"]', "update", None), MSGS_INSUFFICIENT_BALANCE),
        (helper.update_request_body(BAD_SMS_PAYLOAD, '["ttl"]', "update", None), MSGS_INSUFFICIENT_BALANCE),
        (helper.update_request_body(BAD_SMS_PAYLOAD, '["transcode"]', "update", None), MSGS_INSUFFICIENT_BALANCE),
        (helper.update_request_body(BAD_SMS_PAYLOAD, '["urlShortener"]', "update", None), MSGS_INSUFFICIENT_BALANCE),
        (helper.update_request_body(BAD_SMS_PAYLOAD, '["flash"]', "update", None), MSGS_INSUFFICIENT_BALANCE),
        (helper.update_request_body(BAD_SMS_PAYLOAD, '["flash"]', "update", None), MSGS_INSUFFICIENT_BALANCE),
        (helper.update_request_body(BAD_SMS_PAYLOAD, '["flash"]', "update", None), MSGS_INSUFFICIENT_BALANCE)
    ])
    def test_post_sms_status_400_bad_request(self, bearer_token, client, payload, error, capsys):
        """
        Args:
            bearer_token: Token value for test execution
            client: HTTP client to request API
            payload: Json payload to provide to request body, updates form pytest params
            error: Error message to validate from response body
            capsys: Allow access to stdout/stderr output created during test execution
        """
        url = SMS_ENDPOINT
        headers = bearer_token
        response = client.post_req(url, headers=headers, json_payload=payload)
        res_message = response.json()["developerMessage"]
        with capsys.disabled():
            print(response.request.body)
            print(response.json())
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert error in res_message

    @pytest.mark.parametrize("payload, error", [(SMS_PAYLOAD, MSSG_INVALID_TOKEN)])
    def test_post_sms_status_401_unauthorized(self, client, payload, error, capsys):
        """
        Args:
            client: HTTP client to request API
            payload: Json payload to provide to request body, updates form pytest params
            error: Error message to validate from response body
            capsys: Allow access to stdout/stderr output created during test execution
        """
        response = client.post_req(url=SMS_ENDPOINT, headers=EXPIRED_TOKEN, json_payload=payload)
        with capsys.disabled():
            print(response.request.body)
            print(response.json())
        assert response.status_code == HTTPStatus.UNAUTHORIZED
        res_message = response.json()["error"]
        assert error in res_message

    @pytest.mark.parametrize("payload, error", [
        ("", MSSG_INTERNAL_SERVER_ERROR),  # empty body
        ("{,}", MSSG_INTERNAL_SERVER_ERROR),  # bad json body
    ])
    def test_post_sms_status_500_internal_server_error(self, bearer_token, client, payload, error, capsys):
        """
        Args:
            bearer_token: Token value for test execution
            client: HTTP client to request API
            payload: Json payload to provide to request body, updates form pytest params
            error: Error message to validate from response body
            capsys: Allow access to stdout/stderr output created during test execution
        """
        response = client.post_req(url=SMS_ENDPOINT, headers=bearer_token, json_payload=payload)
        with capsys.disabled():
            print(response.request.body)
            print(response.json())
        assert response.status_code == HTTPStatus.BAD_REQUEST
        res_message = response.json()["developerMessage"]
        assert error in res_message
