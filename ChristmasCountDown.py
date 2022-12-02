#***Christmas Countdown X Financial Advent Calendar***

#To-do list:
#(1) Annotate code :)
#(2) Christmas countdown :)
#(3) Create an advent calendar of financial knowledge you've learnt this month :
#(4) random number generator to select a day and recap knowledge :

import datetime

#Setting the variables
dt = datetime.datetime
dtn = dt.now()

#Difference between Christmas and today's date
daysUntilChristmas = dt(year=2022, month=12, day=25) - dt(year=dtn.year, month=dtn.month, day=dtn.day)

if dt(year=dtn.year, month=dtn.month, day=dtn.day) == dt(year=2022, month=12, day=25):
    print("It's Christmassss!")

print("Christmas Countdown...\n>>>{}<<< days until Christmas!".format(daysUntilChristmas.days))
