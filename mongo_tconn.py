#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Modules: pymongo

from datetime import datetime
import sys

try:
    from pymongo import MongoClient
    from pymongo.errors import ConnectionFailure
except ImportError, e:
    print("Error: {0}.".format(e))
    sys.exit(1)

try:
    connection = MongoClient('localhost', 27017)
except ConnectionFailure:
    print("Error: Connection to MongoDB server on {0}: {1} failed".format('localhost', 27017))
    sys.exit(1)

startTime = datetime.now()

server_status = connection['test'].command('serverStatus')

def extract(status, keys):
    if len(keys) is 0:
        return status

    key = keys.pop(0)

    if not key:
        return status

    return extract(status[key], keys)

find = "backgroundFlushing.flushes"
keys = find.split(".")

val = extract(server_status, keys)
print(find, val)

print("Time spend: {}".format(datetime.now() - startTime))
