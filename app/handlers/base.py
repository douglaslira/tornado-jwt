__author__ = 'Douglas Lira'
# -*- coding: utf-8 -*-

import tornado

class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.db
    
    def options(self):
        pass

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'OPTIONS, POST, GET, PATCH, DELETE, PUT')
        self.set_header('Access-Control-Allow-Headers', 'Content-Type')