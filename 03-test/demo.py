import requests
import json

url = "https://ae-openapi.feishu.cn/api/data/v1/namespaces/package_dc6c63__c/objects/object_57fdf8734d9/records"
payload = "{\"filter\":[{\"or\":[{\"leftValue\":\"_name\",\"operator\":\"contain\",\"rightValue\":\"测试\"},{\"leftValue\":\"_createdAt\",\"operator\":\"gte\",\"rightValue\":1503763200000}]}],\"sort\":[{\"field\":\"_createdAt\",\"direction\":\"desc\"}],\"limit\":100,\"offset\":0,\"count\":false,\"fields\":[\"_id\",\"_name\"],\"quickSearch\":\"Sample text\"}"
headers = {
  "Authorization": "T:f9ac7f6d04ff478ba2fc.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcHBJRCI6ImNfZDQ5NDE5MDZiOTJiNDk5MDkzMTEiLCJUZW5hbnROYW1lIjoiYXBhYXMiLCJUZW5hbnRLZXkiOiIiLCJUZW5hbnRJRCI6MzkwLCJFbnYiOiJvbmxpbmUiLCJBcHBUeXBlIjozLCJOYW1lc3BhY2UiOiJwYWNrYWdlX2RjNmM2M19fYyIsImF2ZXIiOiIiLCJzb3VyY2UiOiJwYWdlIiwiZXhwIjoxNjk0MjI2MDczMzQ1fQ.zYXIvHCuZAn0PfSr5xmjx40huPU6keVSvDympdblILo",
  "Content-Type": "application/json"
}

response = requests.request("POST", url, headers=headers, data=payload.encode('utf-8'))

print(response.text)