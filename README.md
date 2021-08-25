# Crime-Victim-Analysis-in-Australia
Final Project - Machine Learning 

## Introduction

The aim of this project was to investigate data from the National Notifiable Disease Surveillance System (NNDSS) and establish 
what trends could be observed.

Data between 2015 and 2020 on infection rates per 100,000 people was extracted from the website, transformed into a comparable dataset and loaded into an SQLite database.

An SQLAclhemy/Flask API was created to allow data to be used in a D3.js web application that was launched on Heroku.

The application consists of an interactive dashboard of four visualisations depicting comparisons of infection rates across disease groups, states and territories and years.



## Structure
```
project 
|
|__ Resources/                 
|   |__ ABS_Crime_Victim_Data.xlsx                      # raw data            
|   |__ Final_Model_Data.csv                            # cleaned data
|   |__ Population_Australia.xls                        # raw data
|
|__ static/                 
|   |__ css/                
|   |   |__ style.css                                   # style sheet 
|   |   
|   |__ images/                                         # images folder
|   |                 
|   |__ js/
|       |__ predict.js                                  # prediction code
|
|__ templates/   
|    |__ home.html                                      # html file
|    |__ index.html                                     # html file
|    |__ learn_more.html                                # html file
|    |__ visualisation.html                             # html file
|
|__ .gitignore
|
|__ app.py                                              # flask app to launch website 
|
|__ DecisionTree_Model_DataPrep_Analysis.ipynb          # model data prep
|
|__ model.pkl                                           # model 


```

## Usage

```
The page was created using:
- HTML
- CSS
- Bootstrap 
- Javascript 
- python
- pandas 
- flask 
- heroku
- Tableau

```

## Questions 

1. Which crime is most predominant in all states? 
2. Which is the safest state in Australia? 
3. How are the crime rates progressing in each state over time?
4. Does gender and/or age play a role in the likelyhood of becoming a victim? 
5. How could our solution be used as a service? 


## Datasets 

|No.|Source|Link|
| -|-|-|
|1|Australian Bureau of Statistics|https://www.abs.gov.au/statistics/people/crime-and-justice/recorded-crime-victims/2020|


## Analysis

### Question 1: Which crime is most predominant in all states? 


Put answer here




### Question 2: Which is the safest state in Australia? 


Put answer here

### Question 3: How are the crime rates progressing in each state over time? 


Put answer here


### Question 4: Does gender and/or age play a role in the likelyhood of becoming a victim? 


Put answer here


### Question 5: How could our solution be used as a service?


Put answer here

## Summary

Put answer here


## Contributors

:small_red_triangle: Petra Moyle: (https://github.com/PetraMoyle)  
:small_red_triangle: Sri Vegunta: (https://github.com/srivegunta)    
:small_red_triangle: Rebecca Gould: (https://github.com/Bec-Gould)  