from typing import Dict
import requests
from datetime import datetime
from app.annict.query import QUERY_GET_PROGRAM, program_parse


class Annict:
    def __init__(self, config: Dict):
        self.token = config['token']
        self.endpoint = "https://api.annict.com/graphql"  # TODO fix

    def get_record_target(self):
        headers = {"Authorization": f"bearer {self.token}"}
        response = requests.post(self.endpoint, params={"query": QUERY_GET_PROGRAM}, headers=headers)
        json_data = response.json()['data']['viewer']['programs']['edges']
        for node_obj in json_data:
            obj = program_parse(node_obj)
            if obj.start_at.timestamp() < datetime.utcnow().timestamp():
                continue
            yield obj


if __name__ == '__main__':
    print(list(Annict({"token": "7Vt5sEE2scAZeYm5H6y3e7NAQimeblGfpRS5T3r4v2g"}).get_record_target()))
