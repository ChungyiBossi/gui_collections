import requests
import json
from KEYS import WEATHER_OPENDATA  # 可以把你的授權統一控管在KEYS檔案內

url = f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001'
header = {
    'Authorization': WEATHER_OPENDATA  # 作為資訊帶入到header
}
data = requests.get(url, headers=header)
print('Response Code: ', data)
data_json = data.json()    # 轉換成 JSON 格式
with open('api_data.json', 'w') as data:
    json.dump(data_json, data, indent=4)
