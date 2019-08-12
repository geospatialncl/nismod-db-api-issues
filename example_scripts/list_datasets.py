# import required libraries
import requests
import json

# get a list of data
response = requests.get('https://www.nismod.ac.uk/api/data/list', auth=('<username>','<password>'))

# get the returned data if a successful request
if response.status_code == 200:

    dataReturned = json.loads(response.text)

else:
    # return some error
	print(response.status_code)
    print(response.text)

# print the list of dataset names
print(dataReturned.keys())

# print all information
print(dataReturned)

# print metadata on a specific dataset
print(dataReturned['<dataset name>'])
