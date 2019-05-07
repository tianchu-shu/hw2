import csv
import pickle
import os
import sys
import re
import csv
import datetime
import pandas as pd
from datetime import timedelta  
import uuid

SEATS = 89
WEEKDAY_PRICE = 40
WEEKEND_PRICE = 50
route = {"Red": 5*SEATS, "Blue": 2*SEATS, "Green": 4*SEATS}


#create the database in the backend first before running the cmd app


today = datetime.datetime.now()
report = {today.strftime('%m/%d/%Y'): {"Red": 1, "Blue": 1, "Green": 0}}
output = open('report.pkl', 'wb')
pickle.dump(report, output)
output.close()


dates = [] 
for i in range(10):
    new = today + datetime.timedelta(days=i+1)
    dates.append(new.strftime('%m/%d/%Y'))    


tally = {}
for date in dates:
    tally[date] = route.copy()

tally[dates[6]]['Blue'] -= 1
tally[dates[5]]['Red'] -= 1
print(tally)

# write tally to a file
output = open('tally.pkl', 'wb')
pickle.dump(tally, output)
output.close()


#create some sold tickets in the stock    
stock = {'c56c67ce-f8dd-4da9-a59c-fb2a02f74c1a': [dates[5],'Red'], 'a1cde9b2-f132-4e0b-b5cb-6668a0c54328': [dates[6], 'Blue']}

# write tickets stock to a file
output = open('stock.pkl', 'wb')
pickle.dump(stock, output)
output.close()

