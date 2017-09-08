import urllib
import requests
import json
import pprint
from time import gmtime
from time import strftime


def get_json():
    url = "https://www.dot511.state.pa.us/RCRS_Event_Data/api/RCRS/liveEvents"
    requests_header = {"Authorization": "Basic c2hsMTIwQHBpdHQuZWR1OkxzejIyNzIzOCE= "}
    r = requests.get(url, headers=requests_header)
    # pprint.pprint(content['Values'][0])
    values = r.json()['Values']

    returned_data = "EventID, EventType, EventOccurs, Update, County, StateRouteNo, FromLocLat, FromLocLong, ToLocLat, TolocLong\n"

    for value in values:
        EventID = value['EventID']
        EventType = value['EventType']
        EventOccurs = value['DateTimeEventOccurs']
        Update = value['LastUpdate']
        County = value['County']
        StateRouteNo = value['StateRouteNo']
        FromLocLatLong = value['FromLocLatLong']
        ToLocLatLong = value['ToLocLatLong']

        cleard = f"{EventID},{EventType},{EventOccurs},{Update},{County},{StateRouteNo},{FromLocLatLong},{ToLocLatLong}\n"
        returned_data += cleard
    file_path = strftime("%Y%m%d%H%M%S", gmtime())
    output = open("incidents%s.csv" % file_path  ,"w+") # the downloaded file would be located with __incident__.py in npmrdsData-master
    output.write(returned_data)
    output.close()

get_json()


def read_json():
    with open('response.json', 'r') as f:
        data = json.load(f)
    pprint.pprint(data['Values'][0])

# read_json()
