import csv
import re
import requests
from bs4 import BeautifulSoup

# user-agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

def main():
    main_page = requests.get("https://www.jmi.ac.in/english/faculty-members", headers = headers)
    html = BeautifulSoup(main_page.text, 'lxml')
    faculty_list = html.select('h3')
    visited_URLs = {}
    for faculty in faculty_list:
        URL = faculty.find('a')["href"]
        if len(URL) > 20 or URL in visited_URLs:
            continue
        else:
            visited_URLs[URL] = True
            URL = "https://www.jmi.ac.in" + URL
            get_write(URL)

def get_write(URL):
    faculty_page = requests.get(URL, headers=headers)
    html = BeautifulSoup(faculty_page.text, 'lxml')
    name = html.find('h3', {'class' : 'img-right-text'}).getText()
    # removing '\n' and '\t' characters from beginning and end
    name = name.lstrip('\n')
    name = name.rstrip('\t')
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", faculty_page.text)
    emails += re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.ac.in", faculty_page.text)
    details = [name]
    for email in emails:
        details.append(email)
    csv_file = open('details.csv', mode = 'a')
    csv_write = csv.writer(csv_file, delimiter = ',')
    csv_write.writerow(details)
    
if __name__ == '__main__':
    main()