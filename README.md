# Dashboard-chart-db-explorer
This is a pure Python framework aims to visualize data (stored in sql database) with an online dashboard. It helps define a dashboard with a set of sql queries and their associated definition for the output chart, and allows reusing without having to rewrite the program.   

At present, the framework mainly applies Dash, whose links to its tutorials and other references are attached at the end of this file. 

## Table of contents
* [Functional Design](#Functional-Design)
* [Algorithmic Design](#Algorithmic-Design)
* [Reference](#Reference)

## Functional Design
User that requests the web dashboard need to prepare a .JSON file that contains queries and chart_def, in the form that is shown below:
```
{"items": [
        {"query": "...;", "chart_def": "table"},
        {"query": "...;", "chart_def": "table"}
    ]
}
```
First install os module locally, and import it. User can get access to a help function called `run(file_dir)`, which receive a parameter called file_dir that points to the prepared json file as shown above. The help function pass the file_dir as an argv.  

```
import os
def run(file_dir): 
    os.system("python app.py " + file_dir)
    return
```
To generate web dashboard, simply run helpfunction `run(file_dir)`.
```
# run the program
run("input.json") 
```

## Algorithmic Design

## Reference
* [Essay That Introduces Dash](https://medium.com/plotly/introducing-dash-5ecf7191b503)
* [Dash Github](https://github.com/plotly/dash/)
* [Dash Online Tutorial](https://dash.plotly.com/)
