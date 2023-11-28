from sklearn.model_selection import train_test_split
from sklearn import metrics

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
from db import *
'''
def pr(num):

    # Assuming you have a DataFrame 'df' with 'Date' and 'Close' columns
    # 'Date' is the date of the stock price, and 'Close' is the closing price of the stock
    df = get(num)
    print(df)
    # Convert 'Date' to datetime
    df[4] = pd.to_datetime(df[4])

    # Use 'Date' to predict 'Close'
    X = df[4].map(df.datetime.toordinal).values.reshape(-1, 1)
    y = df['Close']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Train the algorithm
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # Make predictions using the testing set
    y_pred = regressor.predict(X_test)
    print(y_pred)
pr(4)
'''

def pr(num):
    d=gets(num)

    stock_records = [
    ]
    for i in d:
        stock_records.append(list(i))
    # Create a DataFrame from the stock records
    columns = ['Name', 'StockID', 'Price', 'Quantity']
    df = pd.DataFrame(stock_records, columns=columns)

    # Feature engineering: Create a new feature 'TotalValue' by multiplying 'Price' and 'Quantity'
    df['TotalValue'] = df['Price'] * df['Quantity']

    # Use 'TotalValue' as the feature for prediction
    X = df[['TotalValue']]
    y = df['Price']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = regressor.predict(X_test)

    # Evaluate the model
    mse = metrics.mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

    # Visualize the predictions
    plt.scatter(X_test, y_test, color='black')
    plt.plot(X_test, y_pred, color='blue', linewidth=3)
    plt.title('Stock Price Prediction')
    plt.xlabel('Total Value')
    plt.ylabel('Price')
    plt.show()

def plot(num):
    r = get(num)

    # Assuming you have a DataFrame 'df' with 'StockName', 'Price', and 'Quantity'
    df = pd.DataFrame({
        'StockName': r[1],
        'Price': r[2],
        'Quantity': r[3]
    }, index=[i for i in range(len(r))])  # Use 'StockName' as the index
    fig, ax1 = plt.subplots()

    # Plot price
    color = 'tab:red'
    ax1.set_xlabel('StockName')
    ax1.set_ylabel('Price', color=color)
    ax1.plot(df.index, df['Price'], color=color)  # Use df.index here
    ax1.tick_params(axis='y', labelcolor=color)

    # Create a second y-axis for quantity
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Quantity', color=color)
    ax2.plot(df.index, df['Quantity'], color=color)  # Use df.index here
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.show()