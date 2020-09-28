from abc import ABC, abstractmethod
from typing import Dict

from app.models.common_models import RecordRequest


class RecorderABC(ABC):
    def __init__(self, config: Dict):
        self.config: Dict = config
        # TODO validator

    @abstractmethod
    def record_request(self, record_request: RecordRequest) -> bool:
        """
        :return: True if success else False
        """
        pass
