#***Christmas Countdown***

#To-do list:
#(1) Annotate code :)
#(2) Christmas countdown :)

import datetime

#Setting the variables
dt = datetime.datetime
dtn = dt.now()

#Difference between Christmas and today's date
daysUntilChristmas = dt(year=2022, month=12, day=25) - dt(year=dtn.year, month=dtn.month, day=dtn.day)

if dt(year=dtn.year, month=dtn.month, day=dtn.day) == dt(year=2022, month=12, day=25):
    print("It's Christmassss!")

print("Christmas Countdown...\n>>>{}<<< days until Christmas!".format(daysUntilChristmas.days))
