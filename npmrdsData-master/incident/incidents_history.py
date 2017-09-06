import urllib.request
import time


def get_file():
    url = "http://www.dot7.state.pa.us/crashdata/"
    zipSuffix = ".zip"
    counties = ['Allegheny', 'Armstrong', 'Beaver', 'Butler', 'Fayette', 'Greene', 'Indiana', 'Lawrence', 'Washington', 'Westmoreland']
    for i in range(1997,2017,1):
        time.sleep(1)
        for county in counties:
            file_name = county + "_" + str(i) + zipSuffix
            cur_url = url + file_name
            time.sleep(1)
            try:
                urllib.request.urlretrieve(cur_url,file_name)
            except Exception as e:
                print(e)

get_file()



