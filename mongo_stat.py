#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
import datetime
try:
    from pymongo import MongoClient
    from pymongo.errors import ConnectionFailure
except ImportError, e:
    print("Error: %s." % (e))
    sys.exit(1)

HOST='localhost'
PORT=27017
MONGO_ARGS=['version','uptime','flushes', 'connections_current']

def mongo_connect(host=HOST, port=PORT):
    try:
        connection = MongoClient(host, port)
        return connection
    except ConnectionFailure:
        print("Error: Connection to MongoDB server on %s:%s failed" % (host, port))
        sys.exit(1)

def get_version(connection, version):
    return connection['test'].command('serverStatus')['version']
    connection.close()

def get_uptime(connection, uptime):
    return connection['test'].command('serverStatus')['uptime']

def get_backgroundFlushing(connection, flushes):
    return connection['test'].command('serverStatus')['backgroundFlushing']['flushes']

def get_connectionsCurrent(connection, connections_current):
    return connection['test'].command('serverStatus')['connections']['current']

if len(sys.argv) > 2:
    print("More than 1 (one) argument found.")
    exit(1)

for i in sys.argv:
    if i in MONGO_ARGS:
        if i == 'version':
            print(str(get_version(mongo_connect(), 'version')))
        elif i == 'uptime':
            print(int(get_uptime(mongo_connect(), 'uptime')))
        elif i == 'flushes':
            print(int(get_backgroundFlushing(mongo_connect(), 'flushes')))
        elif i == 'connections_current':
            print(int(get_connectionsCurrent(mongo_connect(), 'connections_current')))
            
