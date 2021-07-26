# Flask Task Chatbot 

Flask Task Chatbot is a simple chatbot created with flask for Python Junior Developer Job Task at Neuro.net. The chatbot's purpose is to ask users for a recommendation rating about the company and reporting to the results to a Microsoft Azure Database.

## Installation


This samples requires prerequisites in order to run, the required packages are found in requirements.txt

```bash
pip install -r requirements.txt
```
## Overview
This Rule-based Chatbot was not made with any external or special bot library but rather with pure Python Language from scratch. Once the repository is cloned the user heads to http://localhost:5000 and is asked for his name. A short conversation with this bot is then held and results are stored on an Azure Cloud Services Database created for experimental purposes only.


## Usage
After cloning thie repository enter the following commands into the command shell of your virtual environment.

```sh
pip install -r requirements.txt
export FLASK_APP=app.py
flask run
```

To View the latest ratings results head back to your command shell and enter the following command:
```
flask ratings
```



## References 

This code is written in accordance to the PEP8 Style Guide for Python Code

[PEP8](https://www.python.org/dev/peps/pep-0008/) 

Graphical interface taken and slightly modified from:
[bbbootstrap](https://bbbootstrap.com/snippets/simple-chat-application-57631463)
