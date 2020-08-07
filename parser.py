import argparse
from bs4 import BeautifulSoup
import requests
import json

wayback_api = 'https://archive.org/wayback/available'
schedule_url = 'sis.itu.edu.tr/tr/ders_programlari/LSprogramlar/prg.php?fb=BLG'


def get_wayback_url(date):
    headers = {'url': schedule_url,
               'timestamp': date}
    response = requests.get(wayback_api, headers)
    wayback_url = response.json().get('archived_snapshots').get('closest').get('url')
    return wayback_url


def parse_schedule(url):
    data = {}
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    courses = soup.find_all('tr', {'onmouseover': True})
    for course in courses:
        columns = course.find_all('td')
        crn = columns[0].text
        course_title = columns[2].text
        instructor = columns[3].text
        data[crn] = {'course_title':course_title,
                     'instructor':instructor}
    return data


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Parsing old CRN - Instructor information from SIS.')
    arg_parser.add_argument('date', type=str, action='store', metavar='YYYYMMDD',
                            help='Date where CRN - Instructor information was present on SIS class schedules.')
    args = arg_parser.parse_args()

    url = get_wayback_url(args.date)
    data = parse_schedule(url)

    with open('data.json', 'w', encoding='utf8') as file:
        json.dump(data, file, indent=1, ensure_ascii=False)
