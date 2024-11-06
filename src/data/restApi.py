import requests
import json


def restApi(path = "sorted_drivers",method = "get",params = {"page":1,}):
    # url = f"http://money.ipdisk.co.kr:800/YMS-api/ver1{path}.php"
    url = f"http://money.ipdisk.co.kr:18000/api/{path}"
    # url = f"http://127.0.0.1:8000/api/{path}"
    
    # print(url)
    # print(params)
    match method:
        case "get":
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print("Error Code:", response.status_code)
        case "post":
            response = requests.post(url, data=json.dumps(params))
            data = response.json()
            return data
        
