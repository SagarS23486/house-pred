import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
data = pd.read_csv("Housing.csv")

# show first rows
print(data.head())
# select features
X = data[['area', 'bedrooms', 'bathrooms', 'stories', 'parking']]

# target variable
y = data['price']

print(X.head())
print(y.head())

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)
# 1️⃣ Correlation Heatmap
corr = data.corr(numeric_only=True)

plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# 2️⃣ Area vs Price Scatter Plot
plt.scatter(data['area'], data['price'])
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area vs Price")
plt.show()



# 3️⃣ Bedrooms vs Price Graph
sns.barplot(x='bedrooms', y='price', data=data)
plt.title("Bedrooms vs Price")
plt.show()
# create model
model = LinearRegression()

# train model
model.fit(X_train, y_train)

print("Model trained successfully")
# predict prices
predictions = model.predict(X_test)

print(predictions[:5])
comparison = pd.DataFrame({
    'Actual Price': y_test,
    'Predicted Price': predictions
})

print(comparison.head())
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)