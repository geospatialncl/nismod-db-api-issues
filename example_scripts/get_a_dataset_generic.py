# import required libraries
import requests
import json

# get a dataset for a local authority using the generic method
response = requests.get('https://www.nismod.ac.uk/api/data/get?dataset_name=<dataset_name>&export_format=geojson&scale=lad&area_codes=<lad_code>, auth=('<username>','<password>'))

# get the returned data if a successful request
if response.status_code == 200:

    dataReturned = json.loads(response.text)

else:
    # return some error
	print(response.status_code)
    print(response.text)

# print the number of features returned
print(len(dataReturned['features']))

# print the data
print(dataReturned)

# save the data to a file
with open('path_to_data_file/name_of_file.geojson','w') as data_file: # open file to save data to
    json.dump(dataReturned, data_file) # write the data from API to the file
