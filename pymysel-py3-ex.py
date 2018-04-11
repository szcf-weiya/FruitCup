import PyMySQL # cannot import. why??
try:
    db = PyMySQL.connect('localhost', 'testusr', 'test623', 'testdb')
    cursor = db.cursor()
    cursor.execute('select version()')
    data = cursor.fetchone()
    print("Database version: %s" % data)
finally:
    db.close()
