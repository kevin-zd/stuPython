import requests
import json
import pandas as pd


url = "https://ae-openapi.feishu.cn/auth/v1/appToken"
payload = "{\"clientId\":\"c_ccefda14ba224697b221\",\"clientSecret\":\"ba079a6761154007b2b8e19c5976533e\"}"
headers = {
  "Content-Type": "application/json"
}

response = requests.request("POST", url, headers=headers, data=payload.encode('utf-8'))

accessToken = response.json()['data']['accessToken']

url = "https://ae-openapi.feishu.cn/v1/data/namespaces/package_copyaadeg25s6kql2__c/objects/_user/records_query"

items = []
off = 0
while True:
    payload = {
        "page_token": "",
        "page_size": 500,
        "select": ["_id", "_name","_email","_department","_id","_type","_manager","_id"],
        "filter": None,
        "order_by": [{"field": "_createdAt", "direction": "desc"}],
        "offset": off
    }
    headers = {
    "Authorization": accessToken,
    "Content-Type": "application/json"
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload).encode('utf-8'))

    segs = response.json()['data']['items']
    for seg in segs:
        items.append(seg)
    if len(segs) == 0:
        break
    off += 500
print(items)

# 将结果转换为JSON格式
result_json = json.dumps(items)

# 创建DataFrame对象
df = pd.read_json(result_json)

# 将DataFrame写入Excel文件
df.to_excel('output.xlsx', index=False)