# For 3rd party lib, see pytz
# or https://pynative.com/list-all-timezones-in-python/
# import pytz
#
# print('Timezones')
# for timeZone in pytz.all_timezones:
#     print(timeZone)

# Starting python 3.9, we have "zoneinfo" package
import zoneinfo
timezones = list(zoneinfo.available_timezones())
timezones.sort()
for tz in timezones:
    print(tz)
print(f"Total {len(timezones)} timezones found.")
