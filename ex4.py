#!/usr/bin/python2
import MySQLdb as mdb

con = mdb.connect('localhost', 'testusr', 'test623', 'testdb')
with con:
    #cur = con.cursor()
    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute('select * from writers')
    for i in range(cur.rowcount): 
        row = cur.fetchone()
        print row['id'], row['name']
