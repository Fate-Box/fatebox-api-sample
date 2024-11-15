import requests

# APIのベースURL
BASE_URL = "https://fate-box-api.onrender.com"

# 画像のベースURL
IMAGE_BASE_URL = f"{BASE_URL}/"

# 星座占いの結果を取得する関数
def get_constellation_result(constellation: str):
    # 星座占いAPIのURL
    api_url = f"{BASE_URL}/constellation/{constellation}"

    # GETリクエストで星座占いの結果を取得
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        sign = data.get("sign")  # 星座名
        rank = data.get("rank")  # ランキング
        rank_message = data.get("rank_message")  # コメント
        image_url = data.get("image_url")  # 画像の相対URL

        # 結果を表示
        print(f"星座: {sign}")
        print(f"ランク: {rank}")
        print(f"コメント: {rank_message}")
        print(f"画像URL: {image_url}")

        # 完全な画像URLを作成（余分なスラッシュを防ぐ）
        full_image_url = IMAGE_BASE_URL + image_url.lstrip('/')
        print(f"画像の完全URL: {full_image_url}")

        # 画像を保存
        download_image(full_image_url, sign, rank)
    else:
        # エラーが発生した場合の処理
        print(f"HTTPエラーが発生しました: {response.status_code}")
        print(f"エラーメッセージ: {response.text}")

# 画像をダウンロードして保存する関数
def download_image(image_url: str, sign: str, rank: int):
    # 画像リクエスト
    image_response = requests.get(image_url)

    if image_response.status_code == 200:
        # 保存するファイル名（星座名とランクを使用）
        filename = f"{sign}_{rank}.png"

        # 画像をローカルに保存
        try:
            with open(filename, 'wb') as f:
                f.write(image_response.content)
            print(f"画像 {filename} が保存されました。")
        except Exception as e:
            print(f"画像の保存中にエラーが発生しました: {str(e)}")
    else:
        print(f"画像の取得に失敗しました: {image_response.status_code}, URL: {image_url}")

# 星座を指定して占い結果を取得
constellation = "かに座"  # ここに占いたい星座名を指定
get_constellation_result(constellation)
