import pytest
from services import crud_service, filter_service
from database.models import create_table
from database import get_connection

@pytest.fixture(autouse=True)
def setup_db():
    create_table()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users")
    conn.commit()
    conn.close()
    crud_service.add_user("Alice", "Smith", 22, "alice@mail.com", "Tech")
    crud_service.add_user("Bob", "Brown", 35, "bob@mail.com", "Finance")
    crud_service.add_user("Charlie", "White", 29, "charlie@mail.com", "Tech")

def test_sort_by_name():
    users = filter_service.sort_by_name()
    names = [u["firstName"] for u in users]
    assert names == sorted(names)

def test_sort_by_age():
    users = filter_service.sort_by_age()
    ages = [u["age"] for u in users]
    assert ages == sorted(ages, reverse=True)

def test_filter_by_company():
    users = filter_service.filter_by_company("Tech")
    companies = [u["company"] for u in users]
    assert all("Tech" in c for c in companies)
