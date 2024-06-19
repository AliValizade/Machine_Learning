import numpy as np
import matplotlib.pyplot as plt


class LLS:
    def __init__(self):
        self.w = None

    # Train
    def fit(self, X, y):
        X = X.reshape(-1, 1)
        self.w = np.matmul(np.matmul(np.linalg.inv(np.matmul(X.T, X)), X.T), y)

    # Predict
    def predict(self, X):
        X = X.reshape(-1, 1)
        return self.w * X

    # Show Result
    def plot(self, X, y, color, xlabel, ylabel):
        plt.scatter(X, y)
        plt.plot(X, self.predict(X), color=color)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title('Linear Regression')
        plt.show()
