import matplotlib.pyplot as plt
import numpy as np
import math

w = np.arange(0, 1, 0.01)
x = 1000
# n = np.arange(0, 50, 1)
# beta = 0.5
# x = 10000
r = 1.1
theta = 0.1
N = 9
b = [0.1 for i in range(0, 9)]
beta = 0.3
# w = 0.5
C = 10
p = 0.3
# n = np.arange(0, 100, 1)
n = 50
# z = (theta * 9 * (r + 2 * theta) * x) / (theta + (r + 2 * theta) * 8) - \
#     ((p - beta - w) * (r + theta) - w) / \
#     (2 * theta + 2 * (r + 2 * theta) * 8) * 8 / b[0]

# y = (r + 2 * theta) * x - ((p - beta + w) *
#                            (r + theta) - 9 * w) / (2 * theta) * 9 / b[0]
# J = 2 * b[0] * (r + 2 * theta) * 8 * (C / 9) + \
#     (r + 2 * theta) * (p - beta + w)
# y = - (r + 2 * theta) / (b[0] * 9) * x * x - \
#     ((r + 2 * theta) * (p - beta + w) - 9 * w) * \
#     ((r + 2 * theta) * (p - beta + w) - 9 * w) / theta - beta * 9 * C / r
# z = - b[0] * (r + 2 * theta) * x * x + J / theta * x +\
#     J * J / (4 * r * theta * theta)\
#     - beta * C / r + J / (r * theta) * 8 * C / 9
# v = (x + 1 - np.sqrt(x * x + 2)) / (2 * x - 1) * 10
# y = (x + 1 - np.sqrt(2 * x + 1)) / (x * x) * 10
# z = 10 * ((x + 1 - np.sqrt(2 * x + 1)) / (x * x) -
#           (x + 1 - np.sqrt(x * x + 2)) / (2 * x - 1))
tn = (-((p - beta + w) * (r + theta) - n * w) /
      (2 * theta) * n * (1 / b[0]) + (r + 2 * theta) * x) / n
tv = - ((p - beta + w) * (r + theta) - w) / \
    (2 * (theta + (r + 2 * theta) * (n - 1))) * \
    n * (1 / b[0]) + (theta * n * (r + 2 * theta) * x) / \
    (theta + (r + 2 * theta) * (n - 1))
wn = (- (r + 2 * theta) / (n * (1 / b[0])) * x * x +
      ((r + 2 * theta) * (p - beta + w) - n * w) / theta * x
      - ((r + theta) * (p - beta + w) - n * w) * (
    (r + 2 * theta) * (p - beta + w) - n * w) / theta * x -
    ((r + theta) * (p - beta + w) - n * w) /
    (4 * r * theta * theta) * n * b[0] - beta * n * C / r) / n
wv = - (b[0] * (r + 2 * theta) * x * x) + \
    x * ((2 * b[0] * (r + 2 * theta) / theta)
         * (n - 1) * (tv / n) + ((r + 2 * theta) * (p - beta + w) - w) / theta)  \
    - (1 / (4 * b[0] * r * theta * theta)) * ((r + theta) * (p + w - beta) - n * w + 2 * b[0] * (r + 2 * theta) * (n - 1) * tv / n) * ((r + theta) * (p + w - beta) - n * w + 2 * b[0] * (r + 2 * theta) * (n - 1) * tv / n) - beta * n * C / b[0] +\
    1 / (theta * r) * ((r + 2 * theta) * (p + w - beta) - n * w + 2 *
                       b[0] * (r + 2 * theta) * (n - 1) * (tv / n)) * (n - 1) * (tv / n)


def draw_and_obtain_figure(ax, subsum, ccc, name, x_label):
    """

    [draw a figure with two yaxis, subsum for the left
    and ccc the right. the ax is the xaxis. Then save the
    figure.]

    Arguments:
        ax {[list]} -- [x axis]
        subsum {[list]} -- [y value for the left y axis]
        ccc {[list]} -- [y value for the right y axis]
        name {[string]} -- [the name of saved figure]
    """
    # plt.rc('text', usetex=True)
    plt.rc('xtick', labelsize=16)
    plt.rc('ytick', labelsize=16)
    plt.rc('axes', labelsize=16)
    # width as measured in inkscape
    width = 3.487 *1.5
    height = width / 1.618

    fig, ax1 = plt.subplots()
    fig.subplots_adjust(left=.15, bottom=.16, right=.99, top=.97)

    color = 'blue'
    ax1.set_xlabel('w', fontsize=16)
    ax1.set_ylabel('Throughput', fontsize=16)
    ax1.plot(ax, subsum, color=color, linestyle="-.")
    # ax1.plot(ax, csum, color='b')
    ax1.tick_params(axis='y')

    color = 'red'
    # we already handled the x-label with ax1
    ax1.plot(ax, ccc, color=color)
    # ax1.tick_params(axis='y', labelcolor=color)
    fig.set_size_inches(width, height)
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    # plt.show()
    plt.legend(fontsize=14)
    name = name + ".pdf"
    plt.savefig(name)
    plt.show()


draw_and_obtain_figure(w, tn, tv, 'wthr', 'def')
exit()
import csv
try:
    ff = open('beta.csv', 'w', newline='')
    fw = csv.writer(ff)
except Exception:
    print('theta open failed')
    exit()
for i in range(len(beta)):
    if i == 0:
        continue
    tmp = (beta[i], wn[i], wv[i])
    fw.writerow(tmp)
if ff:
    ff.close()
# plt.title("1")
# print(wn)
# plt.plot(x, wn, color='red', label='C')
# plt.plot(x, wv, color='blue', label='N')
# # plt.plot(x, z, color='blue', label='N')
# plt.legend()
# plt.show()
