import requests

# 名前を入れる
name = "kayu0514"

# API
api = f"https://fate-box-api.onrender.com/omikuji/{name}"

req = requests.get(api)

if req.status_code == 200:
    data = req.json()
    names = data["name"]
    divi = data["divination"]

    print(f"名前 : {names}\n結果 : {divi}")
else:
    print(f"HTTPエラーが発生しました: {req.status_code}")