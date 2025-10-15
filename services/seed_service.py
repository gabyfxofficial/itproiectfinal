import requests
from services import crud_service

# Fetch and insert users from the external API into the local database
def seed_users_from_api():
    url = "https://dummyjson.com/users"  # Public API providing dummy user data
    try:
        response = requests.get(url, timeout=10)  # Send a GET request with timeout
    except Exception as e:
        print("❌ Error fetching API:", e)
        return  # Stop execution if an error occurs during the request

    # Check if the request was successful
    if response.status_code == 200:
        payload = response.json()          # Convert response to JSON
        data = payload.get("users", [])    # Extract the "users" list
        count = 0                          # Counter for inserted users

        # Loop through each user in the API data
        for user in data:
            addr = user.get("address", {}) or {}   # Address details
            company = user.get("company", {}) or {} # Company info
            bank = user.get("bank", {}) or {}       # Bank details

            # Insert each user into the local database
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
            count += 1  # Increase the counter for each inserted user

        # Print confirmation message with total count
        print(f"✅ Inserted {count} users from API")
    else:
        # Print error message if API call fails
        print(f"❌ Failed to fetch data (status {response.status_code})")
