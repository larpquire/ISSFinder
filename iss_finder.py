import sys
from datetime import datetime
from time import sleep

import requests
from pytz import timezone

WAIT_TIME = 10    # seconds between consecutive http requests

def get_country(lat, lon, email):
    """
        Gets the country name of given coordinates using the 
        Nominatim Open Street API.
        Please see README.md for more details.
    """
    country = 'Probably above international airspace'
    url = 'http://nominatim.openstreetmap.org/reverse?format=json&lat=%f&lon=%f&zoom=0%s'
    
    try:
        res = requests.get(url % (lat, lon, email)).json()
        
        if 'address' in res:
            country = res['address']['country']
            
    except:
        country = 'Unable to locate country'
    
    return country


def main():
    """ 
        Uses the Open Notifier API to get the 
        current location of the ISS.
    """
    iss_pos_url = 'http://api.open-notify.org/iss-now.json'
    email = '&email=' + sys.argv[1] if len(sys.argv) > 1 else ''
    
    while True:
        try:
            res = requests.get(iss_pos_url).json()
            
            if res['message'] == 'success':
                lat = res['iss_position']['latitude']
                lon = res['iss_position']['longitude']
                timestamp = datetime.fromtimestamp(
                    res['timestamp'], tz=timezone('UTC')
                )
                print '%s\nCoordinates: (%f, %f)\nAbove: %s' % (
                    timestamp.astimezone(timezone('Asia/Manila')),
                    lat,
                    lon,
                    get_country(lat, lon, email)
                )
            else:
                print 'No data available at this time.'
            
            print 30*'-'
            sleep(WAIT_TIME)
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
    