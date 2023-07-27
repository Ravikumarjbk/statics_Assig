#Q1>
"""There are three measure centeral tendency is
 mean, median , mode"""
#Q2
"""mean: The mean, also known as the average, is calculated by summing up 
all the values in the dataset and then dividing that sum by the number of data points

median: The median is the middle value of a dataset when it is ordered from smallest to largest. 
If the dataset has an odd number of observations, the median is the middle value itself. 
If the dataset has an even number of observations, the median is the average of the two middle values.

mode: The mode is the value that appears most frequently in the dataset. 
It is possible to have one mode (unimodal), two modes (bimodal), or more (multimodal) in a dataset. 
In some cases, there may be no mode if all values have the same frequency."""

#Q3
import numpy as np
ar1 = [178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]
# ar1_mean = np.array(ar1).mean() #177.01875
# ar1_median = np.median(ar1) #177.0
# l1 = [111,22,11,11,55,66,44,55]
# ar1_mode = np.mod(l1)
# print(ar1_mode)

# #Q4
# std_ar1 = np.std(ar1)
# print(std_ar1)

#Q5
"""Range:
The range is the simplest measure of dispersion and is calculated as the difference between the maximum and minimum values 
in the dataset. It provides an idea of how much the data values vary over the entire range of the dataset
Variance:  measures the average squared deviation of each data point from the mean. It gives a sense of how much the data points deviate from the mean on average.
 A higher variance indicates a more significant spread of data points
The standard deviation is the square root of the variance. It provides a measure of the dispersion in the original units of the data.
  A larger standard deviation indicates a greater spread of data points,
  while a smaller standard deviation suggests that the data points are closer to the mean."""
#Q6
"""The diagram consists of overlapping circles (or other shapes) that represent sets, and the overlapping regions indicate the elements 
that are common to the sets. The non-overlapping regions represent the elements unique to each set."""
#Q7
# A = (2,3,4,5,6,7)
# B = (0,2,6,8,10)
"""
(i) A B {2,6}
(ii) A ⋃ B{0,3,4,5,6,7,8,10}

"""
#Q8
"""Skewness in data is a statistical measure that describes the asymmetry of the probability distribution or frequency distribution of a dataset.
 It indicates whether the data is skewed to the left (negatively skewed), skewed to the right (positively skewed), or approximately symmetric"""
#Q9
"""If a dataset is right-skewed, the position of the median with respect to the mean will be to the left of the mean. 
In other words, the median will be less than the mean.

In a right-skewed distribution, the tail on the right side is longer, which means there are some unusually high values 
that pull the mean towards the right. 
The mean is sensitive to extreme values (outliers) and tends to be influenced by the larger values in the dataset."""
#Q10
"""Covariance:
Covariance measures the degree of joint variability between two variables. 
It indicates whether the two variables tend to increase or decrease together. 
A positive covariance suggests that when one variable increases, the other tends to increase as well.
 A negative covariance suggests that when one variable increases, the other tends to decrease.
Correlation is a standardized version of covariance. It measures both the strength and the direction of the linear relationship between
 two variables. Correlation values are bound between -1 and 1. A correlation of +1 indicates a perfect positive linear relationship, -1 
 indicates a perfect negative linear relationship, and 0 indicates no linear relationship."""
#Q11
"""sample_mean = (Sum of all values in the sample) / (Number of data points in the sample)

dataset = 78, 85, 90, 65, 72]
Sum = 78 + 85 + 90 + 65 + 72 = 390
Number of data points (n) = 5
Sample Mean (x̄) = 78"""
#Q12
"""Mean: The mean is the average of all the data points in the distribution. 
For a perfectly symmetrical normal distribution, the mean is equal to the median and the mode. The mean represents the balance point of the data, 
and its value is affected by outliers.

Median: The median is the middle value of the data when it is arranged in ascending or descending order. 
In a perfectly symmetrical normal distribution, the median is equal to the mean and the mode. Unlike the mean, 
the median is not influenced by extreme values or outliers, making it a robust measure of central tendency.

Mode: The mode is the value that appears most frequently in the data set. For a normal distribution, 
the mode is also equal to the mean and median in a perfect symmetrical distribution. However, it is possible to have a multimodal normal 
distribution, where there is more than one mode."""
#Q14
"""Outliers can have a significant impact on measures of central tendency and dispersion in a data set. 
An outlier is an observation that differs significantly from the rest of the data points, often lying far away from the majority of the values.
 The presence of outliers can distort the typical patterns and characteristics of the data, leading to misleading or biased results when computing 
 central tendency and dispersion measures."""