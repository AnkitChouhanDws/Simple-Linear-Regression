# What is Regression?
***

- Regression takes a group of random variables, thought to be predicting Y, and tries to find a mathematical relationship between them. 
- This relationship is typically in the form of a straight line (linear regression) that best approximates all the individual data points.

Read more: Regression https://www.investopedia.com/terms/r/regression.asp#ixzz5OA1H851T 
Follow us: Investopedia on Facebook

# What is Simple Linear Regression?
***
Linear Regression can be of different types as:
- <font color= 'blue'>Simple Linear Regression</font>
- <font color= 'blue'>Multiple Linear Regression</font>

Here we will only discuss about Simple Linear Regression.<br>
Simple linear regression is a statistical method that allows us to summarize and study relationships between two continuous (quantitative) variables:

One variable, denoted x, is regarded as the predictor, explanatory, or independent variable.
The other variable, denoted y, is regarded as the response, outcome, or dependent variable.

We have certain set of x,y values and we have to find a straight line that best fits the points.

# What is the "Best Fitting Line"?
***
Let 
- y<sub>i</sub> denotes the observed response for experimental unit i
- x<sub>i</sub> denotes the predictor value for experimental unit i
- y<sup>^</sup><sub>i</sub> is the predicted response (or fitted value) for experimental unit i.<br><br>
Then, the equation for the best fitting line is:
y<sup>^</sup><sub>i</sub> = b<sub>0</sub> + b<sub>1</sub>x<sub>i</sub>
<br>
Here, b<sub>0</sub> is the intercept which the line cut on y-axis and b<sub>1</sub> is the slope(gradient) of the line.

![alt text](https://cdn-images-1.medium.com/max/800/1*KwdVLH5e_P9h8hEzeIPnTg.png)
<br><br>
Clearly, our prediction wouldn't be perfectly correct — it has some "prediction error" (or "residual error"). 

In general, when we use y<sup>^</sup><sub>i</sub> = b<sub>0</sub> + b<sub>1</sub>x<sub>i</sub> to predict the actual response yi, we make a prediction error (or residual error) of size e<sub>i</sub> = y<sub>i</sub> − y<sup>^</sup><sub>i</sub> <br>
A line that fits the data "best" will be one for which the n prediction errors — one for each observed data point — are as small as possible in some overall sense.
One way to achieve this goal is to invoke the "least squares criterion," which says to "minimize the sum of the squared prediction errors." That is:

The equation of the best fitting line is: 
y<sub>i</sub> = b<sub>0</sub> + b<sub>1</sub>x<sub>i</sub>
We just need to find the values b<sub>0</sub> and b<sub>1</sub> that make the sum of the squared prediction errors the smallest it can be.
That is, we need to find the values b<sub>0</sub> and b<sub>1</sub> that minimize:
Q = ∑<sup>n</sup><sub>i=1</sub> (y<sub>i</sub> − y<sup>^</sup><sub>i</sub>)<sup>2</sup>
Here's how you might think about this quantity Q:

- The quantity e<sub>i</sub> = y<sub>i</sub> − y<sup>^</sup><sub>i</sub>  is the prediction error for data point i.
- The quantity e<sup>2</sup><sub>i</sub> = (y<sub>i</sub> - y<sub>i</sub>)<sup>2</sup>  is the squared prediction error for data point i.
- And, the symbol ∑<sup>n</sup><sub>i=1</sub>  tells us to add up the squared prediction errors for all n data points.
Incidentally, if we didn't square the prediction error e<sub>i</sub> = y<sub>i</sub> − y<sup>^</sup><sub>i</sub> to get e<sup>2</sup><sub>i</sub> = (y<sub>i</sub>−y<sup>i</sup>)<sup>2</sup>, the positive and negative prediction errors would cancel each other out when summed, always yielding 0.
