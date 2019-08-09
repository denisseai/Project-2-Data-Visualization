import matplotlib.pyplot as pyplot

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

pyplot.style.use('seaborn')
fig, ax = pyplot.subplots()

#To plot a single point, use the scatter() method
ax.scatter(x_values, y_values, c=y_values, cmap=pyplot.cm.Blues, s=10) 

#Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squares of value", fontsize=14)

#Set size of tick labels
ax.tick_params(axis='both',which='major', labelsize=14)

#set range for eac axis
ax.axis([0, 1100, 0, 1100000])

pyplot.show()
