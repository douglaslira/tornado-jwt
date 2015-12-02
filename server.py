#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Douglas Lira'

import os
import torndb
import tornado.auth
import tornado.ioloop
from tornado.options import define, options, parse_command_line, parse_config_file
import tornado.web

import app.handlers.main
import app.handlers.project
import app.handlers.auth

define("debug", default=True, help="Executar o servidor em modo debug", type=bool)
define("port", default=8001, help="Porta em que o servidor vai rodar", type=int)
define("mysql_host", default="127.0.0.1:3306", help="Hostname do banco de dados")
define("mysql_database", default="myproject", help="Nome do banco de dados")
define("mysql_user", default="root", help="Usuário do banco de dados")
define("mysql_password", default="12345", help="Senha do banco de dados")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", app.handlers.main.MainHandler),
            (r"/auth", app.handlers.auth.AuthHandler),
            (r"/project", app.handlers.project.ProjectHandler),
        ]
        settings = dict(
            debug = options.debug,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

        # Connect from MySQL
        self.db = torndb.Connection(
            options.mysql_host,
            options.mysql_database,
            options.mysql_user,
            options.mysql_password,
        )

def main():
    tornado.options.parse_command_line()
    application = Application()

    print ""
    print "----------------------------------------------"
    print "- Servidor rodando na porta %s...          -" % (options.port,)
    print "----------------------------------------------"
    print "- MySQL Host: %s                 -" % (options.mysql_host,)
    print "- MysQL DataBase: %s                  -" % (options.mysql_database,)
    print "- MysQL User: %s                           -" % (options.mysql_user,)
    print "- MysQL Password: %s                      -" % (options.mysql_password,)
    print "----------------------------------------------"
    print "- Author: Douglas Lira                       -"
    print "- Email: douglas.lira.web@gmail.com          -"
    print "----------------------------------------------"
    print ""

    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()