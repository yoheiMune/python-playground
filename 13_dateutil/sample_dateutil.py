# -*- coding: utf-8 -*-

# pip3 install --upgrade python-dateutil
# https://dateutil.readthedocs.org/en/latest/

from dateutil.relativedelta import relativedelta
from datetime import datetime, date, timedelta


# today
today = date.today()
print(today)

# 1ヶ月後
dt = today + relativedelta(months=1)
print(dt)

# 1年後
dt = today + relativedelta(years=1)
print(dt)

# 月末
dt = today + relativedelta(months=1) - timedelta(days=today.day)
print(dt)

# 月初
dt = today - timedelta(days=today.day-1)
print(dt)


"""
class relativedelta(object):
    def __init__(self, dt1=None, dt2=None,
                 years=0, months=0, days=0, leapdays=0, weeks=0,
                 hours=0, minutes=0, seconds=0, microseconds=0,
                 year=None, month=None, day=None, weekday=None,
                 yearday=None, nlyearday=None,
                 hour=None, minute=None, second=None, microsecond=None):
"""
# https://github.com/dateutil/dateutil/blob/master/dateutil/relativedelta.py

# https://docs.python.org/3.5/library/datetime.html
# class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)































