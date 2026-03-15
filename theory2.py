# =============================================================================
#                         TWO MARKS QUESTION & ANSWERS
#                    Unit III, IV & V  |  Python (Spyder)
# =============================================================================


# =============================================================================
# UNIT III -- NumPy, Pandas and Matplotlib
# =============================================================================

# Q1. What is NumPy and why is it used in Python?
"""
NumPy (Numerical Python) is an open-source library used for numerical computing.
It provides support for multi-dimensional arrays, matrices, and a large collection
of mathematical functions to operate on them efficiently.
It is used because it is faster and more memory-efficient than Python lists.
"""

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("Q1 - NumPy array:", arr)


# Q2. Mention any two features of NumPy.
"""
Two features of NumPy:
1. N-dimensional array object (ndarray) for efficient storage and computation.
2. Broadcasting - allows operations on arrays of different shapes.
"""

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print("Q2 - Broadcasting (a + b):", a + b)


# Q3. What is an array in NumPy?
"""
An array in NumPy is an ndarray (n-dimensional array) object that stores
elements of the same data type in a contiguous block of memory.
It can be 1D, 2D, or multi-dimensional.
"""

arr_1d = np.array([10, 20, 30])          # 1D array
arr_2d = np.array([[1, 2], [3, 4]])      # 2D array
print("Q3 - 1D array:", arr_1d)
print("Q3 - 2D array:\n", arr_2d)


# Q4. What is Pandas used for in data analysis?
"""
Pandas is used for data manipulation and analysis. It provides data structures
like Series and DataFrame to handle structured (tabular) data efficiently.
It helps in data cleaning, transformation, filtering, grouping, and merging.
"""

import pandas as pd
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print("Q4 - Pandas DataFrame:\n", df)


# Q5. Define a DataFrame in Pandas.
"""
A DataFrame is a 2-dimensional labelled data structure in Pandas, similar to
a spreadsheet or SQL table. It has rows and columns where each column can be
of a different data type.
"""

df = pd.DataFrame({'Subject': ['Maths', 'Science'], 'Marks': [90, 85]})
print("Q5 - DataFrame:\n", df)


# Q6. What is the purpose of the describe() function in Pandas?
"""
The describe() function generates descriptive statistics of a DataFrame or Series.
It shows count, mean, std deviation, min, max, and quartile values (25%, 50%, 75%).
It is used to get a quick statistical summary of numerical columns.
"""

df = pd.DataFrame({'Marks': [55, 70, 85, 90, 60]})
print("Q6 - describe():\n", df.describe())


# Q7. What is the difference between loc and iloc in Pandas?
"""
loc  : Label-based indexing. Accesses rows/columns using their labels/names.
iloc : Integer-based indexing. Accesses rows/columns using integer positions.

Example:
  df.loc[0]       -> Accesses row with label (index) 0
  df.iloc[0]      -> Accesses the first row by position (0)
"""

df = pd.DataFrame({'A': [10, 20, 30]}, index=['x', 'y', 'z'])
print("Q7 - loc['y']:", df.loc['y'].values)
print("Q7 - iloc[1]:", df.iloc[1].values)


# Q8. What is the use of iloc in Pandas?
"""
iloc is used for integer-location based indexing.
It selects data by row and column positions (starting from 0),
regardless of the index labels.
"""

df = pd.DataFrame({'Name': ['Tom', 'Jerry', 'Spike'], 'Score': [80, 75, 90]})
print("Q8 - iloc[1]:\n", df.iloc[1])        # second row
print("Q8 - iloc[0:2]:\n", df.iloc[0:2])    # first two rows


# Q9. What is the purpose of Matplotlib?
"""
Matplotlib is a 2D plotting library in Python used for creating static,
animated, and interactive visualizations. It helps in creating line plots,
bar charts, histograms, scatter plots, pie charts, and more.
"""

import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Q9 - Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# Q10. What is the purpose of plt.show() in Matplotlib?
"""
plt.show() displays all open figures. It renders the plot and presents it
in a window. Without calling plt.show(), the plot may not appear (especially
in script mode or Spyder's inline backend).
"""

plt.plot([1, 4, 9], label="Squares")
plt.legend()
plt.title("Q10 - plt.show() example")
plt.show()    # Renders and displays the chart


# Q11. Write the syntax to create a line plot using Matplotlib.
"""
Syntax:
    plt.plot(x, y)
    plt.title("Title")
    plt.xlabel("X label")
    plt.ylabel("Y label")
    plt.show()
"""

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, color='blue', marker='o', linestyle='-')
plt.title("Q11 - Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# Q12. Write the syntax to create a scatter plot using Matplotlib.
"""
Syntax:
    plt.scatter(x, y)
    plt.title("Title")
    plt.show()
"""

x = [1, 2, 3, 4, 5]
y = [5, 3, 8, 2, 7]
plt.scatter(x, y, color='red')
plt.title("Q12 - Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# Q13. When is a bar plot used?
"""
A bar plot is used to compare discrete categories or groups.
It displays rectangular bars whose heights represent the values of each category.
Commonly used for comparing sales, scores, frequencies across groups.
"""

categories = ['A', 'B', 'C', 'D']
values = [30, 70, 45, 90]
plt.bar(categories, values, color='green')
plt.title("Q13 - Bar Plot")
plt.show()


# Q14. What is a boxplot used for in data visualization?
"""
A boxplot (box-and-whisker plot) is used to display the distribution of data
based on five summary statistics:
  - Minimum, Q1 (25th), Median (50th), Q3 (75th), Maximum
It helps identify outliers and the spread/skewness of data.
"""

data = [10, 20, 25, 28, 30, 35, 100]   # 100 is an outlier
plt.boxplot(data)
plt.title("Q14 - Boxplot")
plt.show()


# Q15. What information does a histogram display?
"""
A histogram displays the frequency (count) of data within continuous intervals
(bins). It shows the distribution shape of numerical data, helping to identify
patterns like normal distribution, skewness, and outliers.
"""

data = [5, 10, 10, 15, 20, 20, 20, 25, 30, 35]
plt.hist(data, bins=5, color='orange', edgecolor='black')
plt.title("Q15 - Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


# Q16. What is a scatter plot used for?
"""
A scatter plot is used to show the relationship (correlation) between two
numerical variables. Each point represents one observation.
It helps detect trends, clusters, and outliers in data.
"""

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
plt.scatter(x, y, color='purple')
plt.title("Q16 - Scatter Plot (Correlation)")
plt.show()


# Q17. What is a line plot commonly used to represent?
"""
A line plot is commonly used to represent trends over time (time-series data).
For example: stock prices, temperature changes, sales growth over months.
Points are connected with lines to show continuity of change.
"""

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [100, 150, 120, 170, 200]
plt.plot(months, sales, marker='o')
plt.title("Q17 - Line Plot (Monthly Sales Trend)")
plt.show()


# Q18. What is meant by formatting charts in Matplotlib?
"""
Formatting charts means customizing the visual appearance of plots.
This includes:
  - Adding title, labels, legends
  - Changing colors, markers, and line styles
  - Setting grid lines, tick marks, and figure size
"""

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
plt.figure(figsize=(6, 4))
plt.plot(x, y, color='teal', linestyle='--', marker='s', label='y = x²')
plt.title("Q18 - Formatted Chart", fontsize=14)
plt.xlabel("X", fontsize=12)
plt.ylabel("Y", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()


# Q19. What types of plots can be created using Matplotlib? Name any two.
"""
Matplotlib can create many types of plots. Two common ones:
  1. Line Plot   - plt.plot()
  2. Bar Chart   - plt.bar()

Others include: scatter, histogram, pie, boxplot, heatmap, etc.
"""

# Line plot
plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Line Plot")

# Bar chart
plt.subplot(1, 2, 2)
plt.bar(['A', 'B', 'C'], [5, 8, 3])
plt.title("Bar Chart")

plt.suptitle("Q19 - Two Types of Plots")
plt.tight_layout()
plt.show()


# Q20. How does Pandas help in handling structured datasets?
"""
Pandas helps in handling structured datasets by providing:
  - DataFrame: a 2D table structure for easy data manipulation
  - Reading/writing CSV, Excel, SQL files with read_csv(), to_csv(), etc.
  - Data filtering, grouping, sorting, and merging operations
  - Handling missing values with fillna(), dropna()
  - Statistical summaries with describe(), mean(), sum(), etc.
"""

df = pd.read_csv.__doc__[:50]   # Just referencing - shows Pandas has CSV support
df2 = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Carol'],
    'Marks': [85, 92, 78],
    'Grade': ['B', 'A', 'C']
})
print("Q20 - Structured Dataset:\n", df2)
print("Q20 - Mean Marks:", df2['Marks'].mean())


# =============================================================================
# UNIT IV -- Descriptive Statistics
# =============================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


# Q1. What are the different types of data in statistics?
"""
Types of data in statistics:
  1. Qualitative (Categorical): Nominal, Ordinal
  2. Quantitative (Numerical): Discrete, Continuous
     - Interval scale
     - Ratio scale
"""

data_types = ['Nominal', 'Ordinal', 'Interval', 'Ratio']
print("Q1 - Types of data:", data_types)


# Q2. What is nominal data?
"""
Nominal data is categorical data with no natural order or ranking.
Categories are just labels/names.
Example: Gender (Male, Female), Colors (Red, Blue, Green), Blood Group (A, B, O, AB)
"""

nominal_data = ['Male', 'Female', 'Female', 'Male', 'Male']
print("Q2 - Nominal data:", nominal_data)


# Q3. What is ordinal data?
"""
Ordinal data is categorical data with a meaningful order/ranking,
but the differences between categories are not measurable.
Example: Ratings (Poor < Average < Good < Excellent), Education Level
"""

ordinal_data = ['Poor', 'Average', 'Good', 'Excellent']
print("Q3 - Ordinal data (ordered):", ordinal_data)


# Q4. What is the difference between ratio scale and interval scale?
"""
Interval Scale:
  - Has equal intervals between values
  - No true zero point
  - Example: Temperature in Celsius, IQ Score
  - Cannot say "twice as much"

Ratio Scale:
  - Has equal intervals AND a true zero point
  - Example: Height, Weight, Age, Income
  - Can say "twice as much" (e.g., 20kg is twice 10kg)
"""

print("Q4 - Interval: Temperature (0°C doesn't mean no temperature)")
print("Q4 - Ratio: Weight (0 kg means no weight)")


# Q5. Define mean in statistics.
"""
Mean is the arithmetic average of a dataset.
Formula: Mean = Sum of all values / Number of values
It represents the central value of data.
"""

data = [10, 20, 30, 40, 50]
mean_val = np.mean(data)
print("Q5 - Data:", data)
print("Q5 - Mean:", mean_val)


# Q6. What is median?
"""
Median is the middle value of a dataset when arranged in ascending order.
If n is even: Median = average of two middle values
If n is odd:  Median = middle value
It is not affected by extreme values (outliers).
"""

data_odd = [3, 7, 1, 9, 5]
data_even = [3, 7, 1, 9]
print("Q6 - Odd data:", sorted(data_odd), "Median:", np.median(data_odd))
print("Q6 - Even data:", sorted(data_even), "Median:", np.median(data_even))


# Q7. What is mode?
"""
Mode is the value that appears most frequently in a dataset.
A dataset can have one mode (unimodal), two modes (bimodal), or more.
"""

data = [1, 2, 2, 3, 4, 4, 4, 5]
mode_val = stats.mode(data, keepdims=True)
print("Q7 - Data:", data)
print("Q7 - Mode:", mode_val.mode[0])


# Q8. Define mean, median, and mode collectively.
"""
Mean, Median, and Mode are called MEASURES OF CENTRAL TENDENCY.
They describe the center or typical value of a dataset.
  - Mean   : Arithmetic average
  - Median : Middle value when sorted
  - Mode   : Most frequent value
"""

data = [5, 10, 10, 15, 20, 25]
print("Q8 - Mean:", np.mean(data))
print("Q8 - Median:", np.median(data))
print("Q8 - Mode:", stats.mode(data, keepdims=True).mode[0])


# Q9. What is the purpose of a bar chart?
"""
A bar chart is used to compare values across different categories.
Each bar's height represents the value for that category.
It is useful for displaying discrete/categorical data.
"""

subjects = ['Maths', 'Science', 'English', 'History']
scores = [85, 90, 75, 80]
plt.bar(subjects, scores, color='steelblue')
plt.title("Q9 - Bar Chart (Student Scores)")
plt.ylabel("Scores")
plt.show()


# Q10. When is a pie chart used?
"""
A pie chart is used to show the proportion or percentage of each category
relative to the whole dataset. It is best when there are few categories
and you want to show part-to-whole relationships.
"""

labels = ['Maths', 'Science', 'English']
sizes = [40, 35, 25]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Q10 - Pie Chart (Subject Distribution)")
plt.show()


# Q11. What is a box plot used to represent?
"""
A box plot (box-and-whisker plot) represents the distribution of data using:
  - Minimum
  - Q1 (25th percentile)
  - Median (50th percentile)
  - Q3 (75th percentile)
  - Maximum
It also shows outliers as individual points beyond the whiskers.
"""

data = [10, 15, 20, 22, 25, 28, 30, 35, 80]  # 80 is an outlier
plt.boxplot(data, vert=True)
plt.title("Q11 - Box Plot")
plt.ylabel("Values")
plt.show()


# Q12. What is range in statistics?
"""
Range is the difference between the maximum and minimum values in a dataset.
Formula: Range = Maximum - Minimum
It gives a basic measure of spread/variability.
"""

data = [5, 15, 25, 35, 45]
data_range = max(data) - min(data)
print("Q12 - Data:", data)
print("Q12 - Range:", data_range)


# Q13. What is interquartile range (IQR)?
"""
IQR is the range of the middle 50% of the data.
Formula: IQR = Q3 - Q1
  - Q1 = 25th percentile
  - Q3 = 75th percentile
IQR is used to detect outliers and is resistant to extreme values.
"""

data = [5, 10, 15, 20, 25, 30, 35, 40]
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1
print("Q13 - Q1:", q1, "| Q3:", q3, "| IQR:", iqr)


# Q14. What is standard deviation?
"""
Standard deviation measures how much the values in a dataset deviate
from the mean on average.
  - Low SD  : Data points are close to the mean
  - High SD : Data points are spread out far from the mean
Formula: SD = sqrt(variance) = sqrt(mean of squared deviations)
"""

data = [10, 20, 30, 40, 50]
sd = np.std(data)
print("Q14 - Data:", data)
print("Q14 - Standard Deviation:", round(sd, 2))


# Q15. What is skewness?
"""
Skewness measures the asymmetry of the distribution of data.
  - Positive skew (right skew): Tail is on the right side; mean > median
  - Negative skew (left skew):  Tail is on the left side; mean < median
  - Zero skew: Symmetric (normal distribution)
"""

data = [1, 2, 2, 3, 3, 3, 4, 5, 10]  # Right-skewed due to outlier 10
skewness = pd.Series(data).skew()
print("Q15 - Data:", data)
print("Q15 - Skewness:", round(skewness, 4), "(positive = right skewed)")


# Q16. What is kurtosis?
"""
Kurtosis measures the sharpness (peakedness) of the distribution.
  - Leptokurtic (kurtosis > 3): Sharp peak, heavy tails
  - Platykurtic  (kurtosis < 3): Flat peak, light tails
  - Mesokurtic   (kurtosis = 3): Normal distribution
"""

data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
kurtosis_val = pd.Series(data).kurtosis()  # Excess kurtosis (relative to normal)
print("Q16 - Kurtosis (excess):", round(kurtosis_val, 4))


# Q17. What does a histogram represent?
"""
A histogram represents the frequency distribution of continuous data.
The x-axis shows intervals (bins) and the y-axis shows frequency/count.
It helps identify the shape of the data distribution (normal, skewed, etc.)
"""

data = np.random.normal(50, 10, 200)
plt.hist(data, bins=15, color='coral', edgecolor='black')
plt.title("Q17 - Histogram (Normal Distribution)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


# Q18. What is meant by measures of variability?
"""
Measures of variability (spread/dispersion) describe how spread out the
data values are from the center.
Common measures:
  - Range
  - Interquartile Range (IQR)
  - Variance
  - Standard Deviation
"""

data = [10, 20, 30, 40, 50]
print("Q18 - Range:", max(data) - min(data))
print("Q18 - Variance:", round(np.var(data), 2))
print("Q18 - Std Dev:", round(np.std(data), 2))


# Q19. Why are measures of central tendency important?
"""
Measures of central tendency are important because:
  1. They summarize a large dataset into a single representative value.
  2. Help compare different datasets.
  3. Assist in decision making and further statistical analysis.
  4. Provide a baseline for understanding data distribution.
Example: Average marks help evaluate overall class performance.
"""

marks = [55, 60, 70, 80, 90, 95]
print("Q19 - Class Marks:", marks)
print("Q19 - Mean (Central Tendency):", np.mean(marks))


# Q20. What does skewness indicate about a dataset?
"""
Skewness indicates the direction and degree of asymmetry in a dataset:
  - Positive skew: Most data on the left; a few high values pull the tail right
    (mean > median > mode)
  - Negative skew: Most data on the right; a few low values pull the tail left
    (mean < median < mode)
  - Zero skew: Perfectly symmetric data (mean = median = mode)
"""

right_skewed = [1, 2, 2, 3, 3, 3, 10, 15, 20]
left_skewed = [1, 5, 10, 15, 17, 17, 17, 18, 19]
print("Q20 - Right-skewed skewness:", round(pd.Series(right_skewed).skew(), 3))
print("Q20 - Left-skewed skewness:", round(pd.Series(left_skewed).skew(), 3))


# =============================================================================
# UNIT V -- Statistical Inference and Hypothesis Testing
# =============================================================================

import numpy as np
import pandas as pd
from scipy import stats


# Q1. What is a population in statistics?
"""
A population is the complete set of all individuals, objects, or measurements
that share a common characteristic being studied.
Example: All students in a university, all products manufactured in a factory.
"""

# Simulating a population
population = np.random.normal(loc=70, scale=10, size=10000)
print("Q1 - Population size:", len(population))
print("Q1 - Population mean:", round(np.mean(population), 2))


# Q2. What is a sample in statistics?
"""
A sample is a subset of the population selected for study.
It is used to draw conclusions (inferences) about the population
without studying every member.
Example: 100 students selected from a university of 10,000 students.
"""

sample = np.random.choice(population, size=100, replace=False)
print("Q2 - Sample size:", len(sample))
print("Q2 - Sample mean:", round(np.mean(sample), 2))


# Q3. Differentiate between population and sample.
"""
Population:
  - Complete set of all elements
  - Parameters: μ (mean), σ (std dev)
  - Usually large or infinite
  - Studying it is costly/impractical

Sample:
  - A subset of the population
  - Statistics: x̄ (sample mean), s (sample std dev)
  - Smaller and manageable
  - Used to estimate population parameters
"""

print("Q3 - Population mean (μ):", round(np.mean(population), 2))
print("Q3 - Sample mean (x̄):", round(np.mean(sample), 2))


# Q4. What is hypothesis testing?
"""
Hypothesis testing is a statistical procedure used to make decisions or
draw conclusions about a population parameter based on sample data.
Steps:
  1. State null and alternative hypotheses
  2. Choose significance level (α)
  3. Compute test statistic and p-value
  4. Make a decision: Reject or Fail to reject H₀
"""

print("Q4 - Hypothesis testing is used to validate assumptions about data.")


# Q5. What is a null hypothesis (H₀)?
"""
The null hypothesis (H₀) is the default assumption that there is
NO significant difference or effect.
It assumes the status quo / no change.
Example: H₀: The mean exam score = 70 (no difference from average)
"""

print("Q5 - Null Hypothesis (H₀): Mean score = 70 (no significant difference)")


# Q6. What is an alternative hypothesis (H₁)?
"""
The alternative hypothesis (H₁ or Hₐ) is the claim that contradicts H₀.
It represents what we want to prove or detect.
Example: H₁: The mean exam score ≠ 70 (there IS a significant difference)
Types:
  - Two-tailed: H₁: μ ≠ value
  - Left-tailed: H₁: μ < value
  - Right-tailed: H₁: μ > value
"""

print("Q6 - Alternative Hypothesis (H₁): Mean score ≠ 70")


# Q7. What is the level of significance in hypothesis testing?
"""
The level of significance (α) is the probability threshold used to decide
whether to reject the null hypothesis.
Common values: α = 0.05 (5%) or α = 0.01 (1%)
  - If p-value ≤ α → Reject H₀ (result is statistically significant)
  - If p-value > α → Fail to reject H₀
"""

alpha = 0.05
print("Q7 - Level of significance (α):", alpha)


# Q8. What is a Type I error?
"""
Type I error (False Positive) is rejecting a true null hypothesis.
It occurs when we conclude there is an effect when there is none.
The probability of Type I error = α (level of significance)
Example: Concluding a drug is effective when it actually is not.
"""

print("Q8 - Type I Error: Rejecting a true H₀ (False Positive)")
print("Q8 - Probability = α =", alpha)


# Q9. What is a Type II error?
"""
Type II error (False Negative) is failing to reject a false null hypothesis.
It occurs when we fail to detect an effect that actually exists.
The probability of Type II error = β
Example: Concluding a drug is NOT effective when it actually IS.
"""

print("Q9 - Type II Error: Failing to reject a false H₀ (False Negative)")
print("Q9 - Probability = β (beta)")


# Q10. What decision is made if p-value < level of significance?
"""
If p-value < α (level of significance):
  → REJECT the null hypothesis (H₀)
  → The result is statistically significant
  → There is sufficient evidence to support the alternative hypothesis (H₁)
"""

p_value = 0.03
alpha = 0.05
if p_value < alpha:
    print("Q10 - p-value:", p_value, "< α:", alpha, "→ Reject H₀")


# Q11. What decision is made if p-value > level of significance?
"""
If p-value > α (level of significance):
  → FAIL TO REJECT the null hypothesis (H₀)
  → The result is NOT statistically significant
  → Insufficient evidence to support the alternative hypothesis (H₁)
"""

p_value = 0.20
alpha = 0.05
if p_value > alpha:
    print("Q11 - p-value:", p_value, "> α:", alpha, "→ Fail to reject H₀")


# Q12. What is a one-sample t-test used for?
"""
A one-sample t-test is used to determine if the mean of a sample is
significantly different from a known or hypothesized population mean.
H₀: Sample mean = Population mean (μ₀)
H₁: Sample mean ≠ μ₀
"""

sample_data = [72, 68, 75, 70, 80, 65, 78, 71, 69, 74]
pop_mean = 70
t_stat, p_val = stats.ttest_1samp(sample_data, pop_mean)
print("Q12 - One-Sample t-test: t =", round(t_stat, 4), "| p-value =", round(p_val, 4))
if p_val < 0.05:
    print("Q12 → Reject H₀: Sample mean differs from population mean")
else:
    print("Q12 → Fail to reject H₀: No significant difference")


# Q13. When is a paired sample t-test used?
"""
A paired sample t-test is used when comparing two related/dependent groups.
Each observation in one group is matched to an observation in the other.
Example:
  - Comparing a student's marks before and after training
  - Measuring blood pressure before and after medication (same patients)
"""

before = [60, 55, 70, 65, 58]
after = [70, 65, 75, 72, 68]
t_stat, p_val = stats.ttest_rel(before, after)
print("Q13 - Paired t-test: t =", round(t_stat, 4), "| p-value =", round(p_val, 4))
if p_val < 0.05:
    print("Q13 → Reject H₀: Significant difference before and after")
else:
    print("Q13 → Fail to reject H₀: No significant difference")


# Q14. What is an independent samples t-test?
"""
An independent samples t-test (two-sample t-test) compares the means of
two INDEPENDENT (unrelated) groups to see if they differ significantly.
Example:
  - Comparing exam scores of Group A vs Group B (different students)
  - Comparing heights of males vs females
"""

group_a = [75, 80, 85, 70, 78]
group_b = [65, 70, 72, 68, 74]
t_stat, p_val = stats.ttest_ind(group_a, group_b)
print("Q14 - Independent t-test: t =", round(t_stat, 4), "| p-value =", round(p_val, 4))
if p_val < 0.05:
    print("Q14 → Reject H₀: Groups differ significantly")
else:
    print("Q14 → Fail to reject H₀: No significant difference between groups")


# Q15. What is the purpose of one-way ANOVA?
"""
One-way ANOVA (Analysis of Variance) tests whether the means of three or
more independent groups are significantly different.
H₀: All group means are equal (μ₁ = μ₂ = μ₃)
H₁: At least one group mean is different
It is used when t-test is not enough (more than 2 groups).
"""

group1 = [80, 85, 82, 88, 79]
group2 = [70, 75, 72, 68, 74]
group3 = [90, 92, 88, 95, 91]
f_stat, p_val = stats.f_oneway(group1, group2, group3)
print("Q15 - One-Way ANOVA: F =", round(f_stat, 4), "| p-value =", round(p_val, 4))
if p_val < 0.05:
    print("Q15 → Reject H₀: At least one group mean is significantly different")
else:
    print("Q15 → Fail to reject H₀: All group means are equal")


# Q16. What is the Chi-Square test used for?
"""
The Chi-Square (χ²) test is used for categorical data to test:
  1. Goodness of Fit: Does the observed data fit an expected distribution?
  2. Test of Independence: Are two categorical variables independent?
Example: Is there a relationship between gender and subject preference?
"""

# Example: Goodness of fit
observed = [30, 40, 30]          # Observed frequencies
expected = [33.33, 33.33, 33.33] # Expected (equal distribution)
chi2_stat, p_val = stats.chisquare(f_obs=observed, f_exp=expected)
print("Q16 - Chi-Square test: χ² =", round(chi2_stat, 4), "| p-value =", round(p_val, 4))
if p_val < 0.05:
    print("Q16 → Reject H₀: Observed differs from expected distribution")
else:
    print("Q16 → Fail to reject H₀: Data fits expected distribution")


# Q17. What is a p-value in hypothesis testing?
"""
The p-value is the probability of obtaining a test result at least as extreme
as the observed result, assuming H₀ is true.
  - Small p-value (< α): Strong evidence against H₀ → Reject H₀
  - Large p-value (> α): Weak evidence against H₀ → Fail to reject H₀
A p-value of 0.03 means: if H₀ were true, there is only a 3% chance of
getting this result by random chance.
"""

print("Q17 - p-value < 0.05 → Statistically significant → Reject H₀")
print("Q17 - p-value > 0.05 → Not significant → Fail to reject H₀")


# Q18. What is statistical inference?
"""
Statistical inference is the process of drawing conclusions about a
population based on information from a sample.
Two main types:
  1. Estimation: Estimating population parameters using sample statistics
     (point estimate or confidence interval)
  2. Hypothesis Testing: Making decisions about population parameters
     using test statistics and p-values
"""

sample = [72, 75, 68, 80, 71, 69, 77]
print("Q18 - Sample mean (point estimate for population):", round(np.mean(sample), 2))
ci = stats.t.interval(0.95, len(sample)-1, loc=np.mean(sample),
                      scale=stats.sem(sample))
print("Q18 - 95% Confidence Interval:", (round(ci[0], 2), round(ci[1], 2)))


# Q19. What is the importance of sampling in statistics?
"""
Sampling is important in statistics because:
  1. Studying an entire population is often impractical or impossible.
  2. Saves time, cost, and resources.
  3. A well-chosen sample provides accurate estimates of the population.
  4. Enables hypothesis testing and making generalizations.
  5. Reduces errors when done with proper sampling techniques.
"""

population = np.arange(1, 10001)       # Population: 1 to 10,000
sample = np.random.choice(population, size=200, replace=False)
print("Q19 - Population Mean:", np.mean(population))
print("Q19 - Sample Mean (n=200):", round(np.mean(sample), 2))


# Q20. Why are hypothesis tests used in data analysis?
"""
Hypothesis tests are used in data analysis because:
  1. They provide a formal framework for making data-driven decisions.
  2. Help determine if observed differences are real or due to chance.
  3. Used to validate assumptions before applying models.
  4. Quantify uncertainty using p-values and confidence levels.
  5. Widely used in research, medicine, business, and machine learning.
Example: Testing if a new teaching method improves student performance.
"""

control = [65, 70, 68, 72, 66]      # Group without new method
treatment = [75, 80, 78, 82, 76]    # Group with new method
t_stat, p_val = stats.ttest_ind(treatment, control)
print("Q20 - Teaching method test: t =", round(t_stat, 4), "| p-value =", round(p_val, 4))
if p_val < 0.05:
    print("Q20 → Reject H₀: New method significantly improves performance")
else:
    print("Q20 → Fail to reject H₀: No significant improvement")


# =============================================================================
# END OF FILE
# =============================================================================
