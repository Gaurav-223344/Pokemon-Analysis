# Pokemon Analysis


## Table of Content
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Run](#run)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [Technologies Used](#technologies-used)
  * [Contributor](#contributor)

## Overview
This is a pokemon analysis web application that includes statistical analysis and some interactive visualization.

## Motivation
I'm a big fan of Japanese anime and I watched a lot of anime. I used to watch Pokemon when I was kid. There are a variety of Pokemon with amazing powers, So I decided to analyze them.

## Technical Aspect
This project is divided into two part:
1. Analysing data in jupyter notebook with pandas and plotly. 
2. Making streamlit web application by using these analytics strategies.

## Installation
The Code is written in Python 3.8. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Run

#### Linux and macOS User
Open terminal :
```bash
$ python3 app.py
```
This sources will help you to run this project:\
for macOS user : https://www.maketecheasier.com/run-python-script-in-mac \
for Linux user : https://www.educative.io/edpresso/how-to-run-a-python-script-in-linux

#### Windows User
Open Command Prompt :
```bash
$ cd /ProjectLocation
```
```bash
$ streamlit run app.py
```
This will help you if you are windows user and also a beginner :
https://github.com/pettarin/python-on-windows

## Deployement on Heroku
Set the environment variable on Heroku as mentioned in _STEP 1_ in the __Run__ section. [[Reference](https://devcenter.heroku.com/articles/config-vars)]

![](https://i.imgur.com/TmSNhYG.png)

Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Directory Tree 
```
├── .gitignore
├── Analysis.ipynb
├── Finally_Fully_Scraped_Pokemon_Data.csv
├── Procfile
├── analysisfunction.py
├── requirements.txt
├── app.py
├── setup.sh
└── README.md
```
## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://cdn-images-1.medium.com/max/1024/1*u9U3YjxT9c9A1FIaDMonHw.png" width=200>](https://streamlit.io/) [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/3/37/Plotly-logo-01-square.png" width=170>](https://plotly.com
)

## Contributor
[Gaurav-Gaikwad](https://github.com/Gaurav-223344)

