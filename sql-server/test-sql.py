#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import unittest
import pytest
import os
import testinfra
import pyodbc
from dotenv import load_dotenv

# https://learn.microsoft.com/zh-tw/sql/connect/python/python-driver-for-sql-server?view=sql-server-ver16

# Pre-requisites:
# https://learn.microsoft.com/zh-tw/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16&tabs=redhat18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline
# curl https://packages.microsoft.com/config/rhel/9/prod.repo | sudo tee /etc/yum.repos.d/mssql-release.repo

# sudo yum remove unixODBC-utf16 unixODBC-utf16-devel #to avoid conflicts
# sudo ACCEPT_EULA=Y yum install -y msodbcsql18
# # optional: for bcp and sqlcmd
# sudo ACCEPT_EULA=Y yum install -y mssql-tools18
# echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
# source ~/.bashrc
# # optional: for unixODBC development headers
# sudo yum install -y unixODBC-devel
#

#
# Set SQL Server Environment Variables
#

# SERVER = '<server-address>'
# DATABASE = '<database-name>'
# USERNAME = '<username>'
# PASSWORD = '<password>'

if load_dotenv(".env-sql"):
    SERVER = os.getenv('SERVER')
    DATABASE = os.getenv('DATABASE')
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
else:
    print("Please set SQL Server Environment Variables")


class TestAzureSQLServer(unittest.TestCase):

    def setUp(self):
        self.host = testinfra.get_host("local://")
        self.connectionString = ('DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE},Port=1443;UID={USERNAME};PWD={PASSWORD};Encrypt=yes;TrustServerCertificate=yes;').format(SERVER=SERVER, DATABASE=DATABASE, USERNAME=USERNAME, PASSWORD=PASSWORD)
        print(self.connectionString)

    def test_to_sql_server_dns(self):
        sql_server = self.host.addr(SERVER)
        self.assertTrue(sql_server.is_resolvable) # Equal to "getent ahosts 168.63.129.16"

    def test_to_sql_server_ip(self):
        sql_server = self.host.addr(SERVER)
        self.assertFalse(sql_server.is_reachable) # Equal to "ping -W 1 -c 1 168.63.129.16"
        self.assertFalse(sql_server.port(80).is_reachable) # Equal to "nc -w 1 -z 168.63.129.16 80"
        self.assertTrue(sql_server.port(443).is_reachable) # Equal to "nc -w 1 -z 168.63.129.16 443"
        self.assertTrue(sql_server.port(1443).is_reachable) # Equal to "nc -w 1 -z 168.63.129.16 1443"

    def test_connection_to_sql(self):
        # conn = pyodbc.connect(self.connectionString)
        print(conn)
