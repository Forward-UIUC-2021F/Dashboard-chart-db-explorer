# Dashboard-chart-db-explorer
This is a pure Python framework aims to visualize data (stored in sql database) with an online dashboard. It helps define a dashboard with a set of sql queries and their associated definition for the output chart, and allows reusing without having to rewrite the program.   

At present, the framework mainly applies Dash, whose links to its tutorials and other references are attached at the end of this file. 

## Table of contents
* [Functional Design](#Functional-Design)
* [Algorithmic Design](#Algorithmic-Design)
* [Reference](#Reference)

## Functional Design
User that requests the web dashboard can only access `input.py`. First install os module locally, and then store queries (type string) and the corresponding table definitions (typr string) into mySql_select_Query (type list) and chart_def (type list). To generate web dashboard, simply run helpfunction `run()`.

```
import os

# intialization
mySql_select_Query = [...] 
chart_def = [...]

# run the program
run()
```

## Algorithmic Design

## Reference
* [Essay That Introduces Dash](https://medium.com/plotly/introducing-dash-5ecf7191b503)
* [Dash Github](https://github.com/plotly/dash/)
* [Dash Online Tutorial](https://dash.plotly.com/)
