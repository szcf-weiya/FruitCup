#!/usr/bin/python2
import MySQLdb as mdb

con = mdb.connect('localhost', 'testusr', 'test623', 'testdb');
with con:
    cur = con.cursor()
    cur.execute('select * from writers');
#    rows = cur.fetchall()
#    for row in rows:
#        print row
    ## alternative
    for i in range(cur.rowcount):
        row = cur.fetchone()
        print row[0], row[1]
