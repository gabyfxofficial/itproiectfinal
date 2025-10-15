import pytest
from services import crud_service, report_service
from database.models import create_table
from database import get_connection

# Automatically runs before each test to prepare a clean and consistent database
@pytest.fixture(autouse=True)
def setup_db():
    create_table()                           # Ensure the users table exists
    conn = get_connection()                   # Connect to the database
    cur = conn.cursor()
    cur.execute("DELETE FROM users")          # Clear previous records
    conn.commit()
    conn.close()

    # Insert sample users for the report test
    crud_service.add_user("Ana", "Pop", 25, "ana@mail.com", "CompanyA")
    crud_service.add_user("Ion", "Ionescu", 30, "ion@mail.com", "CompanyA")
    crud_service.add_user("Mara", "Marin", 40, "mara@mail.com", "CompanyB")

# Test that the generated report contains the correct data
def test_generate_report():
    report = report_service.generate_report()      # Generate report data from database
    companies = [row["company"] for row in report] # Extract all company names

    # Ensure both companies appear in the report
    assert "CompanyA" in companies
    assert "CompanyB" in companies

    # Verify user counts for each company
    for row in report:
        if row["company"] == "CompanyA":
            assert row["count"] == 2               # CompanyA should have 2 users
        if row["company"] == "CompanyB":
            assert row["count"] == 1               # CompanyB should have 1 user
