# -*- coding:utf-8 -*-
"""
author: DAIDAI_5
date: 2021/10/31
purpose: load content for each page, store into dict
input:  multi_page from layout.py
        tot_mark,corr_index from helpfunc.py
"""

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_draggable

from layout import multi_page
from helpfunc import tot_mark,corr_index
'''
develop multi-page web app that support at most two sections
can customize to load more
'''
key_list = list(multi_page.keys())

if len(key_list) == 0:
    page1 = html.H5('empty page')
    page2 = html.H5('empty page')
elif len(key_list) == 1:
    page1 = multi_page[key_list[0]]
    page2 = html.H5('empty page')
else:  # only display three
    page1 = multi_page[key_list[0]]
    page2 = multi_page[key_list[1]]


app = dash.Dash(__name__)

url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

layout_index = html.Div([
    html.H3('This is the index page for the Dashboard'),
    dcc.Link('Navigate to Row1', href='/row-1'),
    html.Br(),
    dcc.Link('Navigate to Row2', href='/row-2'),
])

if key_list[0] in corr_index:
    if corr_index[key_list[0]] in tot_mark:
        layout_page_1 = html.Div([
            html.H1(tot_mark[corr_index[key_list[0]]]),
            html.Div(id='placeholder2'),
            dash_draggable.ResponsiveGridLayout(
                id='draggable',
                clearSavedLayout=True,
                children=[html.Li(x) for x in page1]),
            html.Br(),
            dcc.Link('Navigate to Index Page', href='/'),
            html.Br(),
            dcc.Link('Navigate to Row2', href='/row-2'),
        ])
    else:
        layout_page_1 = html.Div([
        html.Div(id='placeholder2'),
        dash_draggable.ResponsiveGridLayout(
            id='draggable',
            clearSavedLayout=True,
            children=[html.Li(x) for x in page1]),
        html.Br(),
        dcc.Link('Navigate to Index Page', href='/'),
        html.Br(),
        dcc.Link('Navigate to Row2', href='/row-2'),
        ])
else:
    layout_page_1 = html.Div([
        html.Div(id='placeholder2'),
        dash_draggable.ResponsiveGridLayout(
            id='draggable',
            clearSavedLayout=True,
            children=[html.Li(x) for x in page1]),
        html.Br(),
        dcc.Link('Navigate to Index Page', href='/'),
        html.Br(),
        dcc.Link('Navigate to Row2', href='/row-2'),
    ])

if key_list[1] in corr_index:
    if corr_index[key_list[1]] in tot_mark:
        layout_page_2 = html.Div([
            html.H1(tot_mark[corr_index[key_list[1]]]),
            html.Div(id='placeholder1'),
            dash_draggable.ResponsiveGridLayout(
                id='draggable',
                clearSavedLayout=True,
                children=[html.Li(x) for x in page2]),
            # html.Ul([html.Li(x) for x in page2]),
            html.Br(),
            dcc.Link('Navigate to Index Page', href='/'),
            html.Br(),
            dcc.Link('Navigate to Row1', href='/row-1'),
        ])
    else:
        layout_page_2 = html.Div([
        html.Div(id='placeholder1'),
        dash_draggable.ResponsiveGridLayout(
            id='draggable',
            clearSavedLayout=True,
            children=[html.Li(x) for x in page2]),
        # html.Ul([html.Li(x) for x in page2]),
        html.Br(),
        dcc.Link('Navigate to Index Page', href='/'),
        html.Br(),
        dcc.Link('Navigate to Row1', href='/row-1'),
        ])
else:
    layout_page_2 = html.Div([
        html.Div(id='placeholder1'),
        dash_draggable.ResponsiveGridLayout(
            id='draggable',
            clearSavedLayout=True,
            children=[html.Li(x) for x in page2]),
        # html.Ul([html.Li(x) for x in page2]),
        html.Br(),
        dcc.Link('Navigate to Index Page', href='/'),
        html.Br(),
        dcc.Link('Navigate to Row1', href='/row-1'),
    ])


# index layout
app.layout = url_bar_and_content_div
# "complete" layout
app.validation_layout = html.Div([
    url_bar_and_content_div,
    layout_index,
    layout_page_1,
    layout_page_2,
])


# Index callbacks
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/row-1":
        return layout_page_1
    elif pathname == "/row-2":
        return layout_page_2
    else:
        return layout_index


@app.callback(
    Output('placeholder1', 'children'),
    Input('draggable', 'figure'))
def update_layout(layout):
    return str(layout)  # str('<br />'.join([str(e) for e in layout]))

@app.callback(
    Output('placeholder2', 'children'),
    Input('draggable', 'figure'))
def update_layout(layout):
    return str(layout)  # str('<br />'.join([str(e) for e in layout]))


if __name__ == '__main__':
    app.run_server(debug=False)
