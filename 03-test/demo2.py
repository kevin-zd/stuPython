import requests
import json

url = "https://ae-openapi.feishu.cn/api/data/v1/namespaces/package_dc6c63__c/meta/objects/list"
payload = "{\"filter\":{\"type\":\"custom\",\"quickQuery\":\"Sample Text\"},\"limit\":20,\"offset\":0}"
headers = {
  "Authorization": "T:f9ac7f6d04ff478ba2fc.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcHBJRCI6ImNfZDQ5NDE5MDZiOTJiNDk5MDkzMTEiLCJUZW5hbnROYW1lIjoiYXBhYXMiLCJUZW5hbnRLZXkiOiIiLCJUZW5hbnRJRCI6MzkwLCJFbnYiOiJvbmxpbmUiLCJBcHBUeXBlIjozLCJOYW1lc3BhY2UiOiJwYWNrYWdlX2RjNmM2M19fYyIsImF2ZXIiOiIiLCJzb3VyY2UiOiJwYWdlIiwiZXhwIjoxNjk0MjI2MDczMzQ1fQ.zYXIvHCuZAn0PfSr5xmjx40huPU6keVSvDympdblILo",
  "Content-Type": "application/json"
}

response = requests.request("POST", url, headers=headers, data=payload.encode('utf-8'))

print(response.text)