import numpy as np
import matplotlib.pyplot as plt


class LLS:
    def __init__(self):
        self.w = None

    # Train
    def fit(self, X, Y):
        X = X.reshape(-1, 1)
        self.w = np.matmul(np.matmul(np.linalg.inv(np.matmul(X.T, X)), X.T), Y)

    # Predict
    def predict(self, X):
        X = X.reshape(-1, 1)
        return self.w * X

    # Show Result
    def plot(self, X, y):
        plt.scatter(X, y)
        plt.plot(X, self.predict(X), color='red')
        plt.xlabel('Length')
        plt.ylabel('Height')
        plt.title('Linear Regression')
        plt.show()