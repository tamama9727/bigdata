import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

lifesat = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
# print(lifesat.tail(5))
# print(lifesat.shape)
# print(lifesat.describe())
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values
# print(X)
# print(y)

lifesat.plot(kind='scatter', grid=True,  x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_500, 62_500, 5, 8])
plt.show()

model = LinearRegression()

model.fit(X, y)

X_new = [[31700]]
print(lifesat)
print(model.predict(X_new))