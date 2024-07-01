import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt


class LLS:
    def __init__(self):
        self.w = None

    # Train
    def fit(self, X, y):
        self.w = inv(X.T @ X) @ X.T @ y

    # Predict
    def predict(self, X):
        return X @ self.w
    
    # Evaluate
    def evaluate(self, X_test, Y_test, metric):
        Y_pred  =self.predict(X_test)
        error = Y_test - Y_pred

        if metric == 'mae':
            loss = np.sum(np.abs(error)) / len(Y_test)
        elif metric == 'mse':
            loss = np.sum(error ** 2) / len(Y_test)
        elif metric == 'rmse':
            loss = np.sqrt(np.mean(error ** 2))

        return loss

    # Show Result
    def plot(self, X_train, X_test, Y_train, Y_test, color_train, color_test, xlabel, ylabel):
        plt.scatter(X_train, Y_train, c=color_train, marker='.', label='Training data', alpha=0.5)
        plt.scatter(X_test, Y_test, c=color_test, marker='.', label='Testing data', alpha=0.5)
        plt.plot(X_test, self.predict(X_test), color='green', label='Prediction')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title('Linear Regression')
        plt.legend()
        plt.show()



class LLS_3D:
    def __init__(self):
        self.w = None

    # Train
    def fit(self, X, y):
        X_b = np.hstack([np.ones((X.shape[0], 1)), X])    # Add bias column
        self.w = inv(X_b.T @ X_b) @ X_b.T @ y

    # Predict
    def predict(self, X):
        X_b = np.hstack([np.ones((X.shape[0], 1)), X])    # Add bias column
        return X_b @ self.w
    