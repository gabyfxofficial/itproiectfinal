import requests
from services import crud_service

def seed_users_from_api():
    url = "https://dummyjson.com/users"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get("users", [])
        for user in data:
            crud_service.add_user(
                user["firstName"],
                user["lastName"],
                int(user["age"]),
                user["email"],
                user["company"]["name"]
            )
        print(f"Inserted {len(data)} users from API")
    else:
        print("❌ Failed to fetch data from API")
