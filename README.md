# HW2 Big Bus

Today we finish our look at TDD and observe its impact on the activity
of software design.  We will try to finish the refactoring unit
today, but it may spill over into next week as well.

### Instructions for running project

**Preq**
> Install libraries if needed: PyInquirer, uuid, datetime

Steps to operate the sales application:
1. setup the data on the backend
run the command  >python3 backend.py 

2. Run the sales applications
run the command >python3 bigbus.py 

### Buy
1. Choose your date
2. Choose your route
3. Choose the number of tickets you want to buy
4. Confirm the purchase and get the unique id num for each ticket you buy

### Refund
1. Provide your ticket num (YOU HAVE TO HAVE TICKET TO REFUND)
2. Confirm the refund 
3. Get your refund

I assume the bus tickets for weekdays are $40, for weekends are $50.
I am also assuming the consumers need to provide the unique id of the tickets they want to refund, if they lost the tickets they cannot get refund.

### The daily report will be generated when you exit the sales application as a csv file called "report.csv"


I also have three dictionary files saved in pickles to keep track of the sales:
stock.pkl has each of the ticket num and its date and route.
tally.pkl has each of available numbers of tickets for each route for different dates
report.pkl is the dictionary to keep track of daily sales which will be written to the report.csv" at the end of each day/when the cashier exit the app
