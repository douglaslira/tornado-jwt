__author__ = 'Douglas Lira'

import tornado
import torndb

class DBObject(object):
    def __init__(self, db):
        self.db = db;