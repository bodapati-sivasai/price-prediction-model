import pandas as pd
from sklearn.linear_model import LinearRegression
# Load the data
f = "iphone.csv"
d = pd.read_csv(f)
# Create and fit the model
model = LinearRegression()
model.fit(d[['version']], d['price'])
print("Enter phone version:")
n=int(input())
# Create a DataFrame for prediction to match the feature names
version_to_predict = pd.DataFrame([[n]], columns=['version'])
prediction = model.predict(version_to_predict)

print("the predited value is :",prediction)
