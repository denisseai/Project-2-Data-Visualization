import matplotlib.pyplot as pyplot

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

pyplot.style.use('seaborn')
fig, ax = pyplot.subplots()
ax.plot(input_values, squares, linewidth=3)
ax.scatter(2, 4, s=200) #To plot a single point, use the scatter() method

#Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squares of value", fontsize=14)

#Set size of tick labels
ax.tick_params(axis='both',which='major', labelsize=14)

pyplot.show()
