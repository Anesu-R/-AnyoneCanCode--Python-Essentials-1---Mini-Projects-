#(1) Annotate code, (2) Christmas countdown (3) Create an advent calendar of financial knowledge you learnt (4) random number generator to select day and recap

import datetime

dt = datetime.datetime
dtn = dt.now()

daysUntilChristmas = dt(year=2022, month=12, day=25) - dt(year=dtn.year, month=dtn.month, day=dtn.day)

print("Christmas Countdown...\n{} days until Christmas!".format(daysUntilChristmas.days))