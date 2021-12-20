# -*- coding:utf-8 -*-
"""
purpose: define the chart/markdown html layout according to record and chart_definition
author: DAIDAI_5
date: 2021/09/23
input: tot_mark, tot_record, tot_chart_config, tot_x, tot_y, tot_title from helpfunc file
output:  | tyoe | description
    res  | dict | chart and markdown html layout
"""
##### dash related #####
from dash import dcc
from dash import html
from dash import dash_table
import plotly.graph_objs as go
import plotly.express as px
##### database related #####
from helpfunc import tot_mark, tot_record, tot_chart_config, tot_x, tot_y, tot_title


def table(df,idx,title):
    '''
    :param df: dataframe with chart def = "table"
    :param idx: num query
    :return result: html arrangement with table configuration (to app)
    :problem:
    '''
    # handle columns information
    #col_name = df.dtypes.index
    #col_values = df.values
    #col_dict = {}
    #for i in range(len(col_name)):
    #    col_dict[col_name[i]] = df.columns[i]
    # produce tb configuration

    # customize
    # width = 450 * (len(df.columns))
    # height = min(500,100*len(df.values))
    # if title == '':
    #     title = "Table {idx}: Result for Query {idx}".format(idx = idx)
    # else:
    #     title = "Table {idx}: ".format(idx = idx) + title
    # table arrangement
    if len(df.values)<20:
        tb = dash_table.DataTable(
            id="{idx}".format(idx=idx),
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            style_cell=dict(textAlign='left'),
            #style_header=dict(backgroundColor="paleturquoise"),
            #style_data=dict(backgroundColor="lavender"),
            # style_table={
            #     'height': height,
            #     'width': width
            # },
            export_format='xlsx',
            export_headers='display',
        )
    else:
        tb = dash_table.DataTable(
            id="{idx}".format(idx=idx),
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            style_cell=dict(textAlign='left'),
            #style_header=dict(backgroundColor="paleturquoise"),
            #style_data=dict(backgroundColor="lavender"),
            page_current=0,
            page_action='custom',
            style_table={
                # 'height': '300px',
                'overflowY': 'auto',
                # 'width': width
            },
            fixed_rows={'headers': True},
            export_format='xlsx',
            export_headers='display'
        )
    # result = dash_draggable.ResponsiveGridLayout(
    #     html.Div([
    #     tb,
    #     html.Label(title, style={'textAlign':'center'})
    # ]))
    '''
    v2
    '''
    result = html.Div([
        html.H3(title, style={'textAlign':'center'}),
        tb
    ])

    '''
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i}
                 for i in df.columns],
        data=df.to_dict('records'),
        style_cell=dict(textAlign='left'),
        style_header=dict(backgroundColor="paleturquoise"),
        style_data=dict(backgroundColor="lavender"),
        style_table={
            'height': 500,
            'overflowY': 'scroll',
            'width': 1000
        }
    )
    '''
    return result


def scatter(df,idx,x,y,title):
    '''
    :param df: dataframe with chart def = "scatter"
    :param idx: num query
    :return: html arrangement with scatter configuration (to app)
    '''
    # customize
    columns = [i for i in df.columns]
    # if title == '':
    #     title = "Graph {idx}: Result for Query {idx}".format(idx = idx)
    # else:
    #     title = "Graph {idx}: ".format(idx = idx) + title
    if x == []:
        #scatter graph designer
        if len(columns) == 2:
            fig = px.scatter(df, x=columns[0], y=columns[1])
            sct = dcc.Graph(figure=fig,responsive=True)
            # result = dash_draggable.ResponsiveGridLayout(
            #     html.Div([
            #         sct,
            #         html.Label(title, style={'textAlign':'center'})
            #             ])
            # )
            result = html.Div([
                    html.H3(title, style={'textAlign':'center'}),
                    sct
                        ])
            return result
        else:
            title = "Result for Query {idx} Cannot Output as Scatter".format(idx = idx)
            result = html.Div([
                html.Label(title),
            ])
            return result
    else: #have extra xy mapping
        if len(x) == 1 and len(y) == 1:
            fig = px.scatter(df, x=columns[x[0]], y=columns[y[0]])
            sct = dcc.Graph(figure=fig,responsive=True)
            # result = dash_draggable.ResponsiveGridLayout(
            #     html.Div([
            #         sct,
            #         html.Label(title, style={'textAlign':'center'})
            #             ])
            # )
            result = html.Div([
                    html.H3(title, style={'textAlign':'center'}),
                    sct
                        ])
            return result
        else:
            title = "Result for Query {idx} Cannot Output as Scatter".format(idx = idx)
            result = html.Div([
                html.H3(title),
            ])
            return result

def line_chart(df,idx,x,y,title):
    '''
    :param df: dataframe with chart def = "line chart"
    :param idx: num query
    :param x,y: xy mapping
    :return: html arrangement with line chart configuration (to app)
    '''
    # customize
    columns = [i for i in df.columns]
    # if title == '':
    #     title = "Graph {idx}: Result for Query {idx}".format(idx = idx)
    # else:
    #     title = "Graph {idx}: ".format(idx = idx) + title
    #scatter graph designer
    if x == []:
        if len(columns) == 2:
            #fig = go.Figure(data=[go.Scatter(x=df[columns[0]].values, y=df[columns[1]].values)])
            fig = px.line(df, x=columns[0], y=columns[1], markers=True)

            lct = dcc.Graph(
                id="{idx}".format(idx=idx),
                figure=fig
            )
            result = html.Div([
                    html.H3(title, style={'textAlign':'center'}),
                    lct
                ])
            return result
        else:
            title = "Result for Query {idx} Cannot Output as Line Chart".format(idx = idx)
            result = html.Div([
                html.H3(title),
            ])
            return result
    else: # has extra xy mapping
        if len(x) == 1 and len(y) == 1:
            #fig = go.Figure(data=[go.Scatter(x=df[columns[x[0]]].values, y=df[columns[y[0]]].values)])
            fig = px.line(df, x=columns[x[0]], y=columns[y[0]], markers=True)

            lct = dcc.Graph(
                id="{idx}".format(idx=idx),
                figure=fig
            )
            result =html.Div([
                    html.H3(title, style={'textAlign':'center'}),
                    lct
                ])
            return result
        elif len(x) == 1 and len(y) != 1:
            #fig = go.Figure(data=[go.Scatter(x=df[columns[x[0]]].values, y=df[columns[y[0]]].values)])
            fig = go.Figure()
            # Create and style traces
            for i in range(len(y)):
                fig.add_trace(go.Scatter(x=df[columns[x[0]]], y=df[columns[y[i]]], name=columns[y[i]]))

            lct = dcc.Graph(
                id="{idx}".format(idx=idx),
                figure= fig
            )
            result = html.Div([
                    html.H3(title, style={'textAlign':'center'}),
                    lct
                    ])
            return result
        else:
            title = "Result for Query {idx} Cannot Output as Line Chart".format(idx = idx)
            result = html.Div([
                html.Label(title),
            ])
            return result

def hist(df,idx,x,y,title):
    '''
    :param df: dataframe with chart def = "line chart"
    :param idx: num query
    :param x,y: xy mapping
    :return: html arrangement with line chart configuration (to app)
    :note: if
    '''
    # customize
    x_list = []
    columns = [i for i in df.columns]
    num_bar = len(columns) #number of values
    flag = 0
    # we can only allow 8 bars in total
    if num_bar >= 8:
        num_bar = 8

    if x == []:
        x_list = [_+1 for _ in range(len(df[columns[0]].values))]
    else:
        for i in x:
            x_list.append(df[columns[i]].values)
        x_list = x_list[0].tolist()
    if y != []: #has extra y def then present all
        flag = -1
        num_bar = len(y)
    #print(x_list)
    #print(num_bar)
    #print(y)
    # if title == '':
    #     title = "Graph {idx}: Result for Query {idx}".format(idx = idx)
    # else:
    #     title = "Graph {idx}: ".format(idx = idx) + title
    data_list = []
    if flag == -1:
        #fig = px.histogram(df[columns[y[0]]].values, x=x_list)
        for i in range(len(y)):
            tempt = {'x': x_list, 'y' : df[columns[y[i]]].values, 'type': 'bar','name' : columns[y[i]]}
            data_list.append(tempt)
    else:
        for i in range(num_bar):
            tempt = {'x': x_list, 'y' : df[columns[i]].values, 'type': 'bar','name' : columns[i]}
            data_list.append(tempt)

    fig ={'data': data_list}
    hist_ = dcc.Graph(
        id="{idx}".format(idx=idx),
        figure = fig
    )

    result = html.Div([
            html.H3(title, style={'textAlign':'center'}),
            hist_
        ])
    #print(result)
    return result


'''
only handle with tot_record (contains res for each section) and tot_chart_config (contains chart def for each section)
transfer to app available config

for later use:  res, contains the true layout, type dict
                tot_chart_config, after some deletion, type dict
'''
number = len(tot_record)
# print(tot_record)
res = {}
i = 0
for _ in tot_record: #_ is keys, 0,1,2,3... (int)
    if tot_record[_] is None:
        del tot_chart_config[_] # delete the "ineffective" query's chart definition
        del tot_title[_]
        del tot_x[_]
        del tot_y[_]
        number -= 1
        continue
    tempt_res = []
    for j in range(len(tot_record[_])):
        if tot_chart_config[_][j].lower() == 'table':
            tempt_res.append(table(tot_record[_][j],i,tot_title[_][j]))
        elif tot_chart_config[_][j].lower() == 'scatter':
            if tot_x[_][j] is None:
                tempt_res.append(scatter(tot_record[_][j],i,[],[],tot_title[_][j]))
            else:
                tempt_res.append(scatter(tot_record[_][j],i,tot_x[_][j],tot_y[_][j],tot_title[_][j]))
        elif tot_chart_config[_][j].lower() == 'line chart':
            if tot_x[_][j] is None:
                tempt_res.append(line_chart(tot_record[_][j],i,[],[],tot_title[_][j]))
            else:
                tempt_res.append(line_chart(tot_record[_][j],i,tot_x[_][j],tot_y[_][j],tot_title[_][j]))
        elif tot_chart_config[_][j].lower() == "histogram":
            if tot_x[_][j] is None:
                tempt_res.append(hist(tot_record[_][j],i,[],[],tot_title[_][j]))
            else:
                tempt_res.append(hist(tot_record[_][j],i,tot_x[_][j],tot_y[_][j],tot_title[_][j]))
        else: # this error might can be checked/avoided in earlier steps
            tempt_res.append("unavailable chart type") # mark unsupported chart type
        i += 1
    res[_] = tempt_res
for _ in tot_mark:
    res[_] = html.H3(tot_mark[_])

