from database import get_connection

def add_user(firstName: str, lastName: str, age: int, email: str, company: str) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (firstName,lastName,age,email,company) VALUES (?,?,?,?,?)",
                (firstName, lastName, age, email, company))
    conn.commit()
    conn.close()

def get_all_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_user(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id=?", (user_id,))
    row = cur.fetchone()
    conn.close()
    return row

def update_user(user_id: int, firstName: str, lastName: str, age: int, email: str, company: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET firstName=?, lastName=?, age=?, email=?, company=? WHERE id=?",
                (firstName, lastName, age, email, company, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
