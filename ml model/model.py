
import pandas
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pandas.read_csv("dataset.csv")

X = df[['Temperature', 'Humidity',"Wind"]]
y = df['Acreage']

regr2 = linear_model.()
regr2.fit(df[["Wind"]], df["Acreage"])
plt.scatter(df['Wind'], df['Acreage'])
y_pred = regr2.predict(df[["Wind"]])
plt.plot(df[["Wind"]], y_pred, color = 'red', linewidth = 2)

plt.show()

regr = linear_model.LinearRegression()
regr.fit(X, y)

predicted = regr.predict([[87,32, 2]])
print(predicted)