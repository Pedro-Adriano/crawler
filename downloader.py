import request

class Downloader:
    def __init__(self):
        self.session = requests.Session()

    def get(self, url, params=None, cookies=None):
        response = self.session.get(url, params= params, verify=False, cookies=cookies)
        response.raise_for_status

    def post(self, url, data=None, cookies=None):
        response = self.session.post(url, data=data, verify=False)
        response.raise_for_status
        return response

    def close(self):
        self.session.close()
