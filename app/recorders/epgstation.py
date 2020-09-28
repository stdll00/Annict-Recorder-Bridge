import unicodedata
from typing import Dict

from app.models.common_models import RecordRequest
from app.recorders.abst_recorder import RecorderABC
from difflib import SequenceMatcher
import requests


class EpgStation(RecorderABC):

    def __init__(self, config: Dict):
        super().__init__(config)
        url = f"{self.config['endpoint']}/api/schedule?type=GR"
        self.channels = list(
            map(lambda x: x['channel'], requests.get(url, stream=True).json()), )

    def convert_channel(self, channel_name: str):
        scores = [SequenceMatcher(None, channel_name, unicodedata.normalize("NFKD", d['name'])).ratio()
                  + unicodedata.normalize("NFKD", d['name']).count('1') * 0.01 for d in self.channels]
        return self.channels[scores.index(max(scores))]['id']

    def record_request(self, record_request: RecordRequest) -> bool:
        data = {
            "option": {},
            "encode": {
                "mode1": 0,
                "directory1": record_request.title,
                "delTs": True
            },
            "program": {
                "channelId": self.convert_channel(record_request.channel),
                "startAt": int(record_request.start_at.timestamp() * 1000),
                "endAt": int(record_request.end_at.timestamp() * 1000),
                "name": record_request.title,
                # TODO
                # "genre1": 0,
                # "genre2": 0,
            }
        }
        res = requests.post(f"{self.config['endpoint']}/api/reserves", json=data)
        return res.status_code == 201
