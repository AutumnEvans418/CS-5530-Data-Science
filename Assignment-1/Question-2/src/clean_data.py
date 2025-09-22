import pandas as pd
import numpy as np

df = pd.read_csv("Assignment-1\\Question-2\\raw_data\\StudentsPerformance.csv")

# remove rows with zero values in math score column (should be 1 row)
df = df[df['math score'] != 0]

# remove unnecessary columns: "race/ethnicity","parental level of education"
df = df.drop(labels=["race/ethnicity","parental level of education"], axis=1)

df.to_csv("Assignment-1\\Question-2\\clean_data\\StudentsPerformance_clean.csv", index=False)