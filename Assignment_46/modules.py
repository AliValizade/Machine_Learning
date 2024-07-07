import numpy as np

class Perceptron:
    def __init__(self, input_size, lr_w=0.001, lr_b=0.01, epoch=0, loss_threshold=0.3):
        self.w = np.random.rand(input_size, 1)
        self.b = np.random.rand(1, 1)
        self.lr_w = lr_w
        self.lr_b = lr_b
        self.loss_threshold = loss_threshold
        self.stop_condition = False
        self.Epoch = epoch
        self.losses = []

    def fit(self, X_train, Y_train):
        while self.stop_condition == False:
            self.Epoch += 1
            epoch_losses = []  # List to store losses for the current epoch
            for i in range(X_train.shape[0]):
                x = X_train[i]
                y = Y_train[i]

                y_pred = x @ self.w + self.b
                error = y - y_pred

                self.w += self.lr_w * error * x
                self.b += self.lr_b * error

                loss = np.mean(np.abs(error))
                epoch_losses.append(loss)
            
            mean_loss = np.mean(epoch_losses)
            self.losses.append(mean_loss)
            print(f"Epoch {self.Epoch + 1}, Loss: {mean_loss}")

            # Check stopping condition
            if mean_loss < self.loss_threshold:
                self.stop_condition = True

    def predict(self, X_test):
        return np.dot(X_test, self.w) + self.b

    def evaluate(self, X_test, Y_test):
        Y_pred = self.predict(X_test)
        loss = np.mean(np.abs(Y_test - Y_pred))
        return loss
