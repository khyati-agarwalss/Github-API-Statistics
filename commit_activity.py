# Returns the last year of commit activity grouped by week
# Fetches info from API: https://developer.github.com/v3/repos/statistics/#get-the-last-year-of-commit-activity-data

import csv
import requests
from sys import argv

run, url = argv

def extract_data_to_csv(url):
	data = requests.get(url).json()
	file_writer = open('commit_activity.csv', 'w', newline='')
	csv_writer = csv.writer(file_writer)
	count = 0
	for elem in data:
	    if count == 0:
	        header = ['week', 'total', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
	        csv_writer.writerow(header)
	        count += 1
	    values = [elem['week'], elem['total']]
	    for i in range(7):
	    	values.append(elem['days'][i])
	    csv_writer.writerow(values)
	file_writer.close()

extract_data_to_csv(url)

# Run using the command:
# python commit_activity.py https://api.github.com/repos/khyati-agarwalss/Github-API-Statistics/stats/commit_activity
