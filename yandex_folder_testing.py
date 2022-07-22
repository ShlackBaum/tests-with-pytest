import requests

token_numbers = "" #сюда нужно внести свой токен Я.диска
y_token = "OAuth " + token_numbers

def create_folder(folder_name):
    api_url = "https://cloud-api.yandex.net/v1/disk/resources"
    HEADERS = {"Authorization": y_token}
    PARAMS = {'path': folder_name}
    response = requests.put(api_url, headers=HEADERS, params=PARAMS)
    return response.status_code

def check_folder_created(folder_name):
    api_url = "https://cloud-api.yandex.net/v1/disk/resources"
    HEADERS = {"Authorization": y_token}
    PARAMS = {'path': "/"}
    response = requests.get(api_url, headers=HEADERS, params=PARAMS).json()
    folder_found = 0
    for file_name in response['_embedded']['items']:
        if folder_name == file_name['name']:
            folder_found = 1
    return folder_found

