import matplotlib.pyplot as plt


def kernel_function(xi, x, h):
    z = abs((x - xi) / h)
    if z > 0.5:
        return 0
    return 1


def density_estimate(data, x, h):
    kernel_sum = 0
    for i in range(len(data)):
        kernel_sum = kernel_sum + kernel_function(data[i], x, h)
    return (1 / (len(data) * h)) * kernel_sum


if __name__ == "__main__":
    given_data = [1, 5, 6, 9, 15]
    height = 3
    x_array = []
    y_array = []
    x_array_all_values = []
    y_array_all_values = []
    x_array_old = []
    y_array_old = []
    for point in range(-5, 30):
        new_val = density_estimate(given_data, point, height)
        y_array_all_values.append(new_val)
        x_array_all_values.append(point)
        print(new_val)
        if len(y_array) == 0:
            y_array.append(new_val)
            x_array.append(point)
        elif y_array[len(y_array) - 1] != new_val:
            y_array_old.append(y_array[len(y_array) - 1])
            x_array_old.append(point)
            y_array.append(new_val)
            x_array.append(point)
            print(new_val)
    # add point to the end to add arrow towards -infinity
    x_array.append(20)
    y_array.append(0)
    # add arrow towards +infinity
    plt.scatter(x_array[0], y_array[0], color="green",
                marker="<")
    # add arrow towards -infinity
    plt.scatter(x_array[len(x_array) - 1], y_array[len(y_array) - 1], color="green",
                marker=">")
    plt.grid()
    # add minor ticks so that graph is readable
    plt.xticks(range(-5, 21), minor=True)

    # draw step graph to connect all points in the step graph
    plt.step(x_array, y_array, where='post')

    # delete points which should not appear as step points. These were added to show graph extending to both the infinities
    del x_array[0]
    del y_array[0]
    del x_array[len(x_array) - 1]
    del y_array[len(y_array) - 1]

    # draw over the vertical lines with red dotted lines
    for i in range(0, len(x_array)):
        plt.plot((x_array_old[i], x_array[i]), (y_array_old[i], y_array[i]), 'w-')
        plt.plot((x_array_old[i], x_array[i]), (y_array_old[i], y_array[i]), 'r--')

    # draw step graph with only the points. Shows closed green circles
    plt.step(x_array, y_array, 'go', where='post')

    # draw step graph with the points where the value changed. Shows open green circles
    plt.scatter(x_array_old, y_array_old, color="green",
                marker="o")
    plt.scatter(x_array_old, y_array_old, color="white",
                marker=".")

    plt.show()
    print("Done")
