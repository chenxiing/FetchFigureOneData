#encoding:utf-8

#import torndb

import config

class Database():
    def __init__(self, fetchDirector, parent = None):
        self.fetchDirector = fetchDirector
        self.mysqlHost = config.MYSQL_HOST
        self.mysqlDb = config.MYSQL_DB
        self.mysqlUser = config.MYSQL_USER
        self.mysqlPasswd = config.MYSQL_PASSWD

        self.db = torndb.Connection(host = self.mysqlHost, database = self.mysqlDb, user = self.mysqlUser, password = self.mysqlPasswd)


    def insetData(self):
        print '-----'


