import numpy as np
from numpy.linalg import eig
from matplotlib import pyplot as plt

X = np.array([6, 1, 2, 4, -3,-4,-3])
Y = np.array([10, 1, 3, 6, -2,-1,-5])
Z =np.array([3, 1, 5, 2, 0,2,2])


# Question 3 a)
combined_array = np.vstack((X, Y, Z)).transpose()
print(combined_array)
combined_mean = combined_array.mean(axis=1)
print("2-D Mean", combined_mean)
cov_mat = np.cov(combined_array)
print("Covariance combined", cov_mat)


# Question 3 b)

eig_values, eig_vectors = eig(cov_mat)

idx = eig_values.argsort()[::-1]
eig_values = eig_values[idx]
eig_vectors = eig_vectors[:,idx]
# eig_values, eig_vectors = eig(cov_mat)
print("Eigen Values are: ", eig_values)
# Question 3 d)
print("First Principal Component: ", eig_vectors[0])

# Question 3 e)

# original point is xi, new vector is u
# x1 and u1 are column vectors
# calculate (uTx1)u
plt.scatter(X, Y)
plt.quiver(*[0,0], *2*eig_vectors[0], color=['r'], scale=21)


print(combined_array)
scalar_offset = np.dot(eig_vectors[0], combined_array)
print(scalar_offset)
i = 0
points_for_line = []
for projected_val in scalar_offset:
    vector_val = projected_val*eig_vectors[0]
    print(vector_val)
    points_for_line.append(vector_val)
    plt.plot((X[i], vector_val[0]), (Y[i], vector_val[1]), 'r--')
    plt.plot(X[i], Y[i])
    i = i+1

new_line_x = [x[0] for x in points_for_line]
new_line_x.append(eig_vectors[0][0])
new_line_y = [x[1] for x in points_for_line]
new_line_y.append(eig_vectors[0][1])
plt.plot(new_line_x,new_line_y,'g')
plt.grid()
plt.show()


# verify eigen vector
# np.dot(eig_vectors[0].transpose(),eig_vectors[1]) # should be 0
# np.dot(eig_vectors[1].transpose(),eig_vectors[1]) # should be 1
# np.dot(cov_mat,eig_vectors[0])/eig_vectors[0] # should be matrix of eig_value[0]

