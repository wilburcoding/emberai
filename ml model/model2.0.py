
import pandas
from sklearn import linear_model
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)  # allow CORS for all domains on all routes.

df = pandas.read_csv("dataset2.0.csv")

X = df[['temp', 'humidity', "wind","drought"]]
y = df['acreage']

regr2 = linear_model.LinearRegression()
regr2.fit(df[["drought"]], df["acreage"])
plt.scatter(df['drought'], df['acreage'])
y_pred = regr2.predict(df[["drought"]])
plt.plot(df[["drought"]], y_pred, color='red', linewidth=2)

# plt.show()

regr = linear_model.LinearRegression()
regr.fit(X, y)

predicted = regr.predict([[87, 32, 12,0]])


@app.route("/")
def req():
    # do processing here
    temp = request.args.get('temp')
    humidity = request.args.get('humidity')
    wind = request.args.get('wind')
    print([[int(temp), int(humidity), int(wind), 1]])
    pre = str(regr.predict([[int(temp), int(humidity), int(wind), 1]])[0])
    return jsonify({"result":  str(pre)})


if __name__ == "__main__":
    app.run(port=8081, debug=True)
