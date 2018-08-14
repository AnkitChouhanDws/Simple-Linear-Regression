              #####################################  Simple Linear Regression  ##############################

  
                                                    #Importing-the-libraries


# 1. For calculations
import numpy as np
# 2. For plotting the graph
import matplotlib.pyplot as plt
# 3. For creating series and data-frames
import pandas as pd


                                                      #Loading-the-dataset


dataset = pd.read_csv('Path to dataset')
# Extracting the independent variables and dependent variables from the dataset
X = dataset.iloc[:,:-1].values
y= dataset.iloc[:, 1].values
# Here X is the dependent_variable and y is the dependent_variable



                                                 #Create-testing-training-data


# Importing the train_test_split class
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(X,y, test_size=1/3, random_state=0)
# Here test_size is the part of the dataset used for testing purpose
# The most common values of test_size are: 0.2, 0.25 and 0.3



                                      # Fitting-simple-linear-regressor-to-the-training-set   
                                                                                   

# Import the LinearRegression class
from sklearn.linear_model import LinearRegression
# Create the regressor object
regressor= LinearRegression()
# Fit the regressor in our testing data
regressor.fit(X_train, y_train)
# Now our model has learned the correlation between the independent and dependent variable



                                                # Predict-the-results-for-test_set


y_predicted= regressor.predict(X_test)




                                                        # Visualisation


# 1.  Plotting for training set data

plt.scatter(X_train, y_train, color='red')
# The points are red in color and denoted by *.
# Plotting the regression line
plt.plot(X_train, regressor.predict(X_train), color='blue')
# Add the title
plt.title('Salary vs Years of Experience(trained data)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# 2. Plotting the testing set data
plt.scatter(X_test, y_test, color='red')
# Plot the same regression line
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience (Tested set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()



############################################################  END  ####################################################


