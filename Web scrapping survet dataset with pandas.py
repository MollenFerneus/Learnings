import pandas as pd
from bs4 import BeautifulSoup                   
import requests    



dataset_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv"


df = pd.read_csv(dataset_url)               #reads the csv file using pandas


first_rows = df.head()                      #shows the top 5 rows

num_rows = df.shape[0]                      #gets the number of rows
#print(num_rows)

num_columns = df.shape[1]                   #gets the number of columns 
#print(num_columns)

data_types = df.dtypes                      #gets the dat  a type of each column

age_column = df['Age']
#print(age_column.mean())                    #prints the mean of the column "age"


country = df["Country"].value_counts()          #counts how many times the same country appears
non_repeated_countries = country[country == 1].index                #selects the countries that appeared only 1 time
#print(non_repeated_countries)




