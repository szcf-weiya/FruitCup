#!/bin/bash
wget -c https://pypi.python.org/packages/a8/b4/3544c8e6ed9b1c6a00e5b302e3d5a646e43a8a0ac5216f5ae8706688706e/PyMySQL-0.8.0.tar.gz#md5=839eae787a6de12b133791c7778ebc3a -O PyMySQL.tar.gz
tar -xzf PyMySQL.tar.gz
cd PyMySQL*
python setup.py install
