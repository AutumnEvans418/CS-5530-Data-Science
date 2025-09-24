
# Results from Data Analysis on Students Performance

## 1. Gender Boxplot (math vs reading score)
Question: Are there gender differences in math vs reading?
![plot](gender_boxplot.svg)

Based on the boxplots above, we observe that on average males perform better on math scores while females perform better on reading scores. We also observe that females have a much larger spread of math scores than males, while males have a much larger spread of reading scores than females. Females also displayed the largest change between math and reading scores by about 8 points, while the difference between males scores was about 3 points.

## 2. Test prep impact on math
Question: Do students who completed test prep score higher in math?
![plot](test_prep_histogram.svg)

Students who completed test prep, based on the histograms above, performed better on average on Math than students who did not complete test prep by about 5 points. Scores for those who completed test prep also have less variance, with many more attaining higher scores and much fewer scores below 60.

## 3. Lunch type and average performance
Question: Does lunch type (standard vs free/reduced) relate to outcomes?
![plot](lunch_avg_bar_chart.svg)

Based on the bar chart, we observe that students with a standard lunch perform better by about 8% on average. Based on the domain, we know that while there seems to be a correlation, there probably is a third variable that is not displayed. For example, students who have free/reduced lunches typically come from families with lower economic status and overall may have less resources available that could impact their average performance.

## 4. Subject correlations
Question: How strongly do the three subjects move together?
![plot](score_correlation_heatmap.svg)

The correlation matrix heatmap shows that all scores are positively correlated with each other, meaning that those who with high/low scores in one subject was likely to have similar scores in other subjects. Writing scores and reading scores are highly linearly correlated, while math scores are less correlated to reading/writing scores.

## 5. Math vs reading with trend lines by test prep
Question: How strongly are math and reading scores associated, and do students who completed the test‑preparation course have a _different slope_ in the math–reading relationship than those who did not?

![plot](math_vs_reading_scatter.svg)

