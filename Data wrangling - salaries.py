import pandas as pd

df = pd.read_csv(r"C:/Users/osgou/Programming/Courser_IBM_Projects/Web Scrapping/m1_survey_data(2).csv")


print(df["CompFreq"].unique())                  #prints unique values from column "CompFreq"


def normalize_compensation(row):                #function to read the value from "CompTotal" column depending on value in "CompFreq" column and calculating yearly value for all results.
    if row['CompFreq'] == 'Yearly':
        return row['CompTotal']
    elif row['CompFreq'] == 'Monthly':
        return row['CompTotal'] * 12
    elif row['CompFreq'] == 'Weekly':
        return row['CompTotal'] * 52
    else:
        return
    



df["NormalizedAnnualCompensation"] = df.apply(normalize_compensation, axis=1)           #reads the value from the function, "apply" passes each row seperately to the function as a parameter "row", getting in result a value for each row seperately. 
                                                                                        #axis = 1 is "for each row", axis = 0 is "for each column"
