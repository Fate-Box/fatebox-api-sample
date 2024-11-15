import requests

def get_constellation_result(constellation: str):
    # FastAPIサーバーのURL（適切に変更）
    base_url = "https://fate-box-api.onrender.com"
    
    # 星座占い結果を取得するAPIエンドポイントにリクエスト
    response = requests.get(f"{base_url}/constellation/{constellation}")
    
    if response.status_code == 200:
        # レスポンスが成功した場合、結果を取得
        data = response.json()
        print(f"{data['sign']}の運勢ランキング: {data['rank']}位")
        print("運勢メッセージ:", data['rank_message'])
        print("画像URL:", data['image_url'])
        
        # 画像URLから画像を取得する
        image_response = requests.get(f"{base_url}{data['image_url']}")
        if image_response.status_code == 200:
            # 画像を保存する
            with open(f"{data['sign']}_constellation_result.png", 'wb') as f:
                f.write(image_response.content)
            print("画像が保存されました。")
        else:
            print("画像の取得に失敗しました。")
    else:
        print("星座占いの取得に失敗しました。", response.status_code, response.text)

get_constellation_result("おひつじ座")