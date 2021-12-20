# Dashboard-chart-db-explorer (Final Document)
This is a pure Python framework aims to visualize data (which is stored in sql database) with an online multipage-dashboard (supported up to 2 pages). The module helps define a dashboard with a set of sql queries and their associated definition for the output chart, and, as a result, allows reusing without having to rewrite the program.   

At present, the framework mainly applies Dash (links to its tutorials and other references are attached at the end of this file). 

## Table of contents
* [Set up](#Set-up)
* [Functional Design](#Functional-Design)
* [Algorithmic Design](#Algorithmic-Design)
* [Issues and Future Work](#Issues-and-Future-Work)
* [Reference](#Reference)

## Set Up
To install the module's dependencies, refer to the `requirements.txt`, which containes all of the python dependencies needed at my project's root.
```
pip install -r requirements.txt 
```

Below is an overall breakdown of my repo's file structure.
```
db_generator/
    - requirements.txt
    - app/ 
    	-- main.py
        -- app.py
	-- chart_def.py
	-- helpfunc.py
	-- input.json
	-- layout.py
    - assets/
        -- style.css
```
Notice that the `main.py` file need customize (need include user's database information to connect to the database) and the `input.json` file the an example input file for query and chart definition (the detailed instruction to write your own input file is included below).

## Functional Design
#### Input Definition 

User that requests the web dashboard need to prepare a `.JSON` file that contains layout (of the dashboard), queries and their corresponding chart_def, or other elements like markdown. By default, the x y mapping is in the order of the selected element in the corresponding query, But the users can also choose to write x y mapping explicitly. Here, the index(idx) corresponds to the order (start from 0) of the selected elements in the given query. For example, if the query select id and average_vote, then {...,"x":[1],...} means that we take average_vote as the x axis.   

An example `.json` file is presented below,
```
{
  "name_it_your_self 1": [
    {"query": "...;", "chart_def": "histogram/line chart/scatter/histogram","title": "..." (,"x": [1], "y": [0])}
  ],
  "name_it_your_self 2": ["...this is for markdown..."],
  "charts": ["name_it_your_self 1"],
  "markdowns": ["name_it_your_self 2"],
  "layout": {"name_it_your_self 2": ["name_it_your_self 1","name_it_your_self 2",...],"name_it_your_self 3": [...]}
}

```
#### Take-aways:
1. for chart section: 
	1) user can freely name the chart by replacing "name_it_your_self 1" with the name
	2) "query", "chart_def" and "title" are required
	3) "x", "y" (stands for xy mapping) are optional
	4) at present, we only support histogram/line chart/scatter/table 
2. for markdown definition:
	1) user can freely name the chart by replacing "name_it_your_self 2" with the name
3. what is "charts":
	1) it lists the name of the chart 
4. what is "markdowns"
	1) it lists the name of the markdown
5. what is layout
	1) it defines the subpage and its content
	2) user can use markdown as the header of the sub page, or they can use random name, which will not be shown on the page


#### Starting Code   

First install os module locally, and import it. User can get access to a help function called `run(file_dir)`, which receive a parameter called file_dir that points to the prepared json file as shown above. The help function pass the file_dir as an argv.  

```
class Input(object):
    def __init__(self, file_dir, host, database, user, password):
        self.file_dir = file_dir
        self.host = host
        self.database = database
        self.user = user
        self.password = password
    def run(self):
        ...
    	(command to run the app with input file directory and the database information as additional arguments)
    	...
        return
```
To generate web dashboard:
```
# run the program
initial = Input("XXX.json", '...', '...', '...', '...')
initial.run()
```

#### Demo video

https://user-images.githubusercontent.com/89476239/146725588-da276c99-4ecc-4b5e-8c45-0075d2e64f10.mp4

A clearer version see upload.

## Algorithmic Design
The user store the query and chart_def in pairs inside of the JSON file and pass the file directory into the "dashboard generator". The `helpfunc.py` file takes this information, it reads the queries from the file and pass them to the database, and get the query result. The `chart_def.py` file takes the result and the (unchanged) chart_def and transfer the result into chart configurations according to the char_def. The configuration and the chart_def can be turned into dashboard in the `app.py` file once the file is run by the user.

The following is the diagram that depicts the process that is described in the previous paragram.

![This is an image](/algorithm_diagram.png)

Present available chart type includes: table, scatter, line chart, histogram. And the result will be shown on http://127.0.0.1:8050/ protal.

## Issues and Future Work
1. At present, the dashborad has limited supported chart types (only histogram/line chart/scatter/table) with simple styles; 
2. It supports at most two pages.  
3. The dashboard is hosted on a specified address http://127.0.0.1:8050/. 

## Reference to Package
* [Essay That Introduces Dash](https://medium.com/plotly/introducing-dash-5ecf7191b503)
* [Dash Github](https://github.com/plotly/dash/)
* [Dash Online Tutorial](https://dash.plotly.com/)
* [Dash Draggable Package(github)](https://github.com/MehdiChelh/dash-draggable)


