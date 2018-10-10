#Current hour
import datetime
now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)

import time
year, month, day, hour, minute, second = time.strftime("%Y,%m,%d,%H,%M,%S").split(',')
print(year, month, day, hour, minute, second)

