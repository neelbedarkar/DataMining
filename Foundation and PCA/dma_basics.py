# This is a sample Python script.
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
import math
import matplotlib
X = np.array([8, 0, 7, 9, 2])
Y = np.array([24, 2, 18, 17, 2])

# Question 2 a)
x_mean = np.mean(X)
x_median = np.median(X)
x_mode = stats.mode(X, keepdims=False)

print("Mean of X is {:.5f}".format(x_mean))
print("Median of X is {:.0f}".format(x_median))
print("Mode of X is {:.0f}".format(x_mode[0]), "Count of Mode is: ", x_mode[1])


# Question 2 b)
y_variance = np.cov(Y, bias=True)

print("Biased variance of Y is: {:.5f}".format(y_variance))

# Question 2 c)
x_variance = np.cov(X, bias=True)
# np.std could also get the value.
x_std = math.sqrt(x_variance)
print(x_std)
x_values = np.linspace(x_mean - 5*x_std, x_mean + 5*x_std, 1000)
# plt.plot(x_values, stats.norm.pdf(x_values, x_mean, x_std))
# plt.show()


# Question 2 d)
print("Probability of X>80: {:.5f}".format(len([sample for sample in X if sample > 80])/len(X)))

# Question 2 e)
combined_array = np.vstack((X, Y))
combined_mean = combined_array.mean(axis=1)
print("2-D Mean", combined_mean)
cov_mat = np.cov(combined_array, bias=True)
print("Covariance combined", cov_mat)


# Question 2 f)
# Verify value
# print(cov_mat[0, 1]/(math.sqrt(y_variance)*x_std))
print("Correlation Coefficient: {:.5f}".format(np.corrcoef(X, Y)[0,1]))

# Question 2 g)

plt.scatter(X, Y)
plt.title('Scatter Plot Age vs Weight')
plt.scatter(combined_mean[0], combined_mean[1], c="red")
# plt.vlines(combined_mean[0], np.amin(Y), combined_mean[1], linestyles ="dotted", colors ="red")
# plt.hlines(combined_mean[1], np.amin(X), combined_mean[0], linestyles ="dotted", colors ="red")
plt.xlabel('Age')
plt.ylabel('Weight')
plt.legend(loc='best')
plt.text(combined_mean[0]+0.2, combined_mean[1], "Mean", horizontalalignment='left', size='medium', color='red', weight='semibold')
plt.show()
