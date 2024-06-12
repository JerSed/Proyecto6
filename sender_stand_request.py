import configuration
import requests
import data


def create_user_account(payload):
    response = requests.post(
        url=f"{configuration.URL_SERVICE}{configuration.CREATE_USER_PATH}",
        json=payload,
        headers=data.headers
    )
    return response


user_response = create_user_account(data.user_body)


def obtain_auth_token():
    response = create_user_account(data.user_body)
    response_data = response.json()
    return response_data['authToken']


def submit_new_client_kit(kit_payload):
    token = obtain_auth_token()
    headers = data.headers.copy()
    headers['Authorization'] = f'Bearer {token}'

    response = requests.post(
        url=f"{configuration.URL_SERVICE}{configuration.KITS_PATH}",
        json=kit_payload,
        headers=headers,
    )
    return response


kit_response = submit_new_client_kit(["one_character"])


print(kit_response.status_code)