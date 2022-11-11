import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN

min_pts = 3
epsilon = 2


# returns alphabet equivalent of number
# num starts from 0
def num_to_letter(num):
    return chr(97 + num)


# converts list to np array
def to_np_array(point):
    if type(point) is list:
        return np.array(point)


def l2_dist(point1, point2):
    point1 = to_np_array(point1)
    point2 = to_np_array(point2)
    sum_sq = np.sum(np.square(point1 - point2))
    # Doing squareroot and
    # printing Euclidean distance
    return np.sqrt(sum_sq)


data = [[4, 10], [5, 11], [10, 8], [3, 8], [6, 8], [9, 5], [8, 3], [13, 8], [1, 7], [2, 7], [6, 7], [8, 7], [12, 8],
        [13, 7], [8, 6], [14, 6], [6, 3], [7, 5], [10, 4], [4, 3], [3, 6], [9, 2], [11, 3], [15, 4], [13, 3], [13, 2]]

# print(l2_dist(data[3], data[4]))

# print(len(data))

neighborhood = {}

for x in range(0, len(data)):
    curr_point = num_to_letter(x)
    for y in range(0, len(data)):
        inner_point = num_to_letter(y)
        if l2_dist(data[x], data[y]) <= epsilon:
            l1 = neighborhood.get(curr_point, list())
            l1.append(inner_point)
            neighborhood[curr_point] = l1

print(neighborhood)

clustering = DBSCAN(eps=epsilon, min_samples=min_pts).fit(data)

# get the list of cores
core_samples_mask = np.zeros_like(clustering.labels_)
core_samples_mask[clustering.core_sample_indices_] = 1
# mark noise as -1
core_samples_mask[[x for x in range(0, len(clustering.labels_)) if clustering.labels_[x] == -1]] = -1

# Question 1 list the border points
border_points = {num_to_letter(x): data[x] for x in range(0, len(core_samples_mask)) if core_samples_mask[x] == 0}
print(border_points)

# Question 2 list the noise points
noise_points = {num_to_letter(x): data[x] for x in range(0, len(core_samples_mask)) if core_samples_mask[x] == -1}
print(noise_points)

X = [x[0] for x in data]
Y = [x[1] for x in data]

markers = ['+', 'o', '^', 's', 'D', '>', 'D']  # marker
color = ['k', 'b', 'r', 'g', 'y']

all_clusters = {}
all_clusters_alphabets = {}

for i in range(0, len(data)):
    li = all_clusters.get(clustering.labels_[i], list())
    li.append(data[i])
    all_clusters[clustering.labels_[i]] = li
    # alphabet labeled clusters for printing solution
    li2 = all_clusters_alphabets.get(clustering.labels_[i], list())
    li2.append(num_to_letter(i))
    all_clusters_alphabets[clustering.labels_[i]] = li2

# Question 3
print(all_clusters_alphabets)

for cluster in all_clusters:
    for data_point in all_clusters[cluster]:
        plt.scatter(data_point[0], data_point[1], c=color[cluster + 1], marker=markers[cluster + 1])

for i in range(0, len(data)):
    plt.annotate(num_to_letter(i), (X[i], Y[i]), textcoords="offset points", xytext=(0, 5))

plt.show()
