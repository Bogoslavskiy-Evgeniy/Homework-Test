import requests


class New_folder_yandex_disc:

    def __init__(self, token_yandex):
        self.token_yandex = token_yandex
        self.path = f'/Test'
        self.upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        self.headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token_yandex)}
        self.params = {'path': self.path}


    def create_folder(self):
        resp = requests.put(self.upload_url, headers=self.headers, params=self.params)
        return resp.status_code

    def delete_folder(self):
        requests.delete(self.upload_url, headers=self.headers, params=self.params)

    def get_folder(self):
        resp = requests.get(self.upload_url, headers=self.headers, params=self.params)
        return resp.status_code

token_yandex = ....
new_folder = New_folder_yandex_disc(token_yandex)






