# BMI-calculator
###Data Representation and Querying Project 2016

This repository contains code and information for a third-year undergraduate project for the module **Data Representation and Querying**.
The module is taught to undergraduate students at [GMIT](http://www.gmit.ie) in the Department of Computer Science and Applied Physics.
The lecturer is [Ian McLoughlin](https://ianmcloughlin.github.io).

### Project Overview
We have created a Single-Page Web Application (SPA) that lets users to calculate their BMI value, to know their ideal weight.
This application was selected after we saw the website [bmi-calculator](http://www.bmi-calculator.net/). we are very interested in the idea. thus, we chose to create a our own version. Also, we have login model for more infomation and function.

The project was guided by the following excerpt from the project instructions:
>You are required to develop a single-page web application(SPA) written in the programming language Python using the Flask framework. You must devise an idea for a web application, write the software, write documentation explaining how the application works, and write a short user guide for it.

### Team Members
We selected to complete this project as a team.
The team members are:
- Zehua Yu
- Tangqi Feng
- Weichen Wang
- Qi Fu

works:
- Zehua Yu: introduction part(what is BMI); extension part(pictures animation); lay-out of moreInfo.html.
- Weichen Wang: lay-out of index.html and logined.html.
- Qi Fu: convert part(inches to cm/punds to kg); lay-out of register.html.
- Tangqi Feng: the whole frame; BMI caculator; login and register part(include database); connect to flask; separate different files.

### Meetings
Team meetings were held every Tuesday at 2pm in the library at GMIT's Dublin Road campus for the duration of the project.
At these meetings, the management of the project was discussed, among other topics.
The project was divided into separate tasks, and each task was assigned to team members - usually on an individual basis.
At each meeting, Tangqi Feng took notes using their laptop and assigned the tasks using GitHub Issues.

### How to run the application
The application is written using the [Flask](http://flask.pocoo.org/) library in [Python 3](https://www.python.org).
Both must be installed to run the project.

We use the [sqlite3](https://docs.python.org/2/library/sqlite3.html) package for persistence in the application.
Besides, [Flask Script](https://flask-script.readthedocs.io/en/latest/) is needed. 
This must also be installed.
However, no further configuration our setup is required, as the database is fully contained in the db directory in this repository.

Once these prerequisites are installed, the application can be run locally:
```bash
$ python webapp.py
```

if there is no data table, typing the command to create the table in the database:
```bash
$ python manage.py setup_db
```

Once the application is running, it can be accessed by pointing your browser at http://127.0.0.1:5000/ . 

### Architecture
This web application runs in [Python 3](https://www.python.org) using the [Flask](http://flask.pocoo.org/) web micro-framework and uses SQLite as a database.
Python 3 and Flask were requirements for the project, but SQLite was selected by the team.
We chose SQLite as it is easy to use and does not require much setup to get the web application up and running.
