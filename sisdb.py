#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python:   2.7.8
# Author:   Oleksandr Bogovyk
# Date:     04.11.2014

import sys
import random
import string
import mysql.connector
from mysql.connector import errorcode

NORMAL_STATE    =   0
WARNING_STATE   =   1
CRITICAL_STATE  =   2
UNKNOWN_STATE   =   3

DB_USER = 'sisuser'
DB_NAME = 'sisdb'
DB_PASS = 'sispass'

sql_config = {
    'user': DB_USER,
    'password': DB_PASS,
    'host': '127.0.0.1',
    'database': DB_NAME
}

# Генерация строки (имени пользователя)
def randomWord(wordLength):
    return ''.join(
        random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) for i in range(wordLength))

# Генерация возраста студента
def randomAge():
    rAge = (int(random.randint(18, 50)))
    return rAge

# Получение всех строк из базы c подсчетом
def getDbRows():
    print("Проверка данных в таблице 'students'...")
    print("")
    try:
        dbcon = mysql.connector.connect(**sql_config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Ошибка подключения к базе данных: неверное имя или пароль.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Ошибка подключения к базе данных: база данных не найдена.")
        else:
            print(err)

    cursor = dbcon.cursor()

    query = ("SELECT * FROM students")
    cursor.execute(query)

    for (id, name, age) in cursor:
        print("id:{0}, name:{1}, age:{2}".format(id, name, age))

    cursor = dbcon.cursor()

    query = ("SELECT COUNT(*) FROM students")
    cursor.execute(query)

    print("")
    for [i] in cursor:
        if (i >= 0 and i <= 50):
            print("Количество записей в таблице: {0}. Выход с кодом {1}.".format((i), (NORMAL_STATE)))
            sys.exit(NORMAL_STATE)
        elif (i >= 50 and i <= 100):
            print("Количество записей в таблице: {0}. Выход с кодом {1}.".format((i), (WARNING_STATE)))
            sys.exit(WARNING_STATE)
        elif (i > 100):
            print("Количество записей в таблице: {0}. Выход с кодом {1}.".format((i), (CRITICAL_STATE)))
            sys.exit(CRITICAL_STATE)
        else:
            sys.exit(UNKNOWN_STATE)

    cursor.close()
    dbcon.close()

# Добавление N-строк в базу
def addDbRows(numbers):
    print("Добавление {0} строк в таблицу 'students'...".format(numbers))
    print("")
    try:
        dbcon = mysql.connector.connect(**sql_config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Ошибка подключения к базе данных: неверное имя или пароль.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Ошибка подключения к базе данных: база данных не найдена.")
        else:
            print(err)

    cursor = dbcon.cursor()

    for i in range(numbers):
        query = ("INSERT INTO sisdb.students (name, age) VALUES ('{0}',{rndAge})".format(randomWord(4), rndAge=randomAge()))
        cursor.execute(query)

        dbcon.commit()

    cursor.close
    dbcon.close()

# Удаление N-строк из базы
def delDbRows(numbers):
    print("Удление строк из таблицы 'students'...")
    print("")
    try:
        dbcon = mysql.connector.connect(**sql_config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Ошибка подключения к базе данных: неверное имя или пароль.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Ошибка подключения к базе данных: база данных не найдена.")
        else:
            print(err)

    cursor = dbcon.cursor()
    query = ("DELETE FROM sisdb.students ORDER BY id desc limit {0}".format(numbers))
    cursor.execute(query)
    dbcon.commit()

    cursor.close
    dbcon.close()

# Удаление всех строк из базы
def truncateDbRows():
    print("Очистка таблицы таблицы 'students'...")
    print("")
    try:
        dbcon = mysql.connector.connect(**sql_config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Ошибка подключения к базе данных: неверное имя или пароль.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Ошибка подключения к базе данных: база данных не найдена.")
        else:
            print(err)

    cursor = dbcon.cursor()
    query = ("TRUNCATE TABLE sisdb.students;")
    cursor.execute(query)

    dbcon.commit()

    cursor.close()
    dbcon.close()


# Создать исходные строки
def recreateDbRows():
    print("Восстановление строк в таблице 'students'...")
    print("")
    try:
        dbcon = mysql.connector.connect(**sql_config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Ошибка подключения к базе данных: неверное имя или пароль.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Ошибка подключения к базе данных: база данных не найдена.")
        else:
            print(err)

    cursor = dbcon.cursor()
    query = (
        "INSERT INTO sisdb.students (id, name, age) VALUES (1,'Aaaa',25),(2,'Bbbb',20),(3,'Cccc',14),(4,'Dddd',50),(5,'Eeee',11),(6,'Ffff',11),(7,'Gggg',11),(8,'Hhhh',11),(9,'Iiii',22),(10,'Jjjj',33);")
    cursor.execute(query)

    dbcon.commit()

    cursor.close()
    dbcon.close()

if len(sys.argv) >= 1:
    if sys.argv[1] == "--getrows":
        getDbRows()
    elif sys.argv[1] == "--addrows":
        if sys.argv[2] != "":
            i = int(sys.argv[2])
            addDbRows(i)
            else
            print("Ошибка добавления. Для ключа '--addrows' необходимо указать только один параметр (целое число).")
    elif sys.argv[1] == "--delrows":
        if sys.argv[2] != "":
            i = int(sys.argv[2])
            delDbRows(i)
            else
            print("Ошибка удаления. Для ключа '--delrows' необходимо указать только один параметр (целое число).")
    elif sys.argv[1] == "--truncrows":
        truncateDbRows()
    elif sys.argv[1] == "--recrows":
        recreateDbRows()
    else:
        print("Ошибка передачи параметра...")
        exit(UNKNOWN_STATE)
else:
    print("Ошибка передачи параметра...")
    