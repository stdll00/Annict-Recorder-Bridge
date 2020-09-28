from app.annict.annict import Annict
from app.models.common_models import RecordRequest
from app.recorders.epgstation import EpgStation
from datetime import datetime


def main():
    annict = Annict({"token": "7Vt5sEE2scAZeYm5H6y3e7NAQimeblGfpRS5T3r4v2g"})
    recorders = EpgStation({"endpoint": "http://shinapuri.local"})

    targets = (list(annict.get_record_target()))
    for t in targets:
        print(recorders.record_request(t))


if __name__ == '__main__':
    main()
