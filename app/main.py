from app.annict.annict import Annict
from app.recorders.epgstation import EpgStation


def main():
    annict = Annict({"token": ""})
    recorders = EpgStation({"endpoint": ""})

    for t in annict.get_record_target():
        print(t.title, recorders.record_request(t))


if __name__ == '__main__':
    main()
