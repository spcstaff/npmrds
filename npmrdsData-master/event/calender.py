import urllib
import pprint
import requests
import json
from time import gmtime, strftime
import time
import mlbgame
import re
from bs4 import BeautifulSoup

def get_ppg():
    base_url = "http://www.ppgpaintsarena.com/events/calendar"
    # url = "http://www.ppgpaintsarena.com//events/calendar/2017/7"
    # response = requests.get(url)
    # pprint.pprint(response.json())]
    content = []
    returned_data = "Title, startDateTime, EndDateTime\n"

    for year in range(2011, 2018, 1):
        for month in range(1, 13, 1):
            url = base_url + "/%s/%s" % (year, month)
            response = requests.get(url)
            if response.status_code == 200:
                contents = response.json()
                # pprint.pprint(content['events'])
            if len(contents) != 0:
                for content in contents['events']:
                    title = content['Title']
                    startDateTime = content['StartDateTime']
                    EndDateTime = content['StartDateTime']
                    returned_data += "%s, %s, %s\n" % (title, startDateTime, EndDateTime)
            time.sleep(1)

    file_path = strftime("%d%H%M%S", gmtime())
    output = open("ppg%s.csv" % file_path, "w+")
    output.write(returned_data)
    output.close()

# get_ppg()


def get_pirates():
    returned_data = "time, game\n"
    for year in range(2016, 2017, 1):
        for month in range(1, 13, 1):
            for day in range(1, 32, 1):
                game = mlbgame.day(year, month, day, home="Pirates")
                if len(game) != 0:
                    today = "%s/%s/%s" % (month, day, year)
                    returned_data += "%s, %s\n" % (today, game[0])
    pprint.pprint(returned_data)

    file_path = strftime("pirates%d%H%M%S.csv", gmtime())
    output = open(file_path, "w+")
    output.write(returned_data)
    output.close()

# get_pirates()


def get_field():
    base_url = "http://heinzfield.com/events/"
    return_data = "title, startTime, endTime\n"
    for year in range(2014, 2018, 1):
        for month in range(1, 13, 1):
            cur_tuple = (year, month, 0, 0, 0, 0, 0, 0, 0)
            url = base_url + time.strftime("%Y-%m", cur_tuple) + "/"
            content = requests.get(url)
            soup = BeautifulSoup(content.text, 'lxml')
            events = soup.find_all(id=re.compile('^tribe-events-event-'))
            for event in events:
                info = json.loads(event.get('data-tribejson'))
                title = info['title'].replace(",", " ")
                print(title)
                startTime = info['startTime'].replace(",", " ")
                print(startTime)
                endTime = info['endTime'].replace(",", " ")
                print(endTime)
                return_data += "%s,%s,%s\n" % (title, startTime, endTime)
    output = open("field_event.csv", "w+")
    output.write(return_data)
    output.close()

# get_field()
