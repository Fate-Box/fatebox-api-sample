import requests

def get_omikuji_result(name: str):
    # FastAPIサーバーのURL（適切に変更）
    base_url = "https://fate-box-api.onrender.com"
    
    # おみくじ結果を取得するAPIエンドポイントにリクエスト
    response = requests.get(f"{base_url}/omikuji/{name}")
    
    if response.status_code == 200:
        # レスポンスが成功した場合、結果を取得
        data = response.json()
        print(f"名前 : {data['name']}さん" + "\n" +  f"結果 : {data['divination']}")
        print("画像URL:", data['image_url'])
        
        # 画像URLから画像を取得する
        image_response = requests.get(f"{base_url}{data['image_url']}")
        if image_response.status_code == 200:
            # 画像を保存する
            with open(f"{data['name']}_omikuji_result.png", 'wb') as f:
                f.write(image_response.content)
            print("画像が保存されました。")
        else:
            print("画像の取得に失敗しました。")
    else:
        print("運勢の取得に失敗しました。", response.status_code, response.text)

get_omikuji_result("太郎")