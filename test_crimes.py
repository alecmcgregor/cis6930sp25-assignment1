import pytest
import main
import json
import io
import sys

file = "crime_data.json"

url = "https://data.cityofgainesville.org/resource/gvua-xt9q.json"

simulated_data = [{"narrative":"Bank Robbery","report_date":"02-9-2010","offense_date":"02-8-2010","latitude":"fake numbers","longitude":"more fake numbers"},
                      {"narrative":"Theft","report_date":"02-17-2010","offense_date":"02-16-2010","latitude":"numbers","longitude":"2"},
                      {"narrative":"Failed an Exam","report_date":"02-12-2025","offense_date":"02-11-2025","latitude":"0","longitude":"0"},
                      {"narrative":"Did great on hw","report_date":"02-14-2025","offense_date":"02-11-2025","latitude":"100","longitude":"100"}]

def test_download_url():
    page = main.download_url(url)
    assert page is not None

def test_download_file():
    download = main.download_file(file)
    assert download is not None

def test_offset_limit():
    offset = 1
    limit = 2
    simulation = main.format_data(simulated_data, offset, limit)
    expectation = [["Theft", "02-17-2010", "02-16-2010", "numbers", "2"], ["Failed an Exam", "02-12-2025", "02-11-2025", "0", "0"]]
    assert simulation == expectation

def test_incident_type():
    offset = 0
    limit = 4
    simulation = main.format_data(simulated_data, offset, limit)
    expectation = ["Bank Robbery", "Theft", "Failed an Exam", "Did great on hw"]
    for i in range(4):
        assert simulation[i][0] == expectation[i]

def test_report_offense():
    offset = 1
    limit = 2
    simulation = main.format_data(simulated_data, offset, limit)
    expectation = [["Theft", "02-17-2010", "02-16-2010", "numbers", "2"], ["Failed an Exam", "02-12-2025", "02-11-2025", "0", "0"]]
    for i in range(2):
        assert (simulation[i][1] == expectation[i][1]) and (simulation[i][2] == expectation[i][2])

def test_latitude_longitude():
    offset = 1
    limit = 2
    simulation = main.format_data(simulated_data, offset, limit)
    expectation = [["Theft", "02-17-2010", "02-16-2010", "numbers", "2"], ["Failed an Exam", "02-12-2025", "02-11-2025", "0", "0"]]
    for i in range(2):
        assert (simulation[i][3] == expectation[i][3]) and (simulation[i][4] == expectation[i][4])

def test_formatting():
    assessment = [["Theft", "02-17-2010", "02-16-2010", "numbers", "2"], ["Failed an Exam", "02-12-2025", "02-11-2025", "0", "0"]]
    statement = io.StringIO()
    sys.stdout = statement
    main.print_crimes(assessment)
    expectation = ("Theftþ02-17-2010þ02-16-2010þnumbersþ2\n" + "Failed an Examþ02-12-2025þ02-11-2025þ0þ0\n")
    sys.stdout = sys.__stdout__
    assert statement.getvalue() == expectation
