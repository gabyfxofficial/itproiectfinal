import pytest
from services import crud_service
from database.models import create_table
from database import get_connection

@pytest.fixture(autouse=True)
def setup_db():
    create_table()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users")  # curățăm DB
    conn.commit()
    conn.close()

def test_add_and_get_user():
    crud_service.add_user("Test", "User", 25, "test@example.com", "TestCorp")
    users = crud_service.get_all_users()
    assert len(users) == 1
    assert users[0]["firstName"] == "Test"

def test_update_user():
    crud_service.add_user("Old", "Name", 30, "old@mail.com", "Company")
    user = crud_service.get_all_users()[0]
    crud_service.update_user(user["id"], "New", "Name", 28, "new@mail.com", "NewCo")
    updated = crud_service.get_user(user["id"])
    assert updated["firstName"] == "New"
    assert updated["age"] == 28

def test_delete_user():
    crud_service.add_user("Delete", "Me", 20, "del@mail.com", "Company")
    user = crud_service.get_all_users()[0]
    crud_service.delete_user(user["id"])
    users = crud_service.get_all_users()
    assert len(users) == 0
