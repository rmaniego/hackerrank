"""
    Prompt: Print day of week from a string date.
"""

from datetime import datetime
import calendar

dt = datetime.strptime(input(), "%m %d %Y")
print(calendar.day_name[dt.weekday()].upper())