import pytest
from services import crud_service
from database.models import create_table
from database import get_connection

# Automatically runs before each test to prepare a clean database
@pytest.fixture(autouse=True)
def setup_db():
    create_table()                         # Ensure the table exists
    conn = get_connection()                 # Connect to the database
    cur = conn.cursor()
    cur.execute("DELETE FROM users")        # Clear all records before each test
    conn.commit()
    conn.close()

# Test adding a user and retrieving it from the database
def test_add_and_get_user():
    crud_service.add_user("Test", "User", 25, "test@example.com", "TestCorp")
    users = crud_service.get_all_users()    # Get all users after insertion
    assert len(users) == 1                  # Ensure one user was added
    assert users[0]["firstName"] == "Test"  # Validate inserted user's name

# Test updating an existing user's data
def test_update_user():
    crud_service.add_user("Old", "Name", 30, "old@mail.com", "Company")
    user = crud_service.get_all_users()[0]  # Retrieve inserted user
    crud_service.update_user(user["id"], "New", "Name", 28, "new@mail.com", "NewCo")
    updated = crud_service.get_user(user["id"])  # Get updated user
    assert updated["firstName"] == "New"   # Verify name change
    assert updated["age"] == 28            # Verify age change

# Test deleting a user from the database
def test_delete_user():
    crud_service.add_user("Delete", "Me", 20, "del@mail.com", "Company")
    user = crud_service.get_all_users()[0]  # Retrieve inserted user
    crud_service.delete_user(user["id"])    # Delete the user
    users = crud_service.get_all_users()    # Fetch all users again
    assert len(users) == 0                  # Ensure user was removed
