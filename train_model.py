import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import os

os.makedirs("model", exist_ok=True)

data = yf.download("AAPL", start="2023-01-01", end="2024-12-31")  

data = data[["Open", "High", "Low", "Close", "Volume"]]
data.dropna(inplace=True)

data["Target"] = data["Close"].shift(-1)
data.dropna(inplace=True)

X = data.drop("Target", axis=1)
y = data["Target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "model/stock_model.pkl")
print(" Le modèle entraîné et sauvegardé.")
