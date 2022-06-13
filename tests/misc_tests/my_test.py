import os
import requests
from http.client import responses

print(requests.codes.ok)
print()

messages = requests.status_codes._codes[403]
print(messages[0])
print()

print(responses[403])

# print("1")
# try:
#     os.remove("filename")
# except Exception as e:
#     pass
# print("2")
