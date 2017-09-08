from urllib.request import urlopen
import json
import pprint
from time import gmtime, strftime
from datetime import datetime
from datetime import timedelta


# call the api and generally extract hourly data
def get_history(from_date, to_date):
    # parse input date
    start = datetime.strptime(from_date, '%Y/%m/%d')
    end = datetime.strptime(to_date, '%Y/%m/%d')

    observation = []
    # recursive get url and call the api
    for n in range(int((end - start).days)):
        # build url
        i = start + timedelta(n)
        cur_time = i.strftime('%Y%m%d')
        url = 'http://api.wunderground.com/api/a5d9cc6780b63c74/history_%s/q/PA/Pittsburgh.json' % cur_time
        # call the api
        f = urlopen(url)
        json_string = f.read()
        parsed_json = json.loads(json_string)
        observation += parsed_json['history']['observations']

    pprint.pprint(observation)
    return observation

# get_history('1960/11/1', '1960/11/10')


# parse the result
def parse_result(fromdate, todate):
    # get observation data
    observations = get_history(fromdate, todate)

    returned_data = "date,year,cons, temp, dep, hum, wind, pressure\n"

    for observation in observations:
        date = observation['date']['pretty']
        cons = observation['conds']
        temp = observation['tempi']
        dep = observation['dewpti']
        hum = observation['hum']
        wind = observation['wspdi']
        pressure = observation['pressurei']
        cleared = "%s,%s,%s,%s,%s,%s,%s\n" % (date, cons, temp, dep, hum, wind, pressure)
        returned_data += cleared

    pprint.pprint(returned_data)
    print(len(observations))
    return returned_data

# parse_result()


def save_result(fromdate, todate):
    # name the file path with current time
    file_path = strftime("%Y%m%d%H%M%S", gmtime())
    # write the data stream
    output = open("weather%s.csv" % file_path , "w+")
    output.write(parse_result(fromdate, todate))
    output.close()

# format is important: 'yyyy/mm/dd'
save_result('2016/05/01', '2016/05/06')
