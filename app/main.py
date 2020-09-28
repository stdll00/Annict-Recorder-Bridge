from app.annict.annict import Annict
from app.models.common_models import RecordRequest
from app.recorders.epgstation import EpgStation
from datetime import datetime


def main():
    annict = Annict({"token": ""})
    recorders = EpgStation({"endpoint": ""})

    targets = (list(annict.get_record_target()))
    for t in targets:
        print(recorders.record_request(t))


if __name__ == '__main__':
    main()
