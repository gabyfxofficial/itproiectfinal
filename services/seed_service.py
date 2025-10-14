import requests
from services import crud_service

def seed_users_from_api():
    url = "https://dummyjson.com/users"
    try:
        response = requests.get(url, timeout=10)
    except Exception as e:
        print("❌ Error fetching API:", e)
        return

    if response.status_code == 200:
        payload = response.json()
        data = payload.get("users", [])
        count = 0

        for user in data:
            addr = user.get("address", {}) or {}
            company = user.get("company", {}) or {}
            bank = user.get("bank", {}) or {}

            crud_service.add_user(
                firstName=user.get("firstName", ""),
                lastName=user.get("lastName", ""),
                age=int(user.get("age", 0)),
                email=user.get("email", ""),
                company=company.get("name", ""),
                phone=user.get("phone", ""),
                iban=bank.get("iban", ""),
                country=addr.get("country", ""),
                address_street=addr.get("address", ""),
                address_city=addr.get("city", ""),
                address_state=addr.get("state", ""),
                address_postal=addr.get("postalCode", ""),
                role=user.get("role", "user")
            )
            count += 1
        print(f"✅ Inserted {count} users from API")
    else:
        print(f"❌ Failed to fetch data (status {response.status_code})")
