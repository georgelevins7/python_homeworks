import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()

def inf(user_id):
    for user in data:
        if user["id"] == user_id:
            return {
                "name": user["name"],
                "email": user["email"],
                "city": user["address"]["city"],
                "company": user["company"]["name"]
            }

    if user_id != user["id"]:
        return None
print(inf(5))
print(inf(-5))
print(inf(55))