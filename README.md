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

#### 1. GitHub Cloning:
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
