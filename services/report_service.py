from database import get_connection
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io

# Generate summarized report data grouped by company
def generate_report():
    conn = get_connection()   # Connect to the database
    cur = conn.cursor()
    cur.execute("""
        SELECT company AS company,
               COUNT(*) AS user_count,
               AVG(age) AS avg_age
        FROM users
        GROUP BY company
    """)
    data = cur.fetchall()     # Fetch the grouped results
    conn.close()              # Close the database connection
    return data

# Generate a PDF version of the company report
def generate_report_pdf():
    buffer = io.BytesIO()                     # Create an in-memory buffer for PDF data
    p = canvas.Canvas(buffer, pagesize=A4)    # Create a PDF canvas
    width, height = A4                        # Get A4 page dimensions

    # Title
    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, height - 50, "Company Report")

    # Table header
    p.setFont("Helvetica-Bold", 12)
    y = height - 100
    p.drawString(50, y, "Company")
    p.drawString(250, y, "User Count")
    p.drawString(400, y, "Average Age")
    y -= 20

    # Table data
    p.setFont("Helvetica", 11)
    for row in generate_report():
        p.drawString(50, y, str(row["company"]))        # Company name
        p.drawString(250, y, str(row["user_count"]))    # Number of users
        p.drawString(400, y, f"{row['avg_age']:.1f}")   # Average age (1 decimal)
        y -= 20
        # Create a new page if there's not enough space left
        if y < 50:
            p.showPage()
            y = height - 50

    p.save()                    # Finalize the PDF
    buffer.seek(0)              # Move the buffer cursor to the start
    return buffer               # Return the generated PDF buffer
