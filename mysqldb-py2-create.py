#!/usr/bin/python2

import MySQLdb as mdb

con = mdb.connect('localhost', 'testusr', 'test623', 'testdb')

with con:
    cur = con.cursor();
    cur.execute('drop table if exists writers')
    cur.execute('create table writers(id int primary key auto_increment, name varchar(25))')
    cur.execute('insert into writers(name) values("weiya")')
    cur.execute('insert into writers(name) values("lijun")')
