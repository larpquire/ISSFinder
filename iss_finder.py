import sys
from datetime import datetime
from time import sleep

import requests
from requests.exceptions import RequestException
from pytz import timezone

WAIT_TIME = 10    # seconds between consecutive http requests

def get_country(payload):
    """
        Gets the country name of given coordinates using the 
        Nominatim Open Street API.
        Please see README.md for more details.
    """
    country = 'Probably above international airspace'
    url = 'http://nominatim.openstreetmap.org/reverse'
    
    try:
        res = requests.get(url, params=payload).json()
        
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
    email = sys.argv[1] if len(sys.argv) > 1 else None
    payload = {'format': 'json', 'email': email, 'zoom': 0}
    
    while True:
        try:
            res = requests.get(iss_pos_url).json()
            
            if res['message'] == 'success':
                timestamp = datetime.fromtimestamp(
                    res['timestamp'], tz=timezone('UTC')
                )
                payload['lat'] = res['iss_position']['latitude']
                payload['lon'] = res['iss_position']['longitude']
                print '%s\nCoordinates: (%f, %f)\nAbove: %s' % (
                    timestamp.astimezone(timezone('Asia/Manila')),
                    payload['lat'],
                    payload['lon'],
                    get_country(payload)
                )
            else:
                print 'No data available at this time.'
            
            print 30*'-'
            sleep(WAIT_TIME)
        except KeyboardInterrupt:
            break
        except RequestException as r:
            print '\a%s' % r
            break


if __name__ == '__main__':
    main()
    