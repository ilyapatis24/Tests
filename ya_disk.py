import requests

TOKEN_YADISK = 'AQAAAAA1ivJ_AADLW35kQMDXaUjhnDt5hNRT5Ck'
MKDIR_URL = 'https://cloud-api.yandex.net:443/v1/disk/resources'


def create_folder(folder):
    params = {'path': folder}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN_YADISK}
    create_dir = requests.api.put(MKDIR_URL, headers=headers, params=params)
    return create_dir.status_code


def delete_folder(folder):
    params = {'path': folder}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN_YADISK}
    create_dir = requests.api.delete(MKDIR_URL, headers=headers, params=params)
    return create_dir.status_code