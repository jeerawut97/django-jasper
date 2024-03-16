import os, json, uuid
from pyreportjasper import PyReportJasper
from django.shortcuts import render
from django.conf import settings


def json_to_pdf():
    RESOURCES_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'resources')
    REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports')
    input_file = os.path.join(REPORTS_DIR, 'Blank_A4_Landscape.jrxml')
    output_file = os.path.join(REPORTS_DIR, 'Blank_A4_Landscape.pdf')

    generate_utils_dir = os.path.join(settings.BASE_DIR, 'export', 'generate')
    if not os.path.exists(generate_utils_dir):
        os.mkdir(generate_utils_dir)

    parameters = {"title": "TestTitle", "sub_title": "TestSubTitle"}
    json_obj = json.dumps({"data": {}}, indent=4, ensure_ascii=False)
    json_filename = str(uuid.uuid4().hex) + '.json'
    json_file = os.path.join(generate_utils_dir, json_filename)
    with open(json_file, "w") as outfile:
        outfile.write(json_obj)

    print(f"json_file: {json_file}")
    conn = {
        'driver': 'json',
        'data_file': json_file,
    }

    if output_file is None:
        output_file = os.path.join(generate_utils_dir, str(uuid.uuid4().hex))

    pyreportjasper = PyReportJasper()
    pyreportjasper.config(
        input_file,
        output_file,
        parameters=parameters,
        output_formats=["pdf"],
        db_connection=conn
    )
    pyreportjasper.process_report()

def index(request):
    rs = json_to_pdf()
    print(f"rs: {rs}")
    context = {}
    return render(request, 'index.html', context)
