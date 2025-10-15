from database import get_connection

# Sort users alphabetically by their first name (A → Z)
def sort_by_name():
    conn = get_connection()             # Connect to the database
    cur = conn.cursor()                 # Create a cursor for executing SQL commands
    cur.execute("SELECT * FROM users ORDER BY firstName ASC")
    data = cur.fetchall()               # Fetch all sorted results
    conn.close()                        # Close the connection
    return data

# Sort users by age in descending order (oldest → youngest)
def sort_by_age():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users ORDER BY age DESC")
    data = cur.fetchall()
    conn.close()
    return data

# Filter users by company name (case-insensitive partial match)
def filter_by_company(company: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE company LIKE ?", (f"%{company}%",))
    data = cur.fetchall()               # Fetch all matching users
    conn.close()
    return data
