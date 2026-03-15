import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Q1 - Import and display first five rows
df = pd.read_csv(r'C:\Users\HP\Downloads\winequality.csv')

print("First five rows of the dataset:")
print(df.head())

# Q2 - Data types and Mean, Median, Mode
print("\nDataset Data Types:")
print(df.dtypes)

mean_alcohol = df['alcohol'].mean()
median_alcohol = df['alcohol'].median()
mode_alcohol = df['alcohol'].mode()[0]

print("Mean Alcohol:", mean_alcohol)
print("Median Alcohol:", median_alcohol)
print("Mode Alcohol:", mode_alcohol)

# Q3 - Measures of Variability
print("\nMeasures of Variability for Alcohol:")

range_alcohol = df['alcohol'].max() - df['alcohol'].min()
iqr_alcohol = df['alcohol'].quantile(0.75) - df['alcohol'].quantile(0.25)
std_alcohol = df['alcohol'].std()
var_alcohol = df['alcohol'].var()

print("Range:", range_alcohol)
print("Inter Quartile Range (IQR):", iqr_alcohol)
print("Standard Deviation:", std_alcohol)
print("Variance:", var_alcohol)

# Q4 - Histogram
print("\nHistogram of Alcohol Distribution")

plt.figure()
plt.hist(df['alcohol'], bins=20)
plt.title("Distribution of Alcohol Content")
plt.xlabel("Alcohol")
plt.ylabel("Frequency")
plt.grid(False)
plt.show()

# Q5 - Bar Plot: Average Alcohol by Wine Quality
print("\nBar Plot: Average Alcohol by Wine Quality")

avg_alcohol = df.groupby('quality')['alcohol'].mean()

plt.figure()
avg_alcohol.plot(kind='bar')
plt.title("Average Alcohol Content by Wine Quality")
plt.xlabel("Wine Quality")
plt.ylabel("Average Alcohol")
plt.show()

# Q6 - Boxplot: Volatile Acidity across Wine Quality
print("\nBoxplot: Volatile Acidity across Wine Quality")

plt.figure()
sns.boxplot(x='quality', y='volatile acidity', data=df)
plt.title("Volatile Acidity Distribution by Wine Quality")
plt.show()

# Q7 - Scatter Plot: Alcohol vs Wine Quality
print("\nScatter Plot: Alcohol vs Wine Quality")

plt.figure()
plt.scatter(df['alcohol'], df['quality'])
plt.title("Alcohol vs Wine Quality")
plt.xlabel("Alcohol")
plt.ylabel("Quality")
plt.show()

# Q8 - Line Plot: Average Sulphates by Wine Quality
print("\nLine Plot: Average Sulphates by Wine Quality")

avg_sulphates = df.groupby('quality')['sulphates'].mean()

plt.figure()
plt.plot(avg_sulphates.index, avg_sulphates.values, marker='o')
plt.title("Average Sulphates by Wine Quality")
plt.xlabel("Wine Quality")
plt.ylabel("Average Sulphates")
plt.grid(True)
plt.show()

# Q9 - One-Sample t-test
print("\nOne-Sample t-test for Alcohol")

t_stat, p_value = stats.ttest_1samp(df['alcohol'], 10)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Result: Mean alcohol is significantly different from 10%")
else:
    print("Result: Mean alcohol is NOT significantly different from 10%")

# Q10 - Independent Samples t-test
print("\nIndependent Samples t-test")

group1 = df[df['quality'] >= 6]['alcohol']
group2 = df[df['quality'] < 6]['alcohol']

lev_stat, lev_p = stats.levene(group1, group2)
print("Levene Test p-value:", lev_p)

t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=(lev_p > 0.05))

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Result: Significant difference in alcohol between groups")
else:
    print("Result: No significant difference in alcohol between groups")

# Q11 - Paired Sample t-test
print("\nPaired Sample t-test")

df['alcohol_increased'] = df['alcohol'] * 1.10

t_stat, p_value = stats.ttest_rel(df['alcohol'], df['alcohol_increased'])

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Result: Significant difference after increasing alcohol")
else:
    print("Result: No significant difference")

# Q12 - One-Way ANOVA
print("\nOne-Way ANOVA")

groups = [df[df['quality'] == q]['alcohol'] for q in df['quality'].unique()]

f_stat, p_value = stats.f_oneway(*groups)

print("F-statistic:", f_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Result: Alcohol differs significantly across quality levels")
else:
    print("Result: No significant difference across quality levels")

# Q13 - Chi-Square Test
print("\nChi-Square Test")

df['alcohol_level'] = pd.cut(df['alcohol'],
                             bins=3,
                             labels=["Low", "Medium", "High"])

cont_table = pd.crosstab(df['alcohol_level'], df['quality'])

print("Contingency Table:")
print(cont_table)

chi2, p, dof, expected = stats.chi2_contingency(cont_table)

print("Chi-square value:", chi2)
print("P-value:", p)

if p < 0.05:
    print("Result: Significant association between alcohol level and wine quality")
else:
    print("Result: No significant association between alcohol level and wine quality")
