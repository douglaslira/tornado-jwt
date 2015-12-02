# -*- coding: utf-8 -*-
__author__ = 'Douglas Lira'
import tornado
import json

class ProjectHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Project!!')

    def post(self):
        data = json.loads(self.request.body)
        teste = data['details']
        self.write(teste)