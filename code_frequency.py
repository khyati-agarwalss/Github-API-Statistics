# Returns a weekly aggregate of the number of additions and deletions pushed to a repository.
# Fetches info from API: https://developer.github.com/v3/repos/statistics/#get-the-number-of-additions-and-deletions-per-week

import csv
import numpy as np
import requests
from sys import argv

run, url = argv

def extract_data_to_csv(url):
	data = requests.get(url).json()
	file_writer = open('code_frequency.csv', 'w', newline='')
	csv_writer = csv.writer(file_writer)
	csv_writer.writerow(['week', 'additions', 'deletions'])
	for elem in data:
	    csv_writer.writerow(np.absolute(elem))
	file_writer.close()

extract_data_to_csv(url)

# Run using the command:
# python code_frequency.py https://api.github.com/repos/khyati-agarwalss/Github-API-Statistics/stats/code_frequency
