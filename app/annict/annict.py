from typing import Dict
import requests
from datetime import datetime
from app.annict.query import QUERY_GET_PROGRAM, program_parse


class Annict:
    def __init__(self, config: Dict):
        self.token = config['token']
        self.endpoint = "https://api.annict.com/graphql"

    def get_record_target(self):
        headers = {"Authorization": f"bearer {self.token}"}
        response = requests.post(self.endpoint, params={"query": QUERY_GET_PROGRAM}, headers=headers)
        json_data = response.json()['data']['viewer']['programs']['edges']
        for node_obj in json_data:
            obj = program_parse(node_obj)
            if obj.start_at.timestamp() < datetime.utcnow().timestamp():
                continue
            yield obj
