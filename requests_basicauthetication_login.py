import requests as req
from requests.auth import HTTPBasicAuth


## BUILD WEBSITE STATUS CHECKER ## 
r = req.get('http://httpbin.org/basic-auth/penis/man', auth=('penis', 'man'))
print(r) ## to receive response back 
print(r.status_code)