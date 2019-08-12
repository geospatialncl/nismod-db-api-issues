# nismod-db-api-users
A repository to provide inforamtion, help and an issue reporting method for NISMOD-DB++ API.

# raising issues
Please add any issues here - https://github.com/geospatialncl/nismod-db-api-users/issues

# How to use the API

For early adoptors of the API - webpage/login/docs - https://www.nismod.ac.uk/api

**Python**  
***exmaple scripts***
  - See the set of example scripts available in the repository - https://github.com/geospatialncl/nismod-db-api-users/tree/master/example_scripts

***details***
  - Use the inbuilt requests library
  - e.g.
    - import requests  
    - response = requests.get('https://www.nismod.ac.uk/api/get_lads?lad_codes=E08000021',auth=('username','password'))  
    - response.status_code #200 = successful  
    - response.content #gets data records returned from API
    
**curl**
  - (used in command line)
  - e.g.
    curl --user 'username':'password' https://www.nismod.ac.uk/api/get_lads?lad_codes=E08000021
