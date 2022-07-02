from unittest import result
import requests
result = requests.get("https://mocki.io/v1/9ccc0559-f08c-438c-95c0-82bb6363f037")
# print(result.status_code)
# print(result.text)

print(result.json())
