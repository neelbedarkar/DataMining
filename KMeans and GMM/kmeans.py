import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans


def find_sse(centers, labels, data_set, data_set_label):
    clusterwise_sse = [0, 0]
    for point in range(0, len(data_set)):
        clusterwise_sse[labels[point]] += np.square(data_set[point] - centers[labels[point]]).sum()
    print("Cluster-wise SSE for " + data_set_label)
    print(clusterwise_sse)
    print("Total SSE for " + data_set_label)
    print(clusterwise_sse[0] + clusterwise_sse[1])


points = ["x1", "x2", "x3", "x4", "x5"]
data = np.array([[0, 2],
                 [0, 0],
                 [2, 0],
                 [5, 0],
                 [5, 2]])
x, y = data.T

# Question 1a
kmeans = KMeans(n_clusters=2, init=[data[0], data[1]]).fit(data)
plt.subplot(1, 2, 1)
s = plt.scatter(x, y, c=kmeans.labels_)
x_means, y_means = kmeans.cluster_centers_.T
plt.scatter(x_means, y_means, c=[0, 1])
plt.annotate("Cluster 1 Mean ({}, {}) ".format(kmeans.cluster_centers_[0][0], kmeans.cluster_centers_[0][1]),
             (kmeans.cluster_centers_[0]), textcoords="offset points", xytext=(0, 10))
plt.annotate("Cluster 2 Mean ({:.2f}, {:.2f}) ".format(kmeans.cluster_centers_[1][0], kmeans.cluster_centers_[1][1]),
             (kmeans.cluster_centers_[1]), textcoords="offset points", xytext=(0, -15))
find_sse(kmeans.cluster_centers_, kmeans.labels_, data, "K-Means with x1 and x2")
for i in range(0, len(x)):
    plt.annotate(points[i] + "({}, {})".format(x[i], y[i]), (x[i], y[i]), textcoords="offset points", xytext=(-20, 10))

# Question 1b
# Plotting regular points for judging
plt.subplot(1, 2, 2)
s2 = plt.scatter(x, y)
for i in range(0, len(x)):
    plt.annotate(points[i] + "({}, {})".format(x[i], y[i]), (x[i], y[i]), textcoords="offset points", xytext=(-20, 10))

plt.subplot(1, 2, 2)
manual_labels = [0, 0, 0, 1, 1]
new_u1 = np.mean(data[0:3], axis=0)  # Looking at the graph and clustering
new_u2 = np.mean(data[3:5], axis=0)  # Looking at the graph and clustering
mean_array = np.array([new_u1, new_u2])
# Proving the Kmeans iterations do not change the means nor the clusters
kmeans_2 = KMeans(n_clusters=2, init=[new_u1, new_u2]).fit(data)
find_sse(kmeans_2.cluster_centers_, kmeans_2.labels_, data, "K-Means with manually picked centroids")
if manual_labels != list(kmeans_2.labels_):
    print("Not the same clusters!")
    print(kmeans_2.labels_)
if not np.allclose(kmeans_2.cluster_centers_, mean_array):
    print("Centers not equal!")
    print(kmeans_2.cluster_centers_)
    print(kmeans_2.cluster_centers_)

s2 = plt.scatter(x, y, c=kmeans_2.labels_)
for i in range(0, len(x)):
    plt.annotate(points[i] + "({}, {})".format(x[i], y[i]), (x[i], y[i]), textcoords="offset points", xytext=(-20, 10))

plt.annotate("Cluster 1 Mean ({:.2f}, {:.2f})".format(new_u1[0], new_u1[1]), new_u1, textcoords="offset points",
             xytext=(-5, 10))
plt.annotate("Cluster 2 Mean ({}, {})".format(new_u2[0], new_u2[1]), new_u2, textcoords="offset points",
             xytext=(-40, 10))
u_x, u_y = mean_array.T
#
plt.scatter(u_x, u_y, c=[0, 1])

print(new_u1)
print(new_u2)
plt.show()
print("c=kmeans")

# import seaborn as sns
# sns.scatterplot(x=x, y=y, hue=kmeans.labels_)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# dataset = [[0, 2],
#            [0, 0],
#            [2, 0],
#            [5, 0],
#            [5, 2]]
