
from django .http import HttpResponse
import urllib.request
import re

def index(request):
    url = ["http://gla.ac.in/faculty-staff"]
    response = urllib.request.urlopen(url[0])
    html = response.read()
    htmlstr = html.decode()
    # pdata=re.findall(r'[\w\.-]+@[\w\w.-]+',htmlstr)
    pdata = re.findall("Prof. [^ ][a-z A-Z]*", htmlstr)
    for item in pdata:
        print(item)

