from flask import Blueprint, render_template, send_file
from services.report_service import generate_report, generate_report_pdf

reports_bp = Blueprint("reports", __name__, template_folder="../templates/reports")

@reports_bp.route("/")
def report():
    data = generate_report()
    return render_template("reports/report.html", data=data)

@reports_bp.route("/download")
def download_report():
    pdf_buffer = generate_report_pdf()
    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name="company_report.pdf",
        mimetype="application/pdf"
    )
