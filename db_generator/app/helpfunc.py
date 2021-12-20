# -*- coding:utf-8 -*-
"""
purpose:
    1. handle JSON format file
    2. help functions that (dis-)connect the database and get query result
author: DAIDAI_5
date: 2021/09/18
input: file_dir in argv, the file is in JSON format and contains query and chart_def
output:                 | type  | description
    lay_out_rows        | dict  | record each content of multipage app
    tot_mark            | dict  | for markdowns， keys=index from 0...n
    tot_record          | dict  | for charts (record returned by query), keys=index from 0...n
    tot_chart_config    | dict  | for charts (what chart is it), keys=index from 0...n
    tot_x, tot_y        | dict  | for charts (x-y mapping), keys=index from 0...n
    tot_title           | dict  | for charts (title), keys=index from 0...n
    corr_index          | dict  | record name-index
"""
import mysql.connector
import pandas as pd
import re  # regular expression
import json

'''
connect to the database, will be called by the Input class
'''
class Database(object):
    def __init__(self, host, database, user, password, query):
        'variables only available for developer <<connect to database>>'
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.query = query

    # database connection(set-up, de-connect)
    def set_connection(self):
        """
        purpose: help function that build up connection with database and test if conncetion valid
        input: host,database,user,password
        output: connection
        """
        try:
            connection = mysql.connector.connect(host=self.host, database=self.database, user=self.user,
                                                 password=self.password)
            # test if connect to database successfully
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
            return connection
        except Error as e:
            print("Error while connecting to MySQL", e)

    def break_connection(self, connection, cursor):
        """
        purpose: help function that break with database
        input: connection,cursor
        output: None
        """
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    # get query result from database
    def get_result(self):
        """
        purpose: get result from the database
        input:  (connect info.) host,database,user,password;
                (query) mySql_select_Query
        output: requested result
        """
        # set up and test connection
        connection = self.set_connection()
        # read as dataframe
        frame = pd.read_sql(self.query, connection)
        pd.set_option('display.expand_frame_repr', False)

        # break with database
        cursor = connection.cursor()
        # select records from the table
        #    cursor.execute(mySql_select_Query)
        # fetch result
        #    record = cursor.fetchall()
        # print(record)
        self.break_connection(connection, cursor)
        return frame

'''
receive input and read jason file
'''
class Input(object):
    def __init__(self, file_dir, host, database, user, password):
        self.file_dir = file_dir
        self.host = host
        self.database = database
        self.user = user
        self.password = password
    def read_jason(self):
        '''
        :param file_dir: the dir of the jason file, of string type
        :return:    lay_out: contains chart/markdowns information in order, type dict
                        -- e.g. lay_out={0:[chart/markdown in one section]}
                    lay_out_rows: record each content of multipage app, type dict
                        -- e.g. lay_out_rows= {"D": ["A","B"],"E": ["D","C"]}
                    charts_list, comment_list: contains name for chart/comments, type list
                        -- e.g. charts_list = ["A","B","C"], "markdowns": ["D","E"],
        '''
        file_dir = self.file_dir
        # layout helper
        lay_out = {}
        lay_out_rows = {}
        # Opening JSON file
        f = open(file_dir)

        # returns JSON object as a dictionary
        data = json.load(f)

        # Iterating through the json list
        data_tempt = {} # use to hold content before deciding whether it is a chart or not
        charts_list = [] # record the charts name
        comment_list = [] # record the markdowns name
        for i in data:
            # print(i)
            if i[0:len("markdowns")].lower() == "markdowns": # not handle
                comment_list = data[i]
            elif i[0:len("charts")].lower() == "charts":
                charts_list = data[i] # this will be a list that mark which content is a chart
            elif i[0:len("layout")].lower() == "layout":
                lay_out_rows = data[i]  # this will be a dict of content for each page
            else:
                # first store before request the query
                data_tempt[i] = data[i]
                # raise NameError('Wrong Section Name')
        # Closing file
        f.close()

        # manipulate charts
        for i in data_tempt:
            if i in charts_list:
                mySql_select_Query = []
                chart_def = []
                x = []
                y = []
                title = []
                for j in data_tempt[i]:
                    # record query and chart definition(what type of chart)
                    mySql_select_Query.append(j["query"])
                    chart_def.append(j["chart_def"])
                    # check if defined title
                    if "title" in j.keys():
                        title.append(j["title"])
                    else:
                        title.append("")
                    # check if defined x,y-axis
                    if "x" in j.keys() and "y" in j.keys():  # allow xy mapping
                        x.append(j["x"])
                        y.append(j["y"])
                    else:
                        x.append(None)
                        y.append(None)
                lay_out[i] = [mySql_select_Query, chart_def, x, y, title]
            elif i in comment_list:
                lay_out[i] = data_tempt[i]

        # return mySql_select_Query, chart_def, x, y
        return charts_list, comment_list, lay_out, lay_out_rows

    def handle_query(self):
        charts_list, comment_list, lay_out, lay_out_rows = self.read_jason()
        '''
        for later use: tot_record,tot_chart_config, tot_x, tot_y, tot_title: keys are 0,1,2,3...(int), type dict
                            -- only for chart 
                            -- e.g. tot_record = {0:[result in this section in dataframe]}
                       tot_mark: keys are 0,1,2,3... (int), type dict
                            -- mark the markdowns 
                       lay_out_rows, remain unchanged from the previous part, type dict
        '''
        tot_record = {}
        tot_chart_config = {}
        tot_x = {}
        tot_y = {}
        tot_title = {}
        # for markdown
        tot_mark = {}

        counter = 0
        corr_index = {} #link name with counter
        for _ in lay_out:
            if _ in charts_list:
                corr_index[_] = counter
                mySql_select_Query, chart_def, x, y, title = lay_out[_]
                # handle input and store query and chard_def into seperate list
                record = []
                chart_config = []
                # print(mySql_select_Query)
                if len(mySql_select_Query) != 0:
                    assert len(chart_def) == len(mySql_select_Query), print("no match for chart and data")
                    for query in mySql_select_Query:
                        # check query type
                        assert type(query) == str, print("wrong query type, please input as a string")

                        # check sql injection, need improve
                        assert query.find(';', 0, -1) == -1, print('allowed only one query at a time')
                        assert bool(re.search("select", query, re.IGNORECASE)) is True, print("invalid query")
                        assert query.lower().find("select") == 0, print("invalid query")

                        # get query result
                        db = Database(self.host, self.database, self.user, self.password, query)
                        res = db.get_result()
                        record.append(res)  # st the result of the query, not check NONE here, need further attention

                    # copy chart definition
                    chart_config.extend(chart_def)
                tot_record[counter] = record
                tot_chart_config[counter] = chart_config
                tot_x[counter] = x
                tot_y[counter] = y
                tot_title[counter] = title
                counter += 1
            elif _ in comment_list: #not handle
                corr_index[_] = counter
                tot_mark[counter] = lay_out[_]
                counter +=1
            else:
                continue


        # rearrange lay_out_rows part
        lay_out_rows_tempt = {}
        for i in lay_out_rows.keys():
            pre_row = lay_out_rows[i]
            tempt_row = []
            for j in range(len(pre_row)):
                tempt_row.append(corr_index[pre_row[j]])
            lay_out_rows_tempt[i] = tempt_row
        lay_out_rows = lay_out_rows_tempt

        return tot_record,tot_chart_config, tot_x, tot_y, tot_mark, lay_out_rows, tot_title, corr_index








