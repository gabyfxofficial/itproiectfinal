from database import get_connection

def sort_by_name():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users ORDER BY firstName ASC")
    data = cur.fetchall()
    conn.close()
    return data

def sort_by_age():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users ORDER BY age DESC")
    data = cur.fetchall()
    conn.close()
    return data

def filter_by_company(company: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE company LIKE ?", (f"%{company}%",))
    data = cur.fetchall()
    conn.close()
    return data
