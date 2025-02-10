import argparse
import json
import sys
import urllib.request

#Function to download json data from a url provided to us by Dr.Grant
def fetchdata(url, isjson=True):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'https://www.google.com/',
        'DNT': '1',  # Do Not Track request header
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
    }


    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        data = response.read().decode('utf-8')
        if isjson:
            return json.loads(data)
        else:
            return data

#Function to download the url and return it's contents
def download_url(url):
    data = fetchdata(url)
    return data

#Function to download a local json file and return it's contents if it exists
def download_file(file):
    if file is not None:
        download = open(file)
        return json.load(download)
    else:
        return None

#Function to reurn desired elements of incident type, report date, offense date, latitude, and longitude, in a list format
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

#Function to print out the crimes with their information being seperated by thorns
def print_crimes(report):
    for i in range(len(report)):
        print(f"{report[i][0]}þ{report[i][1]}þ{report[i][2]}þ{report[i][3]}þ{report[i][4]}")

#Main function to run all of the previous functions cohesively
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

#Will recieve the user inputs as arguments and pass them into the main function if enough arguments are provided otherwise it will print help
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

