"""A vaccination calculator."""

__author__ = "730323863"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population:"))
dosesadmined: int = int(input("Doses Administered:"))
doseperday: int = int(input("Doses per day:"))
targetpercent: int = int(input("Target Percent Vaccinated:"))
vaccination: int = int(targetpercent)

step1: float = population * (targetpercent / 100)
step2: float = dosesadmined / 2
step3: float = step1 - step2
step4: float = doseperday / 2
step5: float = round(step3 / step4)

today: datetime = datetime.today()
one_day: timedelta = timedelta(step5)
estimateddate: datetime = today + one_day

print("We will reach " + str(vaccination) + "% vaccination in " + str(step5) + 
        " days, which falls on " + estimateddate.strftime("%B %d, %Y"))