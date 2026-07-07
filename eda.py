import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

df = pd.read_csv("mini_project/insurance.csv")
print(df)
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull())
print(df.isnull().sum())
print(df.duplicated())
print(df.duplicated().sum())
df_cleaned=df.copy();
print(df_cleaned.head(10))
print(df_cleaned.tail(10))
print(df_cleaned.isnull().sum())
print(df_cleaned.duplicated().sum())
print(df_cleaned.shape)
print(df_cleaned.drop_duplicates(inplace=True))
print(df_cleaned.shape)
print(df_cleaned.duplicated().sum())
print(df_cleaned.dtypes)
print(df_cleaned.info())
print(df_cleaned['sex'].value_counts())
df_cleaned['sex']=df_cleaned['sex'].map({"male":0,"female":1})
print(df_cleaned.head())
print(df_cleaned['smoker'].value_counts())
df_cleaned['smoker']=df_cleaned['smoker'].map({"no":0,"yes":1})
print(df_cleaned.head())
df_cleaned.rename(columns={'sex':'is_female',
     'smoker':'is_smoker'},inplace=True)
print(df_cleaned.head())     
print(df_cleaned['region'].value_counts())
df_cleaned=pd.get_dummies(df_cleaned,columns=['region'],drop_first=True)
print(df_cleaned.head())
df_cleaned=df_cleaned.astype(int)
print(df_cleaned.head())
# Features engineering and Extraction
sns.histplot(df['bmi'])
plt.show()
df_cleaned['bmi_category'] = pd.cut(df_cleaned['bmi'],bins=[0,18.5,25,30,100,float('inf')],labels=['underweight','healthy','overweight','obese'])
print(df_cleaned.head())
df_cleaned

