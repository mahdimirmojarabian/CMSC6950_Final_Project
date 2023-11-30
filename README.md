# Air Quality Data Analysis (CMSC6950 Final Project)


## Introduction

In this project, we used an air quality dataset from https://archive.ics.uci.edu/dataset/360/air+quality. These data are the output responses of a gas multisensor device deployed on a field in an Italian city to measure the air quality over time. The dataset contains `9357` rows of hourly averaged responses from an array of 5 metal oxide chemical sensors embedded in an air quality chemical multisensor device. Data was recorded for a period of one year (Early March 2004 – Early April 2005). Also, a co-located reference certified analyzer provided Ground Truth hourly averaged concentrations for CO, Non-Methanic Hydrocarbons, Benzene, Total Nitrogen Oxides (NOx), and Nitrogen Dioxide (NO2). Missing values are labeled with "-200". All columns of the data are shown in Table 1.


<caption>Table 1: Attributes of Dataset</caption>

| Column         | Description                                              |
|----------------|----------------------------------------------------------|
| Date           | Date (DD/MM/YYYY)                                        |
| Time           | Time (HH.MM.SS)                                          |
| CO(GT)         | True hourly averaged CO concentration [mg/m3] (reference analyzer)   |
| PT08.S1(CO)    | PT08.S1 (tin oxide) hourly averaged sensor response (nominally CO targeted)   |
| NMHC(GT)       | Non Metanic HydroCarbons concentration [μg/m3] (reference analyzer) |
| C6H6(GT)       | True hourly averaged Benzene concentration [μg/m3] (reference analyzer)  |
| PT08.S2(NMHC)  | PT08.S2 (titania) hourly averaged sensor response (nominally NMHC targeted) |
| NOx (GT)       | True hourly averaged NOx concentration [ppb] (reference analyzer) |
| PT08.S3(NOx)   | PT08.S3 (tungsten oxide) hourly averaged sensor response    |
| NO2(GT)        | True hourly averaged NO2 concentration [μg/m3] (reference analyzer)  |
| PT08.S4(NO2)   | PT08.S4 (tungsten oxide) hourly averaged sensor response    |
| PT08.S5(O3)    | PT08.S5 (indium oxide) hourly averaged sensor response (nominally O3 targeted)  |
| T              | Temperature [°C]                                         |
| RH             | Relative Humidity (%)                                    |
| AH             | Absolute Humidity                                        |


This project has 3 tasks:

1. `Data Visualization`: Plot the data in a series of clearly labelled plots
2. `Extreme Value Analysis`: Compute some meaningful statistics regarding extreme values in the data and present this data. Explore sensitivity of these results to the definition of "extreme values", again presenting data.
3. `Trend Analysis`: Identify and discuss trends in the data, using appropriate statistical or other tools.

## Prerequisites

For this project I used `Python 3.9.16`. To install the required libraries use the following command:

```python
pip install -r requirements.txt
```

This command will install the libraries listed in the `requirements.txt` file.

Please remember that you need to have Python and pip installed to use the requirements.txt file.


## Methodology

This project's main code is located in a Jupyter Notebook file named `code_project.ipynb`. I also put two of my functions that need unit tests in a .py file called `Functions_For_Test.py` and wrote their test contents in the `Test_Functions_For_Test.py` file. For my project, I have used (pandas, numpy, matplotlib, seaborn, and pytest) libraries in Python.


In the first stage, I constructed a Python panda dataframe from my `AirQuality.csv` file located in the `dataset` folder. I did some initial data cleaning. I dropped extra and all-NaN data (the last 2 columns). I also dropped extra fully empty rows (from index `9357` to `9471`). In the dataframe, missing data was tagged with `-200`. These values were replaced with NaN for easier handling. A function `NaN_Percentages()` was defined to calculate the percentage of NaN values in each column. This was used to decide which columns should be removed. The column "NMHC(GT)" had %90.23 missing values; so, I dropped this attribute because keeping that will not be that helpful for our analysis.

### Data Visualization Task
`Time Series Illustration`: The data was plotted in a series of clearly labeled plots using the matplotlib and pandas libraries in Python. The function `my_plot()` was defined to automatically plot each attribute time series. The `Date` and `Time` columns were extracted and converted to datetime objects, and then each attribute was plotted against the date. The x-axis was set to show only monthly ticks and a grid was added for better visualization.

`Filling in Missed Values Using Interpolation Techniques`: The dataset had many missing values. To handle these, an interpolation technique was used. A copy of the original dataframe was made, and the `interpolate()` function from pandas was used to fill in the missing values. The `nearest` method was used for interpolation, which uses the value of the nearest point to fill the missing values. After filling in the missing values, the function `plot_orig_modif_series()` was used to plot both the original and modified dataframes. This function plotted the original data in red and the modified data in blue, allowing for a clear comparison between the two. The plots were set to show only monthly ticks on the x-axis, and a grid was added for better visualization.

`Data Distribution Visualization`: To assess the distributions of the data, histograms and probability density plots were created for each attribute in the dataset. A function `plot_histograms_density()` was defined to automatically plot both the histogram and probability density function for each attribute on the same plot. The function takes as input the dataframe and the columns to plot. It creates a figure with subplots, one for each attribute. For each attribute, it creates a normalized histogram and a probability density plot on the same subplot. The plots are labeled, and a legend is added for clarity.

### Extreme Value Analysis Task
A function `my_boxplot()` was defined to create boxplots for each attribute in the dataset. The boxplots were used to visualize the distribution of the data and identify potential outliers. The whiskers of the boxplot were set to 1.5 times the Interquartile Range (IQR) by default.

A function `show_stats()` was defined to compute various descriptive statistics for each attribute, including count, mean, median, minimum, maximum, standard deviation, variance, and skewness.

The `Interquartile Range (IQR)` method was used to define what constitutes an “extreme value”. This method was preferred over the Standard Deviation method because it provides specific parameters (IQR, Q1, Q3) for each distribution that can show the behavior of each attribute value uniquely.

A function `remove_outliers_IQR()` was defined to automatically calculate the IQR parameters and the lower and higher limits for each attribute. This function was used to identify and handle outliers in the data. Outliers were defined as values that fall outside of the whiskers in the boxplot. The function also calculated the outlier ratio for each attribute, plotted the outlier ratios in a bar chart, and provided information about the edited dataframe. The outliers were either replaced with the lower or higher limit values or removed from the dataset, depending on the specified mode.

`Extreme Value Analysis (scale=1.5)`: Boxplots were created for each attribute in the dataset using a whisker scale of 1.5. The boxplots were used to visualize the distribution of the data and identify potential outliers. A function remove_outliers_IQR() was defined to automatically calculate the IQR parameters and the lower and higher limits for each attribute. This function was used to identify and handle outliers in the data. Outliers were defined as values that fall outside of the whiskers in the boxplot. The function also calculated the outlier ratio for each attribute, plotted the outlier ratios, and provided information about the edited dataframe. The outliers were replaced with lower or higher limit values.

`Statistical Analysis of Extreme Values (scale=1.5)`: Various descriptive statistics were computed for the outliers, including count, mean, median, minimum, maximum, standard deviation, variance, and skewness. The frequency, range, associated times or conditions, variability, and outlier ratios of the extreme values were analyzed. Also, a bar chart was plotted to compare the outlier ratios for all attributes.

`Comparison of Original and Modified Data (scale=1.5)`: The original and modified dataframes were compared to observe the outliers. The original data was plotted in red, and the modified data in blue, allowing for a clear comparison between the two.

`Extreme Value Analysis (scale=2)`: The same analysis was repeated with a whisker scale of 2. This allowed for the exploration of the sensitivity of the results to the definition of “extreme values.”

`Statistical Analysis of Extreme Values (scale=2)`: The same statistical analysis was conducted for the outliers identified with a whisker scale of 2. The results were compared with those obtained with a whisker scale of 1.5.

`Comparison of Original and Modified Data (scale=2)`: The original and modified dataframes were compared again to observe the outliers identified with a whisker scale of 2. The results were compared with those obtained with a whisker scale of 1.5.

### Trend Analysis Task
`Data Cleaning`: The dataframe was cleaned by dropping rows with NaN values. The ‘Date’ and ‘Time’ columns were formatted to datetime type, and a new column, ‘Week Day’ was added to the dataframe.

`Trend Analysis in CO Values`: To identify a trend in CO values, the mean hourly values of CO were calculated for each day of the week. The data was grouped by ‘Week Day’, and the mean of ‘PT08.S1(CO)’ was calculated for each group. Bar plots were created to visualize the mean hourly values for each day and for each hour of the day.

`Correlation Analysis`: Pearson’s correlation was used to find the correlation between all the features. A heatmap was created to visualize the correlations.

`Pairplot Visualization`: Pairplots were created for each pair of features to visualize the relationships between features. The histograms on the diagonal allowed us to see the distribution of each feature.

`Seasonal Analysis`: A function was defined to assign the seasons based on the astronomical/meteorological definitions. The ‘Date’ column was used to extract the season information, and a new column ‘Season’ was added to the dataframe. Pairplots were created for each pair of features, colored by the season, to visualize the relationships between features in different seasons.

`Trend Analysis of Each Attribute`: To analyze the trend of each attribute, the monthly average points for each attribute were calculated. The data was grouped by ‘Month’ and ‘Month_Name,’ and the mean of each attribute was calculated for each group. The grouped data was sorted by ‘Month.’

A figure with subplots was created, one for each attribute. For each attribute, a bar plot was created to visualize the monthly average values. A rolling average line was also added to the plot to show the trend over time. The x-axis labels were rotated for better readability. The rolling average of each attribute was calculated with a window size of 1. This provided a smoothed line that represents the trend of the attribute over time


## Instructions to Reproduce Figures

If you open the `code_project.ipynb` file in the `code` folder and open it using `Jupyter Notebook` and click on the `Restart and Run All Cells` option, all results and figures will be produced automatically. You don't need to do any other steps. But just in case if the user want to know more, he can follow the below steps:

At first, import the necessary libraries and load the data.
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings('ignore')
df = pd.read_csv("../dataset/AirQuality.csv", sep=";", decimal=',')
```

Secondly, do the initial data cleaning steps:
1- Dropping the last 2 columns (extra & all-nan)
2- Dropping extra fully empty rows
3- Converting "-200" data to "NaN" using `np.nan` and `df.replace`
4- Dropping NMHC(GT) column as it contains a high percentage of null values

So your dataframe that is `df` is ready to go.

Here, we provided detailed instructions on how to reproduce each figure in the project report. 

### Figure 1: [Illustration of the concentration of NOX(GT) [ppb] for one year (Early March 2004 – Early April 2005)]
Run the `my_plot(df, df.columns[2:])` command and below code:
```python
interpol_df = df.copy()
interpol_df = interpol_df[interpol_df.columns[2:]] # Because the first two columns are dates.

interpol_df = interpol_df.interpolate(method='nearest')

print("\n")
print(42*" " + "\033[1;34m Filled NaNs Using Nearest Interpolation Technique \033[0m")
plot_orig_modif_series(df, interpol_df, interpol_df.columns[2:])
```

### Figure 2: [Histograms and probability density plots for each attribute in the dataset]
Just run this code:
```python
plot_histograms_density(df, df.columns[2:])
```

### Figure 3: [Comparasion of Outlier Ratios For All Attributes (Both scales 1.5 and 2)]
Run below code for scale 1.5:
```python
copy_df1 = df.copy()
df_out_edited1, outliers1 = remove_outliers_IQR(copy_df1, copy_df1.columns[2:], scale=1.5, mode="replace")
```
Run below code for scale 2:
```python
copy_df2 = df.copy()
df_out_edited2, outliers2 = remove_outliers_IQR(copy_df2, copy_df2.columns[2:], scale=2, mode="replace")
```

### Figure 4: [Time series plots to display outliers clearly (Both scales 1.5 and 2)]
Run below code for scale 1.5:
```python
copy_df1 = df.copy()
df_out_edited1, outliers1 = remove_outliers_IQR(copy_df1, copy_df1.columns[2:], scale=1.5, mode="replace")

print("\n\033[1;34m Compare modified and original data and see the outliers\033[0m")
plot_orig_modif_series(df, df_out_edited1, df.columns[2:])
```

Run below code for scale 2:
```python
copy_df2 = df.copy()
df_out_edited2, outliers2 = remove_outliers_IQR(copy_df2, copy_df2.columns[2:], scale=2, mode="replace")

print("\n\033[1;34m Compare modified and original data and see the outliers\033[0m")
plot_orig_modif_series(df, df_out_edited2, df.columns[2:])
```

Before entering the steps for reproducing Figures 5, 6, 7, and 8 do below steps just for one time:

1- Eliminating rows with NaN values:
```python
df3 = df_out_edited2.dropna(how='any', axis=0)
df3.reset_index(drop=True,inplace=True)
```

2- Formatting Date and Time to datetime type:
```python
df3['Date'] = pd.to_datetime(df3['Date'],dayfirst=True) 
df3['Time'] = pd.to_datetime(df3['Time'],format= '%H.%M.%S' ).dt.time
```

3- Adding a column with the week days:
```python
df3['Week Day'] = df3['Date'].dt.day_name()
```

4- Rearranging columns:
```python
cols = df3.columns.tolist()
cols = cols[:1] + cols[-1:] + cols[1:14]
df3 = df3[cols]
```

### Figure 5: [Illustration of the CO concentration trend over 24 hours on Monday and Sunday]
Grouping the data by 'Week Day' and calculating the mean of 'PT08.S1(CO)' for each group
```python
grouped_data = df3.groupby('Week Day')['PT08.S1(CO)'].mean().reset_index()
```

Run below code:
```python
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Create a figure with 7 subplots, one for each day of the week
fig, axs = plt.subplots(7, 1, figsize=(20, 50), dpi=300)

for i, day in enumerate(days):
    day_data = df3[df3['Week Day'] == day]
    
    # Create a bar plot on the i-th subplot
    sns.barplot(x='Time', y='PT08.S1(CO)', data=day_data.sort_values('Time'), ax=axs[i])
    
    axs[i].set_title(f"Mean Hourly Values of PT08.S1(CO) on {day}")
    axs[i].set_xticklabels(axs[i].get_xticklabels(), rotation=90)

# Adjust the layout
plt.tight_layout()

# Save the figure
# plt.savefig("C:/Users/Ali/Desktop/weekly_plots.png")

# Show the figure
plt.show()
```

### Figure 6: [Heatmap plot to visualize the correlations between the features]
Run below code:
```python
plt.figure(figsize=(10,5))
sns.heatmap(df3.corr(),cmap='YlGnBu',annot=True)
plt.show()
```

### Figure 7: [Pair plot of our attributes based on the calculated season]
Extracting season information from Date column:
```python
def season(date):
    year = str(date.year)
    seasons = {'spring': pd.date_range(start=year+'/03/21', end=year+'/06/20'),
               'summer': pd.date_range(start=year+'/06/21', end=year+'/09/22'),
               'autumn': pd.date_range(start=year+'/09/23', end=year+'/12/20')}
    if date in seasons['spring']:
        return 'spring'
    if date in seasons['summer']:
        return 'summer'
    if date in seasons['autumn']:
        return 'autumn'
    else:
        return 'winter'

df3['Season'] = df3['Date'].map(season)
```

And run below code:
```python
sns.pairplot(df3, hue='Season')
plt.show()
```

### Figure 8: [The average values of each attribute of the dataset in 12 months of a year]
Run below code:
```python
# List of columns to plot
columns_to_plot = df3.columns.drop(['Date', 'Month', 'Month_Name', 'Time', 'Week Day', 'Season'])

# Create a figure with subplots, one for each column to plot
fig, axs = plt.subplots(len(columns_to_plot), 1, figsize=(7, 50), dpi=300)

# Loop over the columns to plot
for i, column in enumerate(columns_to_plot):
    # Grouping the data by 'Month' and 'Month_Name' and calculating the mean of the current column for each group
    grouped_data = df3.groupby(['Month', 'Month_Name'])[column].mean().reset_index()

    # Sorting the grouped data by 'Month'
    grouped_data = grouped_data.sort_values('Month')

    # Calculate the rolling average of the current column
    window_size = 1  # You can adjust this value
    grouped_data['Rolling_Avg'] = grouped_data[column].rolling(window=window_size).mean()

    # Create a bar plot on the i-th subplot
    sns.barplot(x='Month_Name', y=column, data=grouped_data, ax=axs[i])

    # Add a rolling average line to the plot
    axs[i].plot(grouped_data['Month_Name'], grouped_data['Rolling_Avg'], color='blue')

    # Set the title of the plot
    axs[i].set_title(f'Monthly Average Values of "{column}"')
    axs[i].set_xlabel('')

    # Rotate the x-axis labels for better readability
    axs[i].set_xticklabels(axs[i].get_xticklabels(), rotation=90)

# Adjust the layout
plt.tight_layout()

# Save the figure
# plt.savefig("C:/Users/Ali/Desktop/monthly_plots.png")

# Show the figure
plt.show()
```

## Results
In this part we summarized the results of this project.

### Data Visualization Result

<caption>Table 2: Distribution Results of Our Attributes</caption>

| Column        | Skewness                | Outliers                |
|---------------|-------------------------|-------------------------|
| CO(GT)        | right skewed            | some outliers           |
| PT08.S1(CO)   | right skewed            | many outliers           |
| C6H6(GT)      | right skewed            | many outliers           |
| PT08.S2(NMHC) |                         | almost many outliers    |
| NOx(GT)       | right skewed            | so many outliers        |
| PT08.S3(NOx)  |                         | many outliers           |
| NO2(GT)       |                         | some outliers           |
| PT08.S4(NO2)  |                         | some many outliers      |
| PT08.S5(O3)   | right skewed            | some many outliers      |
| T             | multimodal distribution | no/very few outliers    |
| RH            |                         | no outliers             |
| AH            | multimodal distribution | no/very few outliers    |


### Extreme Value Analysis Result

I have computed various descriptive statistics for the outliers in all columns of data, including count, mean, median, minimum, maximum, standard deviation, variance, and skewness that have shown in Table 3 and Table 4. The frequency of extreme values (count values) on scale = 1.5 is more frequency of extreme values on scale = 2. If scale = 2, the extreme values have more ranges (min value, max value, and mean value). The variability of the extreme values (The standard deviation of the extreme values for each feature) in scale = 1.5 is more than scale = 2.

<caption>Table 3: Descriptive Statistics for Outliers (whisker scale of 1.5)</caption>

| Statistic | CO(GT) | PT08.S1(CO) | C6H6(GT) | PT08.S2(NMHC) | NOx(GT) | PT08.S3(NOx) | NO2(GT) | PT08.S4(NO2) | PT08.S5(O3) | T   | RH  | AH  |
|-----------|--------|-------------|----------|---------------|--------|--------------|---------|--------------|-------------|-----|-----|-----|
| count     | 242.0  | 118.0       | 230.0    | 65.0          | 439.0  | 241.0        | 110.0   | 97.0         | 93.0        | 3.0 | 0.0 | 2.0 |
| mean      | 6.7    | 1774.9      | 34.4     | 1799.2        | 852.3  | 1651.8       | 262.2   | 2467.5       | 2232.4      | 44.1|     | 2.2 |
| median    | 6.4    | 1754.5      | 32.6     | 1770.0        | 807.0  | 1581.0       | 252.5   | 2464.0       | 2197.0      | 44.3|     | 2.2 |
| min       | 5.6    | 1673.0      | 28.4     | 1689.0        | 668.0  | 1437.0       | 238.0   | 551.0        | 2087.0      | 43.4|     | 2.2 |
| max       | 11.9   | 2040.0      | 63.7     | 2214.0        | 1479.0 | 2683.0       | 340.0   | 2775.0       | 2523.0      | 44.6|     | 2.2 |
| std       | 1.1    | 84.7        | 5.6      | 105.3         | 163.1 | 216.0        | 23.1    | 222.2        | 124.3       | 0.6 |     |     |
| var       | 1.3    | 7175.9      | 31.6     | 11082.1       | 26604.6| 46658.1      | 535.5   | 49393.7      | 15441.7     | 0.4 |     |     |
| skew      | 1.6    | 1.0         | 1.7      | 1.3           | 1.2   | 1.8          | 1.3     | -6.7         | 0.9         | -1.3|     |     |


<caption>Table 4: Descriptive Statistics for Outliers (whisker scale of 2)</caption>

| Statistic | CO(GT) | PT08.S1(CO) | C6H6(GT) | PT08.S2(NMHC) | NOx(GT) | PT08.S3(NOx) | NO2(GT) | PT08.S4(NO2) | PT08.S5(O3) | T   | RH  | AH  |
|-----------|--------|-------------|----------|---------------|--------|--------------|---------|--------------|-------------|-----|-----|-----|
| count     | 113.0  | 31.0        | 106.0    | 13.0          | 246.0  | 114.0        | 34.0    | 21.0         | 17.0        | 0   | 0   | 0   |
| mean      | 7.6    | 1892.4      | 38.9     | 1964.4        | 957.1  | 1817.9       | 291.1   | 2644.8       | 2448.4      |     |     |     |
| median    | 7.3    | 1882.0      | 37.0     | 1958.0        | 910.5  | 1756.5       | 284.5   | 2641.0       | 2452.0      |     |     |     |
| min       | 6.5    | 1819.0      | 33.2     | 1889.0        | 782.0  | 1593.0       | 270.0   | 2568.0       | 2359.0      |     |     |     |
| max       | 11.9   | 2040.0      | 63.7     | 2214.0        | 1479.0 | 2683.0       | 340.0   | 2775.0       | 2523.0      |     |     |     |
| std       | 1.1    | 61.7        | 5.3      | 84.3          | 147.4 | 210.3        | 18.6    | 51.9         | 56.4        |     |     |     |
| var       | 1.2    | 3806.4      | 28.5     | 7106.8        | 21739.6| 44232.1      | 346.4   | 2696.3       | 3175.6      |     |     |     |
| skew      | 1.5    | 0.7         | 1.7      | 2.4           | 1.1   | 1.8          | 1.1     | 0.9          | -0.1        |     |     |     |


For the whisker scale of `1.5`, we have more extreme values in all attributes compared to the whisker scale of `2`. The `NOX(GT)` variable has the most extreme values in both whisker scales. We almost don’t have extreme values in the T, RH, and AH variables in both whisker scales.

We found that usually, in `Nov` and `Dec`, we have extreme values. It could be related to temperature inversions, where a layer of warm air traps cooler air near the ground, can prevent pollutants from dispersing, and lead to the buildup of pollutants in the lower atmosphere.

### Trend Analysis Result

To identify a trend in CO values, I calculated the mean hourly values of `PT08.S1(CO)` on each day of the week. We illustrated that the two peaks of CO concentration in the city are `8 AM` and `7 PM`, the beginning and end of office hours, respectively. But on weekends, the peak hours shift to the later hours (`11 AM` and `7 PM`), which makes sense.

Also by using a correlation matrix we found that there is a correlation between all the pollutants but the columns ‘T,’ ‘RH,’ and ‘AH’ don’t have a strong correlation with other features (pollutants). NO2(GT) and NOx(GT) have correlations with other features but are not that strong as compared to CO(GT), C6H6(GT), and Columns with PTs (PT08). CO(GT) and C6H6(GT) can be the columns that are correlated with all other features and can be the target.

To look at the trend of each attribute, we have extracted Monthly Average Values for each attribute. We found that in `August`, we have the minimum values of pollution, maximum temperature, and maximum absolute humidity.









