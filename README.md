# 2_PhonePe-Pulse-Data-Visualization-and-Exploration
This repository consists of all the analysis done for the Phonepe Pulse project.

## What is PhonePe:
PhonePe is a mobile payment platform using which you can transfer money using UPI, recharge phone numbers, pay utility bills, etc. PhonePe works on the Unified Payment Interface (UPI) system and all you need is to feed in your bank account details and create a UPI ID.
To know more about the app, [Click here](https://www.phonepe.com/)

## What is PhonePe Pulse:
The PhonePe Pulse website showcases more than 2000+ Crore transactions by consumers. With over 45% market share, PhonePe's data is representative of the country's digital payment habits. The insights on the website and in the report have been drawn from two key sources - the entirety of PhonePe's transaction data combined with merchant and customer interviews.
Know more about [PhonePe Pulse](https://www.phonepe.com/pulse/)

## Phonepe Pulse Data Visualization and Exploration: A User-Friendly Tool Using Streamlit and Plotly
### Aim of project:
The project is about analysing and generating insights about the data from **PhonePe Pulse system**, and creating a visual image of analysis done onto a **streamlit app** for viewing. By the end of this project, we will have understood how the data is changing every year.

### Data source:
The data for this project is available on the official **github** account of Phonepe Pulse, the link to which is given below.
[PhonePe Pulse Repo](https://github.com/PhonePe/pulse.git)

### Project Domain:
This particular project belongs to the **fintech** domain, where we make analysis on the financial attributes of transactions and users.

### Tools/Techniques used:
Github Cloning, Python, Pandas, MySQL, Streamlit and Plotly.

### Project Overview:
We have made use of the above tools in this project, and an outline of how it went about is shared here.

#### 1. Data Extraction - GitHub Cloning
Firstly, in order to be able to use this data we would have to **download** the PhonePe pulse data from their official Github Repository. Although, download is an option, here we have made use of a concept called **cloning**, where we *create a replica of the repository onto our local system* in the destination we want it to be stored. Once we do that, the repository is mirrored in the exact way onto our local system.

In our case, we have cloned the repository using the below code in the command line where *https://github.com/PhonePe/pulse.git* is the repository having the data

```
C:\Users\****>git clone https://github.com/PhonePe/pulse.git
Cloning into 'pulse'...
remote: Enumerating objects: 15229, done.
remote: Counting objects: 100% (27/27), done.
remote: Compressing objects: 100% (26/26), done.
remote: Total 15229 (delta 3), reused 1 (delta 1), pack-reused 15202
Receiving objects: 100% (15229/15229), 21.95 MiB | 17.70 MiB/s, done.
Resolving deltas: 100% (7745/7745), done.
Updating files: 100% (7921/7921), done.
```
Once the cloning is done, we have view where it is stored using the *cd pulse* command to navigate to the folder, and *dir* to view the contents of the folder..

```
C:\Users\****>cd pulse

C:\Users\****\pulse>dir
 Volume in drive C is Windows-SSD
 Volume Serial Number is 1836-CD75

 Directory of C:\Users\*****\pulse

31-05-2024  12:19    <DIR>          .
31-05-2024  12:19    <DIR>          ..
31-05-2024  12:19                22 .gitignore
31-05-2024  12:19    <DIR>          data
31-05-2024  12:19             2,406 LICENSE
31-05-2024  12:19            20,861 README.md
               3 File(s)         23,289 bytes
               3 Dir(s)  416,571,801,600 bytes free
```
The above code gives an idea of the contents and size of each of the files present in the folder.

#### 2. Data Transformation - Python (Pandas):
We have used **Python** as our language of analysis and used the **VS code editor**. We have leveraged the powerful **Pandas** library in Python to transform the dataset from *JSON format into a structured dataframe*. Pandas facilitated data manipulation, cleaning, and preprocessing, ensuring the data was ready for analysis. Some of these transformations made on the raw data included acting on missing data, renaming, etc.. Once the data was converted to *dataframes*, we make a  copy of them as csv files.

#### 3. Data Storage - MySQL (Dataframe to Data Tables):
Once we have the dataframes created for all the extracted data, we are going to be loading them to our **MySQL database** since our project is designed to take inputs from the database only. For this purpose, we have made use of **mysql-connector-python**, a library in python to establish a connection from python to MySQL database, enabling *seamless integration* of the transformed dataset. By this method, the data was efficiently inserted into relevant tables for storage and retrieval. 

#### 4. Data display - Streamlit:
Now that our data extraction, transformation and storage is done, we are moving with how we can display the data from our python editor. For this we make use of the **streamlit** library in python. This allows us to create interactive web like application, for a user-friendly framework of data visualization and analysis. Streamlit is very efficient in generating creative visuals and styles of application and we can choose to modify it as per we want by incorporating CSS styling also. We have already run through what streamlit can do in our previous project of [YouTube Data Analysis](https://github.com/sanjuhyacinth/1_YoutubeDataHarvesting). Streamlit has a comprehensive set of functions and features that goes well with python to display almost anything we want to, a reference to the multiple offerings of the mdoule can be learnt from this [streamlit documentation](https://docs.streamlit.io/)

#### 5. Data Visualization - Plotly:
Now we are going to be visualizing the data we have with the help of plotly in python onto our streamlit app. [Plotly](https://plotly.com/) is an open-source module of Python that is used for data visualization and supports various graphs like line charts, scatter plots, bar charts, histograms, area plots, etc. Plotly produces interactive graphs, can be embedded on websites, and provides a wide variety of complex plotting options. [Plotly Express](https://plotly.com/python/plotly-express/) is a built-in part of the plotly library, and is the recommended starting point for creating most common figures. We can learn and experiment with various visuals of plotly from these links shared above.

### Important libraries used in Python:
The libraries used in python for this project are:

- import os
- import json
- import pandas as pd
- import streamlit as st
- from streamlit_option_menu import option_menu
- import plotly.express as px
- import mysql.connector
- from PIL import Image

### Streamlit App contents:
Our streamlit app has a 3-4 page report

#### a. Home:
The home page has details about PhonePe, PhonePe Pulse, the general picture of what data is available and where we are extracting the data from.

#### b. Top Visuals:
This section consists of 2 more tabs; *Geo-visualization and Other visualizations*. The Geo-Visualization tab displays data overall and with filters in a **map** form. we specifically use the *plotly.choropleth_mapbox* for this. There are also filters we can use with this. The next tab is the Other Visualization tab which provides filter on one attribute of the data and has a set of questions not visualized in the geo viz tab. This is useful for understanding the data as a whole.

#### c. Top Insights:
Top Insights page of the app throws light on the important questions that need to be visualized in the form of pie, donut and bar charts. Additionally, this tab also has an *insights* button which gives an idea by word on what is observed in the data and why it is the way it is.

#### d. About:
The about section at the last is where the **project** details are shared.

