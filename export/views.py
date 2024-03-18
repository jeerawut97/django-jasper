import os
from io import BytesIO
from django.http import FileResponse
from pyreportjasper import PyReportJasper
from django.shortcuts import render


def json_to_pdf(title="FooKCompany"):
    RESOURCES_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'resources')
    REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports')
    input_file = os.path.join(REPORTS_DIR, 'Blank_A4.jrxml')
    output_file = os.path.join(RESOURCES_DIR, 'Blank_A4.pdf')
    json_filename = 'data.json'
    json_file = os.path.join(REPORTS_DIR, json_filename)
    parameters = {"Title": title}
    conn = {
        'driver': 'json',
        'data_file': json_file
    }

    pyreportjasper = PyReportJasper()
    pyreportjasper.config(
        input_file,
        output_file,
        parameters=parameters,
        output_formats=["pdf"],
        db_connection=conn
    )
    pyreportjasper.process_report()
    return output_file

def pdf_to_buffer(pdf_file_path):
    with open(pdf_file_path, "rb") as f:
        return BytesIO(f.read())

def index(request):
    context = {}
    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get("title", "Ex.Topic")
        buffer = pdf_to_buffer(json_to_pdf(title))
        return FileResponse(buffer, as_attachment=True, filename='helloworld-jasper.pdf')

    return render(request, 'index.html', context)
