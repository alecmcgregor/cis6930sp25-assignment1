import argparse
import json
import sys
import requests

def download_url(url):
    page = requests.get(url)
    if page.status_code == 200:
        return page.json()
    else:
        print("Error, could not connect to the URL")
        return None

def download_file(file):
    if file is not None:
        download = open(file)
        return json.load(download)
    else:
        return None

def format_data(data, offset, limit):
    crimes = []
    for i in range(offset, offset+limit):
        incident_type = data[i].get("narrative", "")
        report_date = data[i].get("report_date", "")
        offense_date = data[i].get("offense_date", "")
        latitude = data[i].get("latitude", "")
        longitude = data[i].get("longitude", "")
        crimes.append([incident_type, report_date, offense_date, latitude, longitude])
    return crimes

def print_crimes(report):
    for i in range(len(report)):
        print(f"{report[i][0]}þ{report[i][1]}þ{report[i][2]}þ{report[i][3]}þ{report[i][4]}")

def main(url, file, offset, limit):
    if url is not None:
        data = download_url(url)
    elif file is not None:
        data = download_file(file)
    if data is not None:
        crimes = format_data(data, offset, limit)
        print_crimes(crimes)
    else:
        print("Error: no data to be read. Please enter a url or file.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, required=False, help="The source location on the web.")
    parser.add_argument("--file", type=str, required=False, help="The source location locally.")
    parser.add_argument("--offset", type=int, required=True, help="The offset to jump forward.")
    parser.add_argument("--limit", type=int, required=True, help="The number of records you want to retrive.")
    args = parser.parse_args()
    if args.url:
        main(args.url, None, args.offset, args.limit)
    elif args.file:
        main(None, args.file, args.offset, args.limit)
    else:
        parser.print_help(sys.stderr)

