import numpy as np

class KNN:
  def __init__(self, k):
    self.k = k

  # Training
  def fit(self, X, Y):
    self.X_train = X
    self.Y_train = Y

  def euqlidian_distance(self, x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

  def predict(self, inputs):
    outputs = []
    for item in inputs:
      distances = []
      for x_train in self.X_train:
        d = self.euqlidian_distance(item, x_train)
        distances.append(d)

      nearest_neighbors = np.argsort(distances)[0:self.k]
      result = np.bincount(self.Y_train[nearest_neighbors])
      outputs.append(np.argmax(result))

    return outputs