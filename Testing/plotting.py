import matplotlib.pyplot as plt
from pontiPy import *


labels = ['Row 1', 'Row 2', 'Row 3', 'Row 4', 'Miss', 'False Alarm']
men_means = [20, 35, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
width = 0.5       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.barh(labels, men_means, width, label='Men')
ax.barh(labels, women_means, width, left=men_means, label='Women')

ax.set_ylabel('Entry size as a number of Observations')
ax.set_title('')
ax.legend()

plt.show()