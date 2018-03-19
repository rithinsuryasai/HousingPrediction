import numpy
import matplotlib.pyplot

# data

true, predicted = [3, -0.5, 2, 7, 4.2], [2.5, 0.0, 2.1, 7.8, 5.3]

# handles : legends

"""true_handle = matplotlib.pyplot.scatter(true, true, alpha=0.6, color='blue', label='true')

pred_handle = matplotlib.pyplot.scatter(true, predicted, alpha=0.6, color='red', label='predicted')

matplotlib.pyplot.legend(handles=[true_handle, pred_handle], loc='upper left')

fit = numpy.poly1d(numpy.polyfit(true, true, 1))

lim = numpy.linspace(min(true)-1, max(true)+1)

matplotlib.pyplot.plot(lim, fit(lim), alpha=0.3, color='black')

matplotlib.pyplot.show()"""

[t, p] = numpy.polyfit(true, true, 1)

print(numpy.poly1d([t, p]))
