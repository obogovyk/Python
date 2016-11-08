#!/usr/bin/python
# -*- coding: utf-8 -*-

# Script for monitoring MongoDB for Zabbix Template
# v.0.11

import sys
try:
    from pymongo import MongoClient
    from pymongo.errors import ConnectionFailure
except ImportError, e:
    print("Error: {0}:s.".format(e))
    sys.exit(1)

host = 'localhost'
port = 27017
# auth = False

MONGO_INFO = [
    'info_version', 'info_uptime'
]
MONGO_ASSERTS = [
    'asserts_regular', 'asserts_warning', 'asserts_msg', \
    'asserts_user', 'asserts_rollovers'
]
MONGO_BFLUSH = [
    'backgroundFlushing_flushes', 'backgroundFlushing_total_ms', \
    'backgroundFlushing_average_ms', 'backgroundFlushing_last_ms'
]
MONGO_CONNECTIONS = [
    'connections_current', 'connections_available'
]
MONGO_DUR = [
    'dur_commits', 'dur_writeToDataFilesMB', 'dur_compression', \
    'dur_commitsInWriteLock', 'dur_earlyCommits'
]
MONGO_NETWORK = [
    "network_bytesIn", "network_bytesOut"
]
MONGO_MEMORY =  [
    'mem_bits', 'mem_resident', 'mem_virtual', \
    'mem_mapped', 'mem_mappedWithJournal'
]

class MongoStats():

    # self._login = ""
    # self._password = ""

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._concat_list = []
        self._connection = self._mongo_connect()

    def __del__(self):
        self._connection.close()

    def _mongo_connect(self):
        try:
            # if auth:
                # connection = MongoClient('mongodb://'+login+':'+password+'@'+self._host+':'+ self._port)
            # else:
            connection = MongoClient(self._host, self._port)
            return connection
        except ConnectionFailure:
            print("Error: Connection to MongoDB server on {0}:s: {1}:s failed".format(self._host, self._port))
            sys.exit(1)

    def concat_metrics(self, p1, p2, p3, p4, p5, p6, p7):
        self._concat_list = list(set(p1 + p2 + p3 + p4 + p5 + p6 + p7))
        return self._concat_list

    def get_version(self):
        return self._connection['test'].command('serverStatus')['version']

    def get_uptime(self):
        return self._connection['test'].command('serverStatus')['uptime']


    def get_asserts_regular(self):
        return self._connection['test'].command('serverStatus')['asserts']['regular']

    def get_asserts_warning(self):
        return self._connection['test'].command('serverStatus')['asserts']['warning']

    def get_asserts_msg(self):
        return self._connection['test'].command('serverStatus')['asserts']['msg']

    def get_asserts_user(self):
        return self._connection['test'].command('serverStatus')['asserts']['user']

    def get_asserts_rollovers(self):
        return self._connection['test'].command('serverStatus')['asserts']['rollovers']


    def get_backgroundFlushing_flushes(self):
        return self._connection['test'].command('serverStatus')['backgroundFlushing']['flushes']

    def get_backgroundFlushing_total_ms(self):
        return self._connection['test'].command('serverStatus')['backgroundFlushing']['total_ms']

    def get_backgroundFlushing_average_ms(self):
        return self._connection['test'].command('serverStatus')['backgroundFlushing']['average_ms']

    def get_backgroundFlushing_last_ms(self):
        return self._connection['test'].command('serverStatus')['backgroundFlushing']['last_ms']


    def get_connections_current(self):
        return self._connection['test'].command('serverStatus')['connections']['current']

    def get_connections_available(self):
        return self._connection['test'].command('serverStatus')['connections']['available']


    def get_dur_commits(self):
        return self._connection['test'].command('serverStatus')['dur']['commits']

    def get_dur_writeToDataFilesMB(self):
        return self._connection['test'].command('serverStatus')['dur']['writeToDataFilesMB']

    def get_dur_compression(self):
        return self._connection['test'].command('serverStatus')['dur']['compression']

    def get_dur_commitsInWriteLock(self):
        return self._connection['test'].command('serverStatus')['dur']['commitsInWriteLock']

    def get_dur_earlyCommits(self):
        return self._connection['test'].command('serverStatus')['dur']['earlyCommits']


    def get_network_bytesIn(self):
        return self._connection['test'].command('serverStatus')['network']['bytesIn']

    def get_network_bytesOut(self):
        return self._connection['test'].command('serverStatus')['network']['bytesOut']


    def get_mem_bits(self):
        return self._connection['test'].command('serverStatus')['mem']['bits']

    def get_mem_resident(self):
        return self._connection['test'].command('serverStatus')['mem']['resident']

    def get_mem_virtual(self):
        return self._connection['test'].command('serverStatus')['mem']['virtual']

    # double parameter: check this metric again!
    def get_mem_mapped(self):
        return self._connection['test'].command('serverStatus')['mem']['mapped']

    def get_mem_mappedWithJournal(self):
        return self._connection['test'].command('serverStatus')['mem']['mappedWithJournal']

if __name__ == "__main__":

    if len(sys.argv) > 2:
        print('ERROR: Only 1 (one) argument allowed.')
        exit(1)

    mng = MongoStats(host, port)
    MONGO_TOTAL = mng.concat_metrics(MONGO_INFO, MONGO_ASSERTS, MONGO_BFLUSH, \
                              MONGO_CONNECTIONS, MONGO_DUR, MONGO_NETWORK, \
                              MONGO_MEMORY)

    for i in sys.argv:
        for items in MONGO_TOTAL:
            if i in items and i == 'info_version':
                print mng.get_version()
            elif i in items and i == 'info_uptime':
                print mng.get_uptime()

            elif i in items and i == 'asserts_regular':
                print mng.get_asserts_regular()
            elif i in items and i == 'asserts_warning':
                print(mng.get_asserts_warning())
            elif i in items and i == 'asserts_msg':
                print(mng.get_asserts_msg())
            elif i in items and i == 'asserts_user':
                print(mng.get_asserts_user())
            elif i in items and i == 'asserts_rollovers':
                print(mng.get_asserts_rollovers())

            elif i in items and i == 'backgroundFlushing_flushes':
                print(mng.get_backgroundFlushing_flushes())
            elif i in items and i == 'backgroundFlushing_total_ms':
                print(mng.get_backgroundFlushing_total_ms())
            elif i in items and i == 'backgroundFlushing_average_ms':
                print(mng.get_backgroundFlushing_average_ms())
            elif i in items and i == 'backgroundFlushing_last_ms':
                print(mng.get_backgroundFlushing_last_ms())

            elif i in items and i == 'connections_current':
                print(mng.get_connections_current()-1)
            elif i in items and i == 'connections_available':
                print(mng.get_connections_available()+1)

            elif i in items and i == 'dur_commits':
                print(mng.get_dur_commits())
            elif i in items and i == 'dur_writeToDataFilesMB':
                print(mng.get_dur_writeToDataFilesMB())
            elif i in items and i == 'dur_compression':
                print(mng.get_dur_compression())
            elif i in items and i == 'dur_commitsInWriteLock':
                print(mng.get_dur_commitsInWriteLock())
            elif i in items and i == 'dur_earlyCommits':
                print(mng.get_dur_earlyCommits())

            elif i in items and i == 'network_bytesIn':
                print(mng.get_network_bytesIn())
            elif i in items and i == 'network_bytesOut':
                print(mng.get_network_bytesOut())

            elif i in items and i == 'mem_bits':
                print(mng.get_mem_bits())
            elif i in items and i == 'mem_resident':
                print(mng.get_mem_resident())
            elif i in items and i == 'mem_virtual':
                print(mng.get_mem_virtual())
            elif i in items and i == 'mem_mapped':
                print(mng.get_mem_mapped())
            elif i in items and i == 'mem_mappedWithJournal':
                print(mng.get_mem_mappedWithJournal())

# endscript
