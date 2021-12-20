# -*- coding:utf-8 -*-
"""
purpose: for test purpose
description: user should type input(query and chart definition) here
author: DAIDAI_5
date: 2021/09/19
input:
    file_dir: JSON file path
    host, database, user, password: database information
"""
import os

class Input(object):
    def __init__(self, file_dir, host, database, user, password):
        self.file_dir = file_dir
        self.host = host
        self.database = database
        self.user = user
        self.password = password
    def run(self):
        string = "python app.py " + self.file_dir + ',' + self.host + ',' + self.database + ',' + self.user + ',' + self.password
        os.system(string)
        return

initial = Input("input.json", 'localhost', 'mag_test', 'root', 'MySQLSxn200519')
initial.run()
