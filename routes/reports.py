from flask import Blueprint, render_template, send_file
from services.report_service import generate_report, generate_report_pdf

# Create a Blueprint for handling report-related routes
reports_bp = Blueprint("reports", __name__, template_folder="../templates/reports")

@reports_bp.route("/")
def report():
    # Generate report data using the service function
    data = generate_report()
    # Render the report page and pass the data to the template
    return render_template("reports/report.html", data=data)

@reports_bp.route("/download")
def download_report():
    # Generate the report in PDF format
    pdf_buffer = generate_report_pdf()
    # Send the generated PDF as a downloadable file
    return send_file(
        pdf_buffer,
        as_attachment=True,           # Force download
        download_name="company_report.pdf",  # Name of the downloaded file
        mimetype="application/pdf"    # Specify file type
    )
