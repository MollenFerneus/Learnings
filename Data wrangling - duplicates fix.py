import pandas as pd

df = pd.read_csv(r"C:/Users/XXXXXXX/m1_survey_data.csv")     #dataframe from link: https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.cs
print(df.head())

duplicates = df.duplicated()            #returns bool if duplicates appear, true for duplicate and false for unique

print(df["Respondent"].duplicated().sum())

print("\nDuplicates: ", duplicates.sum())                 #prints the of sums the true values (duplicates) and returns the amount of duplicates

df = df.drop_duplicates()      #deletes the duplicates and saves the dataframe under new variable

print("\nDuplicates after deletion:", df.duplicated().sum())       #prints the sum of duplicates in new dataframe to verify if the duplicates were deleted

print("\nMissing values: ",df.isna().sum().sum())          #prints the missing values, then sums them by the column, then sums the columns together and prints the total of amount of missing values

print("\nMissing values in WorkLoc: ",df["WorkLoc"].isna().sum())      #prints the sum of misisng values in specific column called "WorkLoc"

print("\nRepeated values and the count: ",df["WorkLoc"].value_counts())        #prints the value_counts which is the sum of the data that is being repeated, for instance "Office" was in 6806 positions

print("\nMost repeated value count: ", df["WorkLoc"].value_counts().max())          #prints the most repeated as a count/amount
print("\nMost repeated value: ",df["WorkLoc"].value_counts().idxmax())        #prints the most repeated word/value

m_value = df["WorkLoc"].value_counts().idxmax()         #saves the value of most repeated value as a variable

df["WorkLoc"] = df["WorkLoc"].fillna(m_value)           #fills the empty data in "WorkLoc" column with the most repeated value
print("\nEmpty places after filling data: ", df["WorkLoc"].isna().sum())                       #prints the empty places in "WorkLoc" column (should be 0)
