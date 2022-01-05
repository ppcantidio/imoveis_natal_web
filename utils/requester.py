import json
import requests

class Requester:
    def __init__(self, rota):
        self.rota = rota
        
    def get(self, endpoint, headers=None, params=None):
        req = requests.get(
            url=f'http://127.0.0.1:5000/api/{self.rota}/{endpoint}',
            headers=headers,
            params=params
            )

        return req

    def post(self, endpoint, headers=None, data=None):
        req = requests.post(
            url=f'http://127.0.0.1:5000/api/{self.rota}/{endpoint}',
            headers=headers,
            data=data
            )

        return req

