import csv
import re
import requests
from bs4 import BeautifulSoup

# user-agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

def main():
    main_page = requests.get("https://englishdu.ac.in/index.php/sample-page/faculty/", headers = headers)
    soup = BeautifulSoup(main_page.text, 'lxml')
    faculty_list = soup.select('h3')
    for faculty in faculty_list:
        URL = faculty.find('a')["href"]
        get_write(URL)

def get_write(URL):
    # faculty basic details from URL
    faculty = URL[46:]
    faculty = faculty.split('-')
    for i in range(len(faculty)):
        if len(faculty[i]) < 4:
            break
    faculty = faculty[:i]    
    faculty_page = requests.get(URL, headers=headers)
    # email IDs from faculty's official page
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", faculty_page.text)
    details = faculty + emails
    # write to csv
    csv_file = open('details.csv', mode = 'a')
    csv_write = csv.writer(csv_file, delimiter = ',')
    csv_write.writerow(details)
    
if __name__ == '__main__':
    main()