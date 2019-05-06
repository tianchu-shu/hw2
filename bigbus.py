
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
from examples import custom_style_3, custom_style_2
from pprint import pprint
import os
import sys
import re
import csv
import pandas as pd
import datetime
from datetime import timedelta  
import uuid
import pickle


'''
House Keeping
'''

SEATS = 89
WEEKDAY_PRICE = 40
WEEKEND_PRICE = 50

dates = []
price = {}
today = datetime.datetime.now()


for i in range(10):
    new = today + datetime.timedelta(days=i+1)
    dates.append(new.strftime('%m/%d/%Y'))
    if new.weekday() <= 3:
        price[new.strftime('%m/%d/%Y')] = WEEKDAY_PRICE
    else:
        price[new.strftime('%m/%d/%Y')] = WEEKEND_PRICE




def ask_direction():
    directions_prompt = {
        'type': 'list',
        'name': 'direction',
        'message': 'Hello, what can I do for you today?',
        'choices': ['Buy', 'Refund', 'Exit']
    }
    answers = prompt(directions_prompt)
    return answers['direction']


def main():
    while True:
        print('Welcome to Big Bus Ticket Stand.')

        exit()



def exit():
    direction = ask_direction()

    tally_file = open('tally.pkl', 'rb')
    tally = pickle.load(tally_file)
    tally_file.close()
    print(tally)
    sfile = open('stock.pkl', 'rb')
    stock = pickle.load(sfile)
    sfile.close()

    output = open('report.pkl', 'rb')
    report = pickle.load(output)
    output.close()

    if today.strftime('%m/%d/%Y') not in report:
        report[today.strftime('%m/%d/%Y')] = {"Red": 0, "Blue": 0, "Green": 0}
    print(report)

    if (direction == 'Buy'):
        buy(stock, tally, report)
    elif (direction == 'Refund'):
        check_ticket(stock, tally)
    else:
        write_up(report)
        sys.exit()



def buy(stock, tally, report):
    answers = prompt(questions1, style=custom_style_3)
    pprint(answers)
    total = checkout(answers)
    print('Your total is $', total)
    currentstock = confirm(answers, tally, stock, report)
    sfile = open('stock.pkl', 'wb')
    pickle.dump(currentstock, sfile)
    sfile.close()
    print('Thank you, bye.')
    

def checkout(answers):
    chosen = answers['date']
    num = int(answers['amount'])
    tprice = price[chosen]
    total = num * tprice
    if num == 4:
        total = total * 0.9
        print('You are qualified for a 10 percent off discount.')
    return total


def confirm(answers, tally, stock, report):
    response = prompt({
        'type': 'confirm',
        'name': 'payment',
        'message': 'Do you want to procese to payment?',
        'default': False }, style=custom_style_3)
    if response['payment']:
        ticketvalidate(answers, tally, report)
        print('Here are your tickets:')
        num = int(answers['amount'])
        date = answers['date']
        route = answers["route"]
        for _ in range(num):
            ti = str(uuid.uuid4())
            print(ti)
            stock[ti] = [date, route]
    return stock
    


def ticketvalidate(answers, tally, report):
    sold = int(answers['amount'])
    date = answers['date']
    route = answers['route']
    if tally[date][route] < sold:
        raise Exception('The date and route you want is sold out')  
    else:
        tally[date][route] -= sold
        tally_file = open('tally.pkl', 'wb')
        pickle.dump(tally, tally_file)
        tally_file.close()

        report[(today.strftime('%m/%d/%Y'))][route] += sold
        print(report)
        rfile = open('report.pkl', 'wb')
        pickle.dump(report, rfile)
        rfile.close()



def confirm_refund(tid, stock, tally):
    answers = prompt({
        'type': 'confirm',
        'name': 'refund',
        'message': 'Are you sure you want to refund?',
        'default': False }, style=custom_style_3)

    if answers:
        date = stock[tid][0]
        route = stock[tid][1]
        stock[tid] = False
        tally[date][route] += 1
        tally_file = open('tally.pkl', 'wb')
        pickle.dump(tally, tally_file)
        tally_file.close()
        print('You have successfully refunded your ticket.')
        return stock
    else:
        return stock


def check_ticket(stock, tally):
    answers = prompt(questions2, style=custom_style_3)
    tid = answers['ticket']
    if tid not in stock:
        print('The ticket number is not valid. Please try again.')
        exit()
    elif stock[tid][0] in dates:
        cstock = confirm_refund(tid, stock, tally)
        sfile = open('stock.pkl', 'wb')
        pickle.dump(cstock, sfile)
        sfile.close()
    else:
        print("Sorry, you can only refund for future date trip")
        exit()


def write_up(report):
    df = pd.DataFrame.from_dict(report)
    df.to_csv("report.csv")

questions1 = [
    {
        'type': 'list',
        'name': 'date',
        'message': 'Which date?',
        'choices': dates
    },
    {
        'type': 'list',
        'name': 'route',
        'message': 'Which route?',
        'choices': ['Red', 'Green', 'Blue'],
        'default': 'Red'
    },
        {
        'type': 'list',
        'name': 'amount',
        'message': 'How many tickets?',
        'choices': ['1', '2', '3', '4']
    }
]


questions2 = [
    {
        'type': 'input',
        'name': 'ticket',
        'message': 'Your ticket number, please?'
    }]



if __name__ == '__main__': main()