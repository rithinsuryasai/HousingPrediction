import pandas
import matplotlib.pyplot

matplotlib.pyplot.figure(figsize=(20, 5))

data = pandas.read_csv('housing.csv.xls')
prices = data['MEDV']
features = data.drop('MEDV', axis=1)
for row, col in enumerate(features.columns):
    matplotlib.pyplot.subplot(1, 3, row+1)
    x = data[col]
    y = prices
    matplotlib.pyplot.plot(x, y, 'o')
    matplotlib.pyplot.title(col)
    matplotlib.pyplot.xlabel(col)
    matplotlib.pyplot.ylabel('prices')
matplotlib.pyplot.show()


def performance_metric(y_true, y_predict):
    from sklearn.metrics import r2_score
    score_ = r2_score(y_true, y_predict)
    return score_


score = performance_metric([3, -0.5, 2, 7, 4.2], [2.5, 0.0, 2.1, 7.8, 5.3])
print(score)
