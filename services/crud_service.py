from database import get_connection
from typing import List, Dict, Any, Optional

def add_user(firstName: str, lastName: str, age: int, email: str, company: str,
             phone: str = "", iban: str = "", country: str = "",
             address_street: str = "", address_city: str = "",
             address_state: str = "", address_postal: str = "",
             role: str = "") -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO users (
            firstName, lastName, age, email, company,
            phone, iban, country, address_street, address_city,
            address_state, address_postal, role
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (firstName, lastName, age, email, company,
          phone, iban, country, address_street, address_city,
          address_state, address_postal, role))
    conn.commit()
    conn.close()

def get_all_users() -> List[Dict[str, Any]]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_user(user_id: int) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id=?", (user_id,))
    row = cur.fetchone()
    conn.close()
    return row

def update_user(user_id: int, firstName: str, lastName: str, age: int, email: str, company: str,
                phone: str = "", iban: str = "", country: str = "",
                address_street: str = "", address_city: str = "",
                address_state: str = "", address_postal: str = "",
                role: str = "") -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE users SET
            firstName=?, lastName=?, age=?, email=?, company=?,
            phone=?, iban=?, country=?, address_street=?, address_city=?,
            address_state=?, address_postal=?, role=?
        WHERE id=?
    """, (firstName, lastName, age, email, company,
          phone, iban, country, address_street, address_city,
          address_state, address_postal, role, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id: int) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
