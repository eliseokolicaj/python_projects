import matplotlib.pyplot as plt 
from random_walk import RandomWalk

#Make a random walk
rw = RandomWalk(50000)
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots(figsize = (15,10))
point_number = range(rw.num_points)
#ax.plot(rw.x_values, rw.y_values, linewidth = 3)
ax.scatter(rw.x_values, rw.y_values,c=point_number,cmap = plt.cm.Blues, edgecolors = 'none', s = 1)

# Emphasize the first and last points.
ax.scatter(0, 0, c = 'green', s = 90)
ax.scatter(rw.x_values[-1],rw.y_values[-1], c = 'red', s = 90)

#Remove the axis
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

#Set the title and labels
ax.set_title('Random Walk', fontsize = 20)
ax.set_xlabel('X-Values', fontsize = 15)
ax.set_ylabel('Y-Values', fontsize = 15)

plt.show()