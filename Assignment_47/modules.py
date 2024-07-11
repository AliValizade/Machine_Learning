import numpy as np
from tqdm import tqdm


class Perceptron:
    def __init__(self, input_size, lr_w=0.001, lr_b=0.01, epoch=0, loss_threshold=0.1):
        self.w = np.random.rand(input_size, 1)
        self.b = np.random.rand(1, 1)
        self.lr_w = lr_w
        self.lr_b = lr_b
        self.loss_threshold = loss_threshold
        self.stop_condition = False
        self.Epoch = epoch
        self.losses = []
        self.prev_loss = float('inf')  # Store the previous loss for comparison

    def activation(self, x, function):
        if function == 'sigmoid':
            return 1 / (1 + np.exp(-x))
        elif function == 'relu':
            return np.maximum(0, x)
        elif function == 'tanh':
            return np.tanh(x)
        elif function == 'linear':
            return x
        else:
            raise Exception('Unknown activation function!')

    def fit(self, X_train, Y_train):
        while not self.stop_condition:
            self.Epoch += 1
            epoch_losses = []  # List to store losses for the current epoch
            for x, y in zip(X_train, Y_train):
                x = x.reshape(-1, 1)
                y = y.reshape(-1, 1)
                # Forwarding
                y_pred = x.T @ self.w + self.b
                y_pred = self.activation(y_pred, 'sigmoid')

                # Back propagation
                error = y - y_pred
                self.w += self.lr_w * x * error
                self.b += self.lr_b * error

                loss = np.mean(np.abs(error))
                epoch_losses.append(loss)
            
            mean_loss = np.mean(epoch_losses)
            self.losses.append(mean_loss)
            print(f"Epoch {self.Epoch}, Loss: {mean_loss}")

            # Check stopping condition
            if mean_loss < self.loss_threshold or np.abs(self.prev_loss - mean_loss) < 0.000001:
                self.stop_condition = True

            self.prev_loss = mean_loss

    def predict(self, X_test):
        Y_pred = []
        for x_test in X_test:
            y_pred = x_test @ self.w + self.b
            y_pred = self.activation(y_pred, 'sigmoid')
            Y_pred.append(y_pred)
        return np.array(Y_pred).reshape(-1)
    
    def calculate_loss(self, X_test, Y_test, metric):
        Y_pred = self.predict(X_test)
        error = Y_test - Y_pred
        if metric == 'mae':
            return np.mean(np.abs(error))
        elif metric == 'mse':
            return np.mean(error ** 2)
        elif metric == 'rmse':
            return np.sqrt(np.mean(error ** 2))
        else:
            raise Exception('Unknown metric')
        
    def calculate_accuracy(self, X_test, Y_test):
        Y_pred = self.predict(X_test)
        Y_pred = np.where(Y_pred > 0.5, 1, 0)
        Y_test = Y_test.reshape(-1)
        return np.sum(Y_pred == Y_test) / len(Y_test)

    def evaluate(self, X_test, Y_test):
        loss = self.calculate_loss(X_test, Y_test, 'mse')
        accuracy = self.calculate_accuracy(X_test, Y_test)
        return loss, accuracy
