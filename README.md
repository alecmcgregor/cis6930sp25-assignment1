# cis6930sp25-assignment1

Name: Alec McGregor

## Assignment Description

This assignment was to create a python function that can collect elements from the Crime Respones API and output the information into a specific format using thorns to seperate the data. Additionally, functionality tests were created to ensure that all parts of the code worked as intended.

## How to install

pipenv install -e .

## How to run

pipenv run python main.py --url https://data.cityofgainesville.org/resource/gvua-xt9q.json --offset 0 --limit 5

## Example

![video](video)

## Features and functions

#### main.py

download_url(url) - this function was used to download and read in the .json url.
download_file(file) - this function was used to download and read in the .json file.
format_data(data, offset, limit) - this function was used to parse through the .json data and extract the desired elements into a list.
print_crimes(report) - this function was used to print out the elements into the deisred, thorn seperated, output.

## Bugs and Assumptions
The first assumption is that limit will never be greater than 1000 as to prevent going out of bounds when parsing through the data. The second assumption is that if a value does not exist, blank space will be printed where the value would have gone, like so "". Lastly the user must provide either a url or a file, along with an offset and a limit in order for the main.py file to run. If some or all of that data is not provided there will be a system message that notifies the user of what they are missing.
