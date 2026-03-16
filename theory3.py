# =============================================================================
#                         TWO MARKS QUESTION & ANSWERS
#                         Unit III & Unit IV  |  Python (Spyder)
# =============================================================================


# =============================================================================
# UNIT III -- NumPy, Pandas and Matplotlib
# =============================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Q1. What is NumPy and why is it used in Python?
"""
NumPy (Numerical Python) is an open-source library used for numerical computing.
It provides support for multi-dimensional arrays, matrices, and a large collection
of mathematical functions to operate on them efficiently.
It is used because it is faster and more memory-efficient than Python lists.
"""

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

arr_1d = np.array([10, 20, 30])
arr_2d = np.array([[1, 2], [3, 4]])
print("Q3 - 1D array:", arr_1d)
print("Q3 - 2D array:\n", arr_2d)


# Q4. What is Pandas used for in data analysis?
"""
Pandas is used for data manipulation and analysis. It provides data structures
like Series and DataFrame to handle structured (tabular) data efficiently.
It helps in data cleaning, transformation, filtering, grouping, and merging.
"""

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
  df.loc['y']  -> Accesses row with label 'y'
  df.iloc[1]   -> Accesses the second row by position
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
print("Q8 - iloc[1]:\n", df.iloc[1])
print("Q8 - iloc[0:2]:\n", df.iloc[0:2])


# Q9. What is the purpose of Matplotlib?
"""
Matplotlib is a 2D plotting library in Python used for creating static,
animated, and interactive visualizations. It helps in creating line plots,
bar charts, histograms, scatter plots, pie charts, and more.
"""

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
plt.show()


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

data = [10, 20, 25, 28, 30, 35, 100]
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
  1. Line Plot  - plt.plot()
  2. Bar Chart  - plt.bar()

Others include: scatter, histogram, pie, boxplot, heatmap, etc.
"""

plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Line Plot")

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
  - Reading/writing CSV, Excel files with read_csv(), to_csv(), etc.
  - Data filtering, grouping, sorting, and merging operations
  - Handling missing values with fillna(), dropna()
  - Statistical summaries with describe(), mean(), sum(), etc.
"""

df = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Carol'],
    'Marks':   [85, 92, 78],
    'Grade':   ['B', 'A', 'C']
})
print("Q20 - Structured Dataset:\n", df)
print("Q20 - Mean Marks:", df['Marks'].mean())


# =============================================================================
# UNIT IV -- Descriptive Statistics
# =============================================================================

from scipy import stats


# Q1. What are the different types of data in statistics?
"""
Types of data in statistics:
  1. Qualitative (Categorical) : Nominal, Ordinal
  2. Quantitative (Numerical)  : Discrete, Continuous
       - Interval scale
       - Ratio scale
"""

data_types = ['Nominal', 'Ordinal', 'Interval', 'Ratio']
print("Q1 - Types of data:", data_types)


# Q2. What is nominal data?
"""
Nominal data is categorical data with no natural order or ranking.
Categories are just labels/names.
Example: Gender (Male, Female), Blood Group (A, B, O, AB), Colors
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
  - Can say "twice as much" (e.g., 20 kg is twice 10 kg)
"""

print("Q4 - Interval: Temperature (0°C doesn't mean no temperature)")
print("Q4 - Ratio   : Weight (0 kg means no weight at all)")


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
If n is odd  : Median = middle value
If n is even : Median = average of the two middle values
It is not affected by extreme values (outliers).
"""

data_odd  = [3, 7, 1, 9, 5]
data_even = [3, 7, 1, 9]
print("Q6 - Odd data :", sorted(data_odd),  "| Median:", np.median(data_odd))
print("Q6 - Even data:", sorted(data_even), "| Median:", np.median(data_even))


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
  - Mode   : Most frequently occurring value
"""

data = [5, 10, 10, 15, 20, 25]
print("Q8 - Mean  :", np.mean(data))
print("Q8 - Median:", np.median(data))
print("Q8 - Mode  :", stats.mode(data, keepdims=True).mode[0])


# Q9. What is the purpose of a bar chart?
"""
A bar chart is used to compare values across different categories.
Each bar's height represents the value for that category.
It is useful for displaying discrete/categorical data.
"""

subjects = ['Maths', 'Science', 'English', 'History']
scores   = [85, 90, 75, 80]
plt.bar(subjects, scores, color='steelblue')
plt.title("Q9 - Bar Chart (Student Scores)")
plt.ylabel("Scores")
plt.show()


# Q10. When is a pie chart used?
# (Answer not required)

# Q11. What is a box plot used to represent?
# (Answer not required)

# Q12. What is range in statistics?
# (Answer not required)

# Q13. What is interquartile range (IQR)?
# (Answer not required)

# Q14. What is standard deviation?
# (Answer not required)

# Q15. What is skewness?
# (Answer not required)

# Q16. What is kurtosis?
# (Answer not required)

# Q17. What does a histogram represent?
# (Answer not required)

# Q18. What is meant by measures of variability?
# (Answer not required)

# Q19. Why are measures of central tendency important?
# (Answer not required)

# Q20. What does skewness indicate about a dataset?
# (Answer not required)


# =============================================================================
# END OF FILE
# =============================================================================
