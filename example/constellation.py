import requests

# 名前を入れる
constellation = "かに座"

# API
api = f"https://fate-box-api.onrender.com/constellation/{constellation}"

req = requests.get(api)

if req.status_code == 200:
    data = req.json()
    sign = data["sign"]
    rank = data["rank"]
    rank_message = data["rank_message"]

    print(f"星座 : {sign}\nランク : {rank}\nコメント : {rank_message}")
else:
    print(f"HTTPエラーが発生しました: {req.status_code}")