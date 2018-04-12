#!/usr/bin/python2
import MySQLdb as mdb

con = mdb.connect('localhost', 'testusr', 'test623', 'testdb')
with con:
    cur = con.cursor()
#    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute('select * from writers')
    rows = cur.fetchall()
    desc = cur.description
    print "%s %3s" % (desc[0][0], desc[1][0])
    for row in rows: 
        print "%2s %3s" % row
