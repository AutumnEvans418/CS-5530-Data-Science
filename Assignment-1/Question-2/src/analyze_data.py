import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Assignment-1\\Question-2\\clean_data\\StudentsPerformance_clean.csv")

print(df)


# Side‑by‑side boxplots of math score and reading score grouped by gender.
bp = df.boxplot(column=['math score', 'reading score'], by=['gender'], figsize=(8,6))
plt.yticks(ticks=range(0, 105, 5))

plt.savefig("Assignment-1\\Question-2\\reports\\gender_boxplot.svg")

# histogram of math score grouped by test preparation course.
hist = df.plot.hist(
    column='math score', 
    by='test preparation course', 
    figsize=(8,6),
    ylim = (0,0.045),
    bins=15,
    title="Math Score Distribution by Test Preparation Course",
    density=True)

for ax in hist:
    ax.set_xticks(range(0, 105, 5))

plt.savefig("Assignment-1\\Question-2\\reports\\test_prep_histogram.svg")

# lunch and average performance
# Grouped bar chart of mean overall_avg of all the scores (math, reading, writing) by lunch.
df['overall_avg'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
print(df)
lunch_avg = df.groupby('lunch')['overall_avg'].mean().reset_index()
ax = lunch_avg.plot.bar(
    x='lunch', 
    y='overall_avg', 
    legend=False, 
    figsize=(8,6),
    title="Average Performance by Lunch Type",
    xlabel="Lunch Type",
    ylabel="Average Performance")
# rotate x-axis labels for better readability
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)

plt.savefig("Assignment-1\\Question-2\\reports\\lunch_avg_bar_chart.svg")

# Subject correlations
# Correlation heatmap for math, reading, writing with annotated coefficients.
corr = df[['math score', 'reading score', 'writing score']].corr()

print(corr)

import seaborn as sns
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Correlation Heatmap of Scores")
# rotate x-axis labels for better readability
plt.xticks(rotation=0)
plt.savefig("Assignment-1\\Question-2\\reports\\score_correlation_heatmap.svg")

# Math vs reading with trend lines by test prep 
# Scatter plot with two straight best‑fit lines (one for each group: completed, none)

groups = [('completed', 'blue'), ('none', 'orange')]
fig, ax = plt.subplots()
for group in groups:
    x = np.array(df[df['test preparation course'] == group[0]]['reading score'])
    y = np.array(df[df['test preparation course'] == group[0]]['math score'])

    ax.scatter(x, y, c=group[1], label=f"{group[0]} ({len(x)})", alpha=0.5, s=10)

    z = np.polyfit(x,y,1)
    p = np.poly1d(z)
    plt.plot(x,p(x), color=group[1])

ax.set_title("Math vs Reading Scores by Test Preparation Course")
ax.legend()
ax.grid(True)
ax.set_xlabel("Reading Score")
ax.set_ylabel("Math Score")

plt.savefig("Assignment-1\\Question-2\\reports\\math_vs_reading_scatter.svg")
