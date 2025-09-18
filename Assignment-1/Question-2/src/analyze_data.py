import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Assignment-1\\Question-2\\clean_data\\StudentsPerformance_clean.csv")

print(df)


# Side‑by‑side boxplots of math score and reading score grouped by gender.
bp = df.boxplot(column=['math score', 'reading score'], by=['gender'], figsize=(8,6))
plt.savefig("Assignment-1\\Question-2\\reports\\gender_boxplot.svg")

