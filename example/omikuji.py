import requests

# FastAPIサーバーのベースURL
BASE_URL = "https://fate-box-api.onrender.com"

def fetch_omikuji(name: str):
    """おみくじAPIから結果を取得する"""
    try:
        response = requests.get(f"{BASE_URL}/omikuji/{name}")
        response.raise_for_status()  # エラーがある場合は例外を発生
        data = response.json()
        print(f"名前: {data['name']}")
        print(f"おみくじ結果: {data['divination']}")
        print(f"画像URL: {data['image_url']}")
        return data
    except requests.exceptions.RequestException as e:
        print(f"おみくじAPIの取得に失敗しました: {e}")
        return None

def fetch_image(image_url: str, save_path: str):
    """画像を取得して保存する"""
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"画像を保存しました: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"画像の取得に失敗しました: {e}")

def main():
    # ユーザー名を入力
    name = input("名前を入力してください: ")

    # おみくじ結果を取得
    result = fetch_omikuji(name)
    if result:
        image_url = result['image_url']
        save_path = f"{name}_result.png"  # 保存先のファイル名
        # 画像を取得して保存
        fetch_image(image_url, save_path)

if __name__ == "__main__":
    main()
