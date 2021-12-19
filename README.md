# Dashboard-chart-db-explorer (Final Document)
This is a pure Python framework aims to visualize data (which is stored in sql database) with an online multipage-dashboard (supported up to 3 pages). The module helps define a dashboard with a set of sql queries and their associated definition for the output chart, and, as a result, allows reusing without having to rewrite the program.   

At present, the framework mainly applies Dash (links to its tutorials and other references are attached at the end of this file). 

## Table of contents
* [Set up](#Set-up)
* [Functional Design](#Functional-Design)
* [Algorithmic Design](#Algorithmic-Design)
* [Issues and Future Work](#Issues-and-Future-Work)
* [Reference](#Reference)

## Set Up

## Functional Design
#### Input Definition 

User that requests the web dashboard need to prepare a `.JSON` file that contains layout (of the dashboard), queries and their corresponding chart_def, or other elements like markdown. By default, the x y mapping is in the order of the selected element in the corresponding query, But the users can also choose to write x y mapping explicitly. Here, the index(idx) corresponds to the order (start from 0) of the selected elements in the given query. For example, if the query select id and average_vote, then {...,"x":[1],...} means that we take average_vote as the x axis.   

An example `input.json` file is presented below,
```
{
  "name_it_your_self 1": [
    {"query": "...;", "chart_def": "histogram/line chart/scatter/histogram"(,"title": "...","x": [1], "y": [0])}
  ],
  "name_it_your_self 2": ["...this is for markdown..."],
  "charts": ["name_it_your_self 1"],
  "markdowns": ["name_it_your_self 2"],
  "layout": {"name_it_your_self 2": ["name_it_your_self 1","name_it_your_self 2",...],"name_it_your_self 3": [...]}
}

```
Take-aways:
1. for chart section: 
	1) user can freely name the chart by replacing "name_it_your_self 1" with the name
	2) "query" and "chart_def" are required
	3) "title" and "x", "y" (stands for xy mapping) are optional
	4) at present, we only support histogram/line chart/scatter/histogram 
2. for markdown definition:
	1) user can freely name the chart by replacing "name_it_your_self 2" with the name
3. what is "charts":
	1) it lists the name of the chart 
4. what is "markdowns"
	1) it lists the name of the markdown
5. what is layout
	1) it defines the subpage and its content
	2) user can use markdown as the header of the sub page, or they can use random name, which will not be shown on the page


#### Running Code   

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

#### Demo video

## Algorithmic Design
The user store the query and chart_def in pairs inside of the JSON file and pass the file directory into the "dashboard generator". The `helpfunc.py` file takes this information, it reads the queries from the file and pass them to the database, and get the query result. The `chart_def.py` file takes the result and the (unchanged) chart_def and transfer the result into chart configurations according to the char_def. The configuration and the chart_def can be turned into dashboard in the `app.py` file once the file is run by the user.

The following is the diagram that depicts the process that is described in the previous paragram.

![This is an image](/algorithm_diagram.png)

Present available chart type includes: table, scatter, line chart, histogram

## Issues and Future Work

## Reference
* [Essay That Introduces Dash](https://medium.com/plotly/introducing-dash-5ecf7191b503)
* [Dash Github](https://github.com/plotly/dash/)
* [Dash Online Tutorial](https://dash.plotly.com/)


