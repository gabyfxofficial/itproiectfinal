import pytest
from services import crud_service, report_service
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
    crud_service.add_user("Ana", "Pop", 25, "ana@mail.com", "CompanyA")
    crud_service.add_user("Ion", "Ionescu", 30, "ion@mail.com", "CompanyA")
    crud_service.add_user("Mara", "Marin", 40, "mara@mail.com", "CompanyB")

def test_generate_report():
    report = report_service.generate_report()
    companies = [row["company"] for row in report]
    assert "CompanyA" in companies
    assert "CompanyB" in companies
    for row in report:
        if row["company"] == "CompanyA":
            assert row["count"] == 2
        if row["company"] == "CompanyB":
            assert row["count"] == 1
