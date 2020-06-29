import requests
from bs4 import BeautifulSoup as soup
text = ""
def get(url, Headers = None, data=None, params=None, allow_redirects=None,cookies=None,auth=None):
    if allow_redirects != None and allow_redirects != True:
        allow_redirects = False
    global text
    try:
        r = requests.get(url,headers= Headers,data=data,params=params, allow_redirects=allow_redirects,cookies=None, auth = None)
        text = r.text
        return r
    except:
        return "(Request-Soup Debug) there was an error with your GET request"
def post(url, headers=None,data=None,json=None,allow_redirects=None,cookies=None,auth=None):
    if allow_redirects != None and allow_redirects != True:
        allow_redirects = False
    global text
    try:
        r = requests.post(url,headers= Headers,data=data,params=params, json=json, allow_redirects=allow_redirects,cookies=None, auth = None)
        text = r.text
        return r
    except:
        return "(Request-Soup Debug) there was an error with your POST request"

def find(content,second=None, source=None, parser=None):
    bs = None
    global text
    if source == None:
        if parser == None:

            bs = soup(text, "html.parser")
        else:
            try:
                bs = soup(text, parser)
            except:
                return "Parser String Invalid"
    else:
        if parser == None:
            bs = soup(read, "html.parser")
        else:
            bs = soup(read, parser)
    return bs.find(content,second)

def findAll(content,second=None, source=None, parser=None):
    global text
    bs = None
    if source == None:
        if parser == None:

            bs = soup(text, "html.parser")
        else:
            try:
                bs = soup(text, parser)
            except:
                return "Parser String Invalid"
    else:
        if parser == None:
            bs = soup(read, "html.parser")
        else:
            bs = soup(read, parser)
    return bs.findAll(content,second)
class Session():
    def __init__(self):
        self.session = requests.Session()
        self.text = ""
    def get(url, Headers = None, data=None, params=None, allow_redirects=None,cookies=None,auth=None):
        if allow_redirects != None and allow_redirects != True:
            allow_redirects = False
        try:
            r = self.session.get(url,headers= Headers,data=data,params=params, allow_redirects=allow_redirects,cookies=None, auth = None)
            self.text = r.text
            return r
        except:
            return "(Request-Soup Debug) there was an error with your GET request"
    def post(url, headers=None,data=None,json=None,allow_redirects=None,cookies=None,auth=None):
        if allow_redirects != None and allow_redirects != True:
            allow_redirects = False
        try:
            r = self.session.post(url,headers= Headers,data=data,params=params, json=json, allow_redirects=allow_redirects,cookies=None, auth = None)
            text = r.text
            return r
        except:
            return "(Request-Soup Debug) there was an error with your POST request"

    def find(content,second=None, source=None, parser=None):
        bs = None
        if source == None:
            if parser == None:
                bs = soup(self.text, "html.parser")
            else:
                try:
                    bs = soup(self.text, parser)
                except:
                    return "Parser String Invalid"
        else:
            if parser == None:
                bs = soup(read, "html.parser")
            else:
                bs = soup(read, parser)
        return bs.find(content,second)

    def findAll(content,second=None, source=None, parser=None):
        bs = None
        if source == None:
            if parser == None:
                bs = soup(self.text, "html.parser")
            else:
                try:
                    bs = soup(self.text, parser)
                except:
                    return "Parser String Invalid"
        else:
            if parser == None:
                bs = soup(read, "html.parser")
            else:
                bs = soup(read, parser)
        return bs.findAll(content,second)
if __name__ == "__main__":
    text = ""
