## ISSFinder
This Python script displays the current coordinates of the International Space Station as well as which country/region it's above at. The output is printed out onto the console, and updates every 10 seconds unless exited.

## Data Resources
1. [Open Notifier API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/) - for getting the ISS coordinates.
2. [Nominatim Open Street Map API](https://nominatim.openstreetmap.org/) - for handling the reverse geocoding stuff.

## Requirements
1. requests (`pip install requests`)
2. pytz (`pip install pytz`)

## Running the Script
cd to the project's root directory and then run:
```
$ python iss_finder.py <optional_email_address>
```
The script will continuously update the coordinates as well as name of the country/region displayed on the screen. To exit, press CTRL+C.

You may want to include a valid email address as a command line arg, especially when you intend to keep the script running for a long time. As per the [Nominatim Open Street Map wiki](http://wiki.openstreetmap.org/wiki/Nominatim#Reverse_Geocoding):
> If you are making large numbers of request please include a valid email address or alternatively include your email address as part of the User-Agent string.
> This information will be kept confidential and only used to contact you in the event of a problem, see Usage Policy for more details.

## Settings
The default waiting time between two consecutive HTTP requests made to Open Notifier is set at 10 seconds. If you want to change this, assign the desired value to the global variable `WAIT_TIME` in the file `iss_finder.py`.

## Contributing
As always, please feel free to comment or suggest improvements.
