import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


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

  def evaluate(self, X, Y):
    Y_pred = self.predict(X)
    accuracy = np.sum(Y_pred == Y) / len(Y)
    return accuracy



if __name__ == '__main__':
  iris = load_iris()
  x = iris.data
  y = iris.target

  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

  my_knn = KNN(3)
  my_knn.fit(x_train, y_train)
  my_accuracy = my_knn.evaluate(x_test, y_test)
  print('Accuracy of my_knn: ', my_accuracy)

  skl_knn = KNeighborsClassifier(3)
  skl_knn.fit(x_train, y_train)
  skl_accuracy = skl_knn.score(x_test, y_test)
  print('Accuracy of skl_knn: ', skl_accuracy)