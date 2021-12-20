# -*- coding:utf-8 -*-
"""
author: DAIDAI_5
date: 2021/10/31
purpose: load content for each page, store into dict
input:  res from chart_def.py
        lay_out_rows from helpfunc.py
output:       | type | description
   multi_page | dict | content for each page
"""

def split_to_page(res, lay_out_rows):
    final_list = res.values()

    multi_page = {}
    # get each rows
    for _ in lay_out_rows.keys():
        prerow_idx = lay_out_rows[_]
        prerow_elmt = []
        for i in prerow_idx:
            prerow_elmt.append(res[i])
        multi_page[_] = prerow_elmt
    return multi_page
