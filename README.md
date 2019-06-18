# nismod-db-api-issues
A issue reporting/handling repository for NISMOD-DB++ API.

# raising issues
Please add any issues here - https://github.com/geospatialncl/nismod-db-api-issues/issues

# How to use teh API

For early adoptors of the API - webpage/login/docs - https://www.nismod.ac.uk/api

**With Python**
  - Use the inbuilt requests library
  - e.g.
    - import requests  
    - response = requests.get('https://www.nismod.ac.uk/api/get_lads?lad_codes=E08000021',auth=('username','password'))  
    - response.status_code #200 = successful  
    - response.content #gets data records returned from API
    
**With curl**
  - (used in command line)
  - e.g.
    curl --user 'username':'password' https://www.nismod.ac.uk/api/get_lads?lad_codes=E08000021
