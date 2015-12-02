# -*- coding: utf-8 -*-
__author__ = 'Douglas Lira'
import tornado

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Olá Mundo!!')