import requests

# Geocoding APIを使って地点名から緯度・経度を取得する関数
def geocode(api_key, location_name):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        'address': location_name,
        'key': api_key
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            # 緯度・経度を返す
            lat = data['results'][0]['geometry']['location']['lat']
            lng = data['results'][0]['geometry']['location']['lng']
            return lat, lng
        else:
            return None, f"Geocoding API error: {data['status']}"
    else:
        return None, f"Error: {response.status_code}"

# Distance Matrix APIを使って距離を計算する関数
def get_distance(api_key, origin, destination):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    
    # 出発地点と到着地点の緯度・経度を文字列として指定
    params = {
        'origins': f"{origin[0]},{origin[1]}",  # 出発地点の緯度・経度
        'destinations': f"{destination[0]},{destination[1]}",  # 到着地点の緯度・経度
        'key': api_key,  # APIキー
        'mode': 'walking',  # 徒歩での移動
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        try:
            distance = data['rows'][0]['elements'][0]['distance']['text']
            duration = data['rows'][0]['elements'][0]['duration']['text']
            return distance, duration
        except KeyError:
            return None, "Error: Response format is invalid."
    else:
        return None, f"Error: {response.status_code}"

# メイン処理
def main():
    api_key = "AIzaSyAE9B6ZoRbQznWFlJRDQFcaUjyZ7lXi0W8"  # 取得したAPIキーを入力

    # ユーザーから出発地点と到着地点の名前を入力
    origin_name = input("出発地点の名前を入力してください: ")
    destination_name = input("到着地点の名前を入力してください: ")
    
    # 出発地点と到着地点の緯度・経度を取得
    origin_lat, origin_lng = geocode(api_key, origin_name)
    if origin_lat is None:
        print(f"出発地点のエラー: {origin_lng}")
        return

    destination_lat, destination_lng = geocode(api_key, destination_name)
    if destination_lat is None:
        print(f"到着地点のエラー: {destination_lng}")
        return

    # 距離と所要時間を計算
    distance, duration = get_distance(api_key, (origin_lat, origin_lng), (destination_lat, destination_lng))
    
    if distance:
        print(f"出発地点: {origin_name}")
        print(f"到着地点: {destination_name}")
        print(f"距離: {distance}")
        print(f"所要時間: {duration}")
    else:
        print(f"距離計算エラー: {duration}")

if __name__ == "__main__":
    main()
