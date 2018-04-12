# FruitCup
Notes for using python and MySQL when participating in the Fruit Cup Contest.

## load data local infile

提示“ERROR 1148 (42000): The used command is not allowed with this MySQL version”

参考[MySQL: Enable LOAD DATA LOCAL INFILE](https://stackoverflow.com/questions/10762239/mysql-enable-load-data-local-infile)

解决方案，传入“local\_infile=1”，其实离正确答案就只有一步之遥，我传入的是“local-infile=1”

参考

1. [MySQL LOAD DATA LOCAL INFILE Python](https://stackoverflow.com/questions/12890098/mysql-load-data-local-infile-python)
2. [MySQL :: MySQL 5.5 Reference Manual :: 23.8.7.49 mysql_options()](https://dev.mysql.com/doc/refman/5.5/en/mysql-options.html)
## References
1. [mySQL Python turtorial](http://zetcode.com/db/mysqlpython/)
2. [try...except...finally](https://blog.csdn.net/u012208403/article/details/40476363)
3. [Python 3 - MySQL Database Access](https://www.tutorialspoint.com/python3/python_database_access.htm)
4. [MySQL - 6.3.2 Adding User Accounts](https://dev.mysql.com/doc/refman/5.5/en/adding-users.html)
