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
    # conn = {
    #     'driver': 'json',
    #     'data_file': json_file
    # }
    conn = {
      'driver': 'csv',
      'data_file': os.path.join(RESOURCES_DIR, 'csvExampleHeaders.csv'),
      'csv_charset': 'utf-8',
      'csv_out_charset': 'utf-8',
      'csv_field_del': '|',
      'csv_out_field_del': '|',
      'csv_record_del': "\r\n",
      'csv_first_row': True,
      'csv_columns': "Name,Street,City,Phone".split(",")
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
        with open(json_to_pdf(title), 'rb') as file:
            response = FileResponse(file)
            response['Content-Type'] = 'text/plain'
            response['Content-Disposition'] = 'attachment; filename="helloworld-jasper.pdf"'
            return response

    return render(request, 'index.html', context)
