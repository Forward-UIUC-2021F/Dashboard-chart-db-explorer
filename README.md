# Dashboard-chart-db-explorer
This is a pure Python framework aims to visualize data (stored in sql database) with an online dashboard. It helps define a dashboard with a set of sql queries and their associated definition for the output chart, and allows reusing without having to rewrite the program.   

At present, the framework mainly applies Dash, whose links to its tutorials and other references are attached at the end of this file. 

## Table of contents
* [Functional Design](#Functional-Design)
* [Algorithmic Design](#Algorithmic-Design)
* [Reference](#Reference)

## Functional Design
* __Input__  
User that requests the web dashboard need to prepare a .JSON file that contains queries and chart_def, in the form that is shown below.
Separate query is store in "items":
```
"item": [
        {"query": "...;", "chart_def": "table"},
        {"query": "...;", "chart_def": "table"}
    ]
```
To-be-joined queries are stored in "items", whose result will later joint according to the concatenate method indicate in the field:
```
"items": [
        {"query": "...;"},
        {"query": "...;","chart_def": "..."},
        {"chart_def": "..."},
        {"concatenate": "col (or row)"}
  ]
```
The example input can be:
```
{
"item": [...],
"items": [...]
}
```
* __Run__   
First install os module locally, and import it. User can get access to a help function called `run(file_dir)`, which receive a parameter called file_dir that points to the prepared json file as shown above. The help function pass the file_dir as an argv.  

```
import os
def run(file_dir): 
    ...
    (command to run the app with input file directory as additional argument)
    ...
    return
```
To generate web dashboard, simply run helpfunction `run(file_dir)`.
```
# run the program
run("input.json") 
```

## Algorithmic Design
The user store the query and chart_def in pairs inside of the JSON file and pass the file directory into the "dashboard generator". The `helpfunc.py` file takes this information, it reads the queries from the file and pass them to the database, and get the query result. The `chart_def.py` file takes the result and the (unchanged) chart_def and transfer the result into chart configurations according to the char_def. The configuration and the chart_def can be turned into dashboard in the `app.py` file once the file is run by the user.
The following is the diagram that depicts the process that is described in the previous paragram.

![This is an image](/algorithm_diagram.png)

Present available chart type includes: table, scatter, line chart, histogram

## Reference
* [Essay That Introduces Dash](https://medium.com/plotly/introducing-dash-5ecf7191b503)
* [Dash Github](https://github.com/plotly/dash/)
* [Dash Online Tutorial](https://dash.plotly.com/)
