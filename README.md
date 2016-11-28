# BMI-calculator
###Data Representation and Querying Project 2016

This repository contains code and information for a third-year undergraduate project for the module **Data Representation and Querying**.
The module is taught to undergraduate students at [GMIT](http://www.gmit.ie) in the Department of Computer Science and Applied Physics.
The lecturer is [Ian McLoughlin](https://ianmcloughlin.github.io).

### Project Overview
We have created a Simple Web Application that lets users to calculate their BMI value, to know their ideal weight. And provide login function for users to get more function and infomations.

This application was selected after we saw the website [bmi-calculator](http://www.bmi-calculator.net/). we are very interested in the idea. thus, we chose to create a our own version. 

This Web Application includes 4 pages, switched by the routes of [Flask](http://flask.pocoo.org/) server. searching/adding data to database(SQLite) is also completed by the server.

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

We use the [sqlite3](https://docs.python.org/2/library/sqlite3.html) package for login/register part in the application.
Besides, [Flask Script](https://flask-script.readthedocs.io/en/latest/) is needed. 
This must also be installed.

Install Flask:

If you are on Mac OS X or Linux, chances are that one of the following two commands will work for you:
```bash
$ sudo easy_install virtualenv
```
or even better:
```bash
$ sudo pip install virtualenv
```
One of these will probably install virtualenv on your system. Maybe it’s even in your package manager. If you use Ubuntu, try:
```bash
$ sudo apt-get install python-virtualenv
```

If you are on Windows and don’t have the easy_install command, you must install it first. Check the pip and setuptools on Windows section for more information about how to do that. Once you have it installed, run the same commands as above, but without the sudo prefix.

Once you have virtualenv installed, just fire up a shell and create your own environment. I usually create a project folder and a venv folder within:
```bash
$ mkdir myproject
$ cd myproject
$ virtualenv venv
New python executable in venv/bin/python
Installing setuptools, pip............done.
```
Now, whenever you want to work on a project, you only have to activate the corresponding environment. On OS X and Linux, do the following:
```bash
$ . venv/bin/activate
```
If you are a Windows user, the following command is for you:
```bash
$ venv\scripts\activate
```
Either way, you should now be using your virtualenv (notice how the prompt of your shell has changed to show the active environment).

And if you want to go back to the real world, use the following command:
```bash
$ deactivate
```
After doing this, the prompt of your shell should be as familiar as before.

Now, let’s move on. Enter the following command to get Flask activated in your virtualenv:
```bash
$ pip install Flask
```
A few seconds later and you are good to go.

System-Wide Installation
This is possible as well, though I do not recommend it. Just run pip with root privileges:
```bash
$ sudo pip install Flask
```
(On Windows systems, run it in a command-prompt window with administrator privileges, and leave out sudo.)

Install [Flask-Script](https://flask-script.readthedocs.io/en/latest/) with pip:
```bash
$ pip install Flask-Script
```

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
