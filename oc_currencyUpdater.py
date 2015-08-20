#!/usr/bin/python
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode
import sys
import urllib2
import json

''' curr_code = ['RUR','EUR','USD'] '''
''' curr_sell = {} '''
''' curr_buy = {} '''

config = {
  'user': 'root',
  'password': '******',
  'host': '127.0.0.1',
  'database': 'os',
  'raise_on_warnings': True
}

def isInternetOn():
    try:
        response=urllib2.urlopen('http://google.com.ua', timeout=1)
        return True
    except urllib2.URLError:
        return False

''' TODO: Добавить цикл с валютами! '''
def getValue(currency):
    if(currency == 'RUR'):
        link = urllib2.urlopen('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
        data = json.load(link)
        value = json.dumps(data[0]["sale"], separators=(',', ': ')).strip('"')
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
        
        updateCurrency()
        '''
        #factor = ('{:.2f}').format(1 / float(currency))
        
        query = ("SELECT firstname, lastname, email FROM users LIMIT {}".format(number))
        cursor.execute(query)

        for (firstname, lastname, email) in cursor:
            print("{:s},{:s},{:s}").format(firstname, lastname, email)

        cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist.")
        else:
            print(err)
    else:
        cnx.close()

if __name__ == "__main__":
    if(isInternetOn() == True):
        print(getValue(currency))
    else:
        print('Network connection error!')
    sys.exit(1)
    
