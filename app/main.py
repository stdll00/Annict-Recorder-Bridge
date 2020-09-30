from app.annict.annict import Annict
from app.recorders.epgstation import EpgStation
import os


def get_config():
    annict_conf = dict()
    annict_conf['token'] = os.getenv("annict_token")
    recorder_conf = dict()
    recorder_conf['endpoint'] = os.getenv("endpoint", "http://localhost")

    return annict_conf, recorder_conf


def main():
    annict_conf, recorder_conf = get_config()
    annict = Annict(annict_conf)
    recorder = EpgStation(recorder_conf)

    for t in annict.get_record_target():
        print(t.title, recorder.record_request(t))


if __name__ == '__main__':
    main()
