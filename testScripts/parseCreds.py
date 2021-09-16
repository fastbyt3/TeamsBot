import json
with open(".creds.json") as f:
    jsonObj = json.load(f)

# print(jsonObj)
print(f"Email: {jsonObj['email']}")
print(f"Password: {jsonObj['password']}")