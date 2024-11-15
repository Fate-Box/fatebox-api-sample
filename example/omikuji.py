import requests

# APIのベースURL
BASE_URL = "https://fate-box-api.onrender.com"

# 画像のベースURL
IMAGE_BASE_URL = f"{BASE_URL}/"

# おみくじ結果を取得する関数
def get_omikuji_result(name: str):
    # おみくじAPIのURL
    api_url = f"{BASE_URL}/omikuji/{name}"

    # GETリクエストで占い結果を取得
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        name = data.get("name")  # 名前
        divination = data.get("divination")  # 運勢
        image_url = data.get("image_url")  # 画像の相対URL

        print(f"名前: {name}")
        print(f"運勢: {divination}")
        print(f"画像URL: {image_url}")

        # 完全な画像URLを作成（2重スラッシュを防ぐ）
        full_image_url = IMAGE_BASE_URL + image_url.lstrip('/')

        # 画像を保存
        download_image(full_image_url, name, divination)
    else:
        print(f"HTTPエラーが発生しました: {response.status_code}")

# 画像をダウンロードして保存する関数
def download_image(image_url: str, name: str, divination: str):
    # 画像リクエスト
    image_response = requests.get(image_url)

    if image_response.status_code == 200:
        # 保存するファイル名（名前と運勢を使用）
        filename = f"{name}_{divination}.png"

        # 画像をローカルに保存
        with open(filename, 'wb') as f:
            f.write(image_response.content)

        print(f"画像 {filename} が保存されました。")
    else:
        print(f"画像の取得に失敗しました: {image_response.status_code}, URL: {image_url}")

# 名前を指定して占い結果を取得
name = "kayu0514"  # ここに名前を指定
get_omikuji_result(name)
