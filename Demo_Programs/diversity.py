#https://developers.google.com/docs/api/quickstart/python

import requests
import json
fname = 'Lynda'
lname = 'Yearwood'
url = "https://api.diversitydata.io/?fullname="+fname+"%20"+lname
response = requests.get(url)
print (response.text)
data = (json.loads[response.text])
print (data["fullname"])