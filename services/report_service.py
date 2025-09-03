from database import get_connection
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io

def generate_report():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT company AS company,
               COUNT(*) AS user_count,
               AVG(age) AS avg_age
        FROM users
        GROUP BY company
    """)
    data = cur.fetchall()
    conn.close()
    return data

def generate_report_pdf():
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Titlu
    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, height - 50, "Company Report")

    # Header tabel
    p.setFont("Helvetica-Bold", 12)
    y = height - 100
    p.drawString(50, y, "Company")
    p.drawString(250, y, "User Count")
    p.drawString(400, y, "Average Age")
    y -= 20

    # Date
    p.setFont("Helvetica", 11)
    for row in generate_report():
        p.drawString(50, y, str(row["company"]))
        p.drawString(250, y, str(row["user_count"]))
        p.drawString(400, y, f"{row['avg_age']:.1f}")
        y -= 20
        if y < 50:  # pagină nouă dacă nu mai încape
            p.showPage()
            y = height - 50

    p.save()
    buffer.seek(0)
    return buffer
