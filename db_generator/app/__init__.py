# -*- coding:utf-8 -*-
"""
author: DAIDAI_5
date: 2021/12/20
purpose: starting code
"""
# example starting code
from main import dash_generator

module = dash_generator("input.json", 'localhost', 'mag_test', 'root', 'MySQLSxn200519')
module.run()
