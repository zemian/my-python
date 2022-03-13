# For 3rd party lib, see pytz
# or https://pynative.com/list-all-timezones-in-python/

import pytz

print('Timezones')
for timeZone in pytz.all_timezones:
    print(timeZone)
