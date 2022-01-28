import requests
import sys
import time
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import random


# # Used in old process as well as testing 
# # basically used to send requests to burp
# proxy = '127.0.0.1:8080' 

# os.environ['http_proxy'] = proxy 
# os.environ['HTTP_PROXY'] = proxy
# os.environ['https_proxy'] = proxy
# os.environ['HTTPS_PROXY'] = proxy
# os.environ['REQUESTS_CA_BUNDLE'] = "cacert.pem"

# proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Accept-Encoding": "gzip, defate, br",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Upgrade-Insecure-Requests" : "1",
    "Connection" : "keep-alive",
    }



def gather_contacts(company, pages):
    company = format_company(company)
    count = 0
    data = {
        "q" : company, 
        "start" : 0,
        "gsw_rd": "ssl" 
        }
    # current session contacts
    global gathered_contacts
    gathered_contacts = []
    
    while (count < pages ):
        u = "https://www.google.com/search?q=site%3Alinkedin.com%2Fin+"
        r = requests.get(url = u, params = data, verify=False, headers = headers)
        print("Page: {0}".format(str(count+1)))
        print(r.url)

        # send to scrape function
        scrape_contacts(r.content)

        data["start"] += 10
        count += 1
        # easiest bot detect prevention invented
        time.sleep(random.randrange(5, 10))
    # send results to preprocess and gen_emails
    return gathered_contacts

def scrape_contacts(req_content):
    soup = BeautifulSoup(req_content, "html.parser")
    contacts = soup.find_all("h3")
    for c in contacts:
        cur = str(c.text).split("-")[0]
        if "Related searches" in cur:
            continue
        else:
            gathered_contacts.append(cur)
    

def format_company(company):
    return company.replace(" ", "+")

def usage():
    print("[~] usage: ./main.py \"company name\" \"number of pages\" \"path to result csv\"")
    pass

if __name__ == "__main__":
    try:
        company = sys.argv[1]
        pages = sys.argv[2]
        # company = format_company(company)
        # path = sys.argv[3]
        gathered_contacts = gather_contacts(company, int(pages))
    except IndexError:
        usage()