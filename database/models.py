from database import get_connection

def create_table():
    """
    Create users table with extended fields:
    phone, iban, country, address_street, address_city,
    address_state, address_postal, role
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstName TEXT,
            lastName TEXT,
            age INTEGER,
            email TEXT,
            company TEXT,
            phone TEXT,
            iban TEXT,
            country TEXT,
            address_street TEXT,
            address_city TEXT,
            address_state TEXT,
            address_postal TEXT,
            role TEXT
        )
    """)
    conn.commit()
    conn.close()
