#!/usr/bin/python
import MySQLdb
import sys
sys.path.insert(0, "/Users/chaitanyakalantri/Desktop/Zappos Data Science/ZapposFoodApp")
import createdb

def testcreatedb():
    connection = MySQLdb.connect(host="localhost", user="root",  db="pythonspot")
    try:
        with connection.cursor as c:
            c.execute("show tables")
            assert c.fetchall()[0][0] == None
    
    createdb.createdb()
    
    try:
        with connection.cursor as c:
            c.execute("show tables")
            assert c.fetchall()[0][0] != None
    createdb.dropdb()

def testdropdb():

    createdb.createdb()
    connection = MySQLdb.connect(host="localhost", user="root",  db="pythonspot")
    try:
        with connection.cursor as c:
            c.execute("show tables")
            assert c.fetchall()[0][0] != None
    
    createdb.dropdb()
    
    try:
        with connection.cursor as c:
            c.execute("show tables")
            assert c.fetchall()[0][0] == None



if __name__ == "__main__":
    testdropdb()
    testcreatedb()

