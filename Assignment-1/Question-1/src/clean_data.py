import pandas as pd
import numpy as np
df = pd.read_csv("Assignment-1\\Question-1\\raw_data\\frailty_raw.csv")

print(df)

# standard units
df['Height_m'] = df['Height_in'] * 0.0254
df['Weight_kg'] = df['Weight_lbs'] * 0.45359237
df = df.drop(['Height_in', 'Weight_lbs'], axis=1)

# feature engineering

df['BMI'] = (df['Weight_kg'] / (df['Height_m'] ** 2)).round(2)

bins = [0, 30, 45, 60, np.inf]
names = ['<30', '30-45', '46-60', '>65']
df['AgeRange'] = pd.cut(df['Age_yrs'], bins, labels=names)

# encoding
df = pd.get_dummies(data=df, columns=['AgeRange', 'Frailty'], drop_first=True)
df['Frailty_Y'] = df['Frailty_Y'].astype(int)

print(df)

df.to_csv("Assignment-1\\Question-1\\clean_data\\frailty_clean.csv", index=False)