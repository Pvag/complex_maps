import numpy as np
import matplotlib.pyplot as plt

def monocolor_complex_square_map(xs, ys):
    for y in ys:
        for x in xs:
            # draw on plot 1
            axes[0].scatter(x, y, color='red', marker='o')

            # point after the map
            x_map = x*x - y*y
            y_map = 2*x*y
            # draw on plot 2
            axes[1].scatter(x_map, y_map, color='blue', marker='o')

def color_complex_square_map(xs, ys):
    x_max = xs[-1]
    y_max = ys[-1]
    for y in ys:
        for x in xs:
            color = ((x+x_max)/(2*x_max), (y+y_max)/(2*y_max), (x+x_max+y+y_max)/(2*x_max+2*y_max))

            # draw on plot 1
            axes[0].scatter(x, y, color=color, marker='o')

            # point after the map
            x_map = x*x - y*y
            y_map = 2*x*y

            # draw on plot 2
            axes[1].scatter(x_map, y_map, color=color, marker='o')

def bland_colors(x, y, x_max, y_max):
    color = ((x+x_max)/(2*x_max), (y+y_max)/(2*y_max), (x+x_max+y+y_max)/(2*x_max+2*y_max))

    return color

def blue_green_colors(x, y):
    theta = np.arctan(y/x)
    max_theta = np.pi/2.
    b = ((theta+max_theta)/(2*max_theta))
    g = (1. - b)
    color = (0, g, b)
    alpha = 1 - (np.sqrt(x*x + y*y))/8.2

    return color, alpha

def color_pos_half_complex_square_map(xs, ys):
    x_max = xs[-1]
    y_max = ys[-1]
    point_size = 27
    for y in ys:
        for x in xs:
            if (x > 0):
                # color = (abs(x)/x_max, abs(y)/y_max, abs(x+y)/(x_max+y_max))
                # color = bland_colors(x, y, x_max, y_max)
                color, alpha = blue_green_colors(x, y)

                # draw on plot 1
                axes[0].scatter(x, y, color=color, alpha=alpha, marker='o', s=point_size)

                # point after the map
                x_map = x*x - y*y
                y_map = 2*x*y

                # draw on plot 2
                axes[1].scatter(x_map, y_map, color=color, alpha=alpha, marker='o', s=point_size)

# Square  grid
# x
x_0 = -2
x_n = 10
x_end = -x_0
# y
y_0 = x_0
y_n = x_n
y_end = -y_0

xs = np.linspace(x_0, x_end, x_n)
ys = np.linspace(y_0, y_end, y_n)

num_subplots = 2
fig, axes = plt.subplots(1, num_subplots, figsize=(9, 8.2))

# monocolor_complex_square_map(xs, ys)
# color_complex_square_map(xs, ys)
color_pos_half_complex_square_map(xs, ys)

x_min_plot = -5
x_max_plot = -x_min_plot
y_min_plot = -8.5
y_max_plot = -y_min_plot

axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].set_title('The initial grid')
axes[0].axis('on')
axes[0].set_aspect('equal', adjustable='box')
axes[0].set_xlim(x_min_plot, x_max_plot)
axes[0].set_ylim(y_min_plot, y_max_plot)
axes[0].grid(True, linestyle='--', alpha=0.7)

axes[1].set_xlabel('x')
axes[1].set_ylabel('y')
axes[1].set_title('The grid after the complex square map')
axes[1].axis('on')
axes[1].set_aspect(1)
axes[1].set_xlim(x_min_plot, x_max_plot)
axes[1].set_ylim(y_min_plot, y_max_plot)
axes[1].grid(True, linestyle='--', alpha=0.7)

fig.suptitle('The Complex Square Map', fontsize=16, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'), y=.95)

plt.savefig('complex_square.png')
plt.show()