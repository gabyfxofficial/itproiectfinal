import pytest
from services import crud_service, filter_service
from database.models import create_table
from database import get_connection

# Automatically runs before each test to set up a clean database with sample data
@pytest.fixture(autouse=True)
def setup_db():
    create_table()                           # Ensure the users table exists
    conn = get_connection()                   # Connect to the database
    cur = conn.cursor()
    cur.execute("DELETE FROM users")          # Clear all records before testing
    conn.commit()
    conn.close()

    # Insert sample users for testing
    crud_service.add_user("Alice", "Smith", 22, "alice@mail.com", "Tech")
    crud_service.add_user("Bob", "Brown", 35, "bob@mail.com", "Finance")
    crud_service.add_user("Charlie", "White", 29, "charlie@mail.com", "Tech")

# Test sorting users alphabetically by first name
def test_sort_by_name():
    users = filter_service.sort_by_name()     # Get users sorted by name
    names = [u["firstName"] for u in users]
    assert names == sorted(names)             # Verify sorting order is correct

# Test sorting users by age in descending order
def test_sort_by_age():
    users = filter_service.sort_by_age()      # Get users sorted by age (DESC)
    ages = [u["age"] for u in users]
    assert ages == sorted(ages, reverse=True) # Verify sorting order is correct

# Test filtering users by company name
def test_filter_by_company():
    users = filter_service.filter_by_company("Tech")  # Get users working in "Tech"
    companies = [u["company"] for u in users]
    assert all("Tech" in c for c in companies)        # Ensure all users belong to "Tech"
