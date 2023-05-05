import matplotlib.pyplot as plt 

plt.style.use('seaborn')
input_values= range(1 , 1000)
squares = [ x**2 for x in input_values]

fig, ax = plt.subplots()
#ax.plot(input_values, squares, linewidth = 3)

#Scatter method
ax.scatter(input_values,squares,c=squares, cmap= plt.cm.Blues,s=4)

## Set chart title and label axes.
ax.set_title('Square Graph', fontsize = 20)
ax.set_xlabel('Value', fontsize = 14)
ax.set_ylabel('Square of value', fontsize = 14)

#Set size of tick labels
ax.tick_params(axis= 'both', which = 'major', labelsize = 14)

#Set the range for each axis.
ax.axis([0,1101,0,1100000])

plt.show()