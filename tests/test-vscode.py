import datetime
import os
now = str(datetime.datetime.now())
print(now)
print(type(now))

print(os.environ["DASHBOARD_COSMOS_ACCOUNT_URI"])