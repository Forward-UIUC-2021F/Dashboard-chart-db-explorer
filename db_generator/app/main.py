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
import helpfunc
import chart_def
import layout
import app

class dash_generator(object):
    def __init__(self, file_dir, host, database, user, password):
        self.file_dir = file_dir
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def run(self):
        initial = helpfunc.Input(self.file_dir, self.host, self.database, self.user, self.password)
        tot_record,tot_chart_config, tot_x, tot_y, tot_mark, lay_out_rows, tot_title, corr_index = helpfunc.Input.handle_query(initial)

        # chartdef needs tot_mark, tot_record, tot_chart_config, tot_x, tot_y, tot_title
        res, tot_chart_config = chart_def.handle_records(tot_mark, tot_record, tot_chart_config, tot_x, tot_y, tot_title)

        # split_to_page(res, lay_out_rows)
        multi_page = layout.split_to_page(res, lay_out_rows)

        # def app(multi_page,tot_mark,corr_index)
        app.app(multi_page,tot_mark,corr_index)

