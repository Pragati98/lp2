# Python Code to find out the equation of the Best Fit Line in Linear Regression
#Import the Python numpy mdule and call it np
import numpy as np

# The given data for number of hours of driving is as follows
# The numpy array is used to convert data into the array x_values
x_values = np.array([10,9 ,2 ,15,10,16,11,16], dtype=np.float64)

#The given data for risk score on a scale of 0-100 is as follows
# The numpy array is used to convert data into the array y_values
y_values = np.array([95,80,10,50,45,98,38,93], dtype=np.float64)

# define the function to calculate mean of the given values
def mean(m_values):
    sm=0
    kount=0
    for num in m_values:
        sm = sm + num
        kount = kount + 1
    return float(sm) / kount

# Define a function to find the values of
# coefficients m and b of a Best-fit-line
# using statitical formulas
def best_fit_line(x_values,y_values):
    m = (((mean(x_values)*mean(y_values)) - mean(x_values*y_values)) /
         ((mean(x_values)*mean(x_values)) - mean(x_values*x_values)))
    b = mean(y_values) - m*mean(x_values)
    return m, b

m, b = best_fit_line(x_values, y_values)
print("Equation of Best Fit Line is: " + "y = " + str(round(m,2)) + "x + " + str(round(b,2)) )

# y values of regression line
regression_line = [(m*x)+b for x in x_values]

# To plot a regression line, choose a value from the given dataset
# say x_prediction = 15
# using the equation of line, predict the value, say y_prediction
x_prediction = 15
y_prediction = (m*x_prediction)+b

# plot the data points as well as regression line 
# import matplotlib library for plotting data points
# and regression line 
import matplotlib.pyplot as plt
from matplotlib import style

plt.title('Plot of Linear Regression')
plt.scatter(x_values, y_values,color='#5b9dff',label='data')
plt.scatter(x_prediction, y_prediction, color='#fc003f', label="predicted")
plt.plot(x_values, regression_line, color='000000', label='regression line')
plt.legend(loc=4)
plt.show()
