# Annict Recorder Bridge
[Annict](https://annict.jp/) の放送予定を自動でEPGStationに送信します

# Get Started
AnnictユーザーかつEPGStationのみをサポート
```
pip3 install -r requierements.txt

python3 app/main.py
```
cronなどで定期的に実行してください

# TODO
- [x] Annictからの取得
- [x] 録画


- [ ] 録画詳細情報
- [ ] 重複削除
- [ ] 30分以外のアニメへの対応 (番組表とのマッチ?)
- [ ] EPGSationの詳細設定
