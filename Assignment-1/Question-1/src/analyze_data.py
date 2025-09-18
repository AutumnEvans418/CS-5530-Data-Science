import pandas as pd
import numpy as np

df = pd.read_csv("Assignment-1\\Question-1\\clean_data\\frailty_clean.csv")

print(df)

summary = df.describe().to_markdown()

findings = f"""
# Findings from Data Analysis

## Summary Statistics
{summary}

## Correlations
{df[['Grip_strength_kg','Frailty_Y']].corr().to_markdown()}
"""

with open("Assignment-1\\Question-1\\reports\\findings.md", "w") as f:
    f.write(findings)