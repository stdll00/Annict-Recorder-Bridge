# Annict Recorder Bridge
[Annict](https://annict.jp/) の放送予定を自動でEPGStationに送信します

## Get Started
Annictユーザーかつ録画サーバーはEPGStationのみをサポート
```
pip3 install -r requierements.txt

python3 app/main.py
```
cronなどで定期的に実行してください

## NOTE
EPG Stationで録画する場合にルールとannictに重複があっても問題ありません。
録画ファイルが2個になりますがいい感じに処理されます

## TODO
- [x] Annictからの取得
- [x] 録画

(やりたい)
- [ ] 録画詳細情報
- [x] 重複録画抑制
- [ ] 30分以外のアニメへの対応 (番組表とのマッチ?)
- [ ] EPGSationの詳細設定
- [ ] 環境変数サポート
- [ ] Test

(やる気がない)
- [ ] Chinachuやその他の録画機器サポート
- [ ] Annict以外のサポート
- [ ] DBを持って諸々の管理
