#!/usr/bin/python
# -*- coding: utf-8 -*-

# OpenCart currency updater script using PrivatBank API.
# This script updates currency values and wtite them to MySQL `oc_currencies` table.

import mysql.connector
from mysql.connector import errorcode
import sys
import urllib2
import json

''' curr_codes = ['USD','EUR','RUR','BTC'] '''

'''
Database:

oc_currencies table ->
c_from | c_to | buy   | sell   | date       | time
EUR      UAH    29.9    30.6     2017-03-14   14:21
'''

config = {
  'user': 'root',
  'password': '******',
  'host': '127.0.0.1',
  'database': 'oc_currencies',
  'raise_on_warnings': True
}

def isConnectionOn():
    try:
        response=urllib2.urlopen('http://google.com.ua', timeout=1)
        return True
    except urllib2.URLError:
        return False

''' TODO: Переделать цикл с валютами! '''
def getValue(currency):
  # for i in curr_code
    if(currency == 'RUR'):
        link = urllib2.urlopen('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
        data = json.load(link)
        value = json.dumps(data[0]["sale"], separators=(',', ': ')).strip('"')
        # add buy also
        return value
    elif(currency == 'EUR'):
        link = urllib2.urlopen('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
        data = json.load(link)
        value = json.dumps(data[1]["sale"], separators=(',', ': ')).strip('"')
        return value
    else:
        link = urllib2.urlopen('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
        data = json.load(link)
        value = json.dumps(data[2]["sale"], separators=(',', ': ')).strip('"')
        return value

def updateCurrency(currency, value):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        
        '''
        currency_query = ("INSERT INTO oc_currency "
                       "(__, __) "
                       "VALUES (%f, %s)")
        currency_data = print data[2]['sale']
        cursor.commit()
        
        #factor = ('{:.2f}').format(1 / float(currency))
        
        cursor.close()
        cnx.close()
        '''
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Name or passwrod is incorrect.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist.")
        else:
            print(err)
    else:
        cnx.close()

if __name__ == "__main__":
    if isConnectionOn():
        # print(getValue(currency))
        # Add values to MySQL DB Currency Table
    else:
        print('[Error]: Please check your network connection.')
    sys.exit(1)    
