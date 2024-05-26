import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
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


class FindingNemo:
    def __init__(self, train_image):
        self.knn = KNeighborsClassifier(n_neighbors=3)
        X_train, Y_train = self.convert_image_to_dataset(train_image)
        self.knn.fit(X_train, Y_train)
    
    def convert_image_to_dataset(self, image):
        image = cv.resize(image, (0, 0), fx=0.5, fy=0.5)
        image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
        image_hsv_px_list = image_hsv.reshape(-1, 3)

        light_orange = (1, 50, 100)
        dark_orange = (18, 255, 255)
        orange_mask = cv.inRange(image_hsv, light_orange, dark_orange)

        light_white = (0, 0, 100)
        dark_white = (145, 60, 255)
        white_mask = cv.inRange(image_hsv, light_white, dark_white)

        light_black = (0, 0, 0)
        dark_black = (255, 255, 4)
        black_mask = cv.inRange(image_hsv, light_black, dark_black)

        image_mask = orange_mask + white_mask + black_mask

        x_train = image_hsv_px_list / 255
        y_train = image_mask.reshape(-1, ) // 255

        return x_train, y_train

    def remove_background(self, test_image):
        test_image = cv.resize(test_image, (0, 0), fx=0.25, fy=0.25)
        test_image_rgb = cv.cvtColor(test_image, cv.COLOR_BGR2RGB)
        test_image_hsv = cv.cvtColor(test_image, cv.COLOR_BGR2HSV)

        x_test = test_image_hsv.reshape(-1, 3) / 255
        y_pred = self.knn.predict(x_test)

        output = np.array(y_pred).reshape(test_image_rgb.shape[:2])
        output = output.astype('uint8')
        final_result = cv.bitwise_and(test_image_rgb, test_image_rgb, mask=output)

        return final_result


class FindingDory:
    def __init__(self, train_image):
        self.knn = KNeighborsClassifier(n_neighbors=3)
        X_train, Y_train = self.convert_image_to_dataset(train_image)
        self.knn.fit(X_train, Y_train)
    
    def convert_image_to_dataset(self, image):
        image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
        image_hsv_px_list = image_hsv.reshape(-1, 3)
        
        light_blue = (90, 50, 70)
        dark_blue = (110, 255, 255)
        blue_mask = cv.inRange(image_hsv, light_blue, dark_blue)

        light_navy_blue = (110, 50, 50)
        dark_navy_blue = (130, 255, 255)
        navy_blue_mask = cv.inRange(image_hsv, light_navy_blue, dark_navy_blue)

        light_yellow = (20, 150, 150)
        dark_yellow = (30, 255, 255)
        yellow_mask = cv.inRange(image_hsv, light_yellow, dark_yellow)

        image_mask = yellow_mask + blue_mask + navy_blue_mask

        x_train = image_hsv_px_list / 255
        y_train = image_mask.reshape(-1, ) // 255

        return x_train, y_train

    def remove_background(self, test_image):
        test_image_rgb = cv.cvtColor(test_image, cv.COLOR_BGR2RGB)
        test_image_hsv = cv.cvtColor(test_image, cv.COLOR_BGR2HSV)

        x_test = test_image_hsv.reshape(-1, 3) / 255
        y_pred = self.knn.predict(x_test)

        output = np.array(y_pred).reshape(test_image_rgb.shape[:2])
        output = output.astype('uint8')
        final_result = cv.bitwise_and(test_image_rgb, test_image_rgb, mask=output)

        return final_result



if __name__ == '__main__':
   
  train_dory = cv.imread('data/dory.jpg')

  # test_dory = cv.imread('data/abji-dory.jpg')
  test_dory = cv.imread('data/abji-dory.jpg')

  trained_data = FindingDory(train_dory)

  rm_bg_dory = trained_data.remove_background(test_dory)

  plt.imshow(rm_bg_dory)
  plt.show()

  # iris = load_iris()
  # x = iris.data
  # y = iris.target

  # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

  # my_knn = KNN(3)
  # my_knn.fit(x_train, y_train)
  # my_accuracy = my_knn.evaluate(x_test, y_test)
  # print('Accuracy of my_knn: ', my_accuracy)

  # skl_knn = KNeighborsClassifier(3)
  # skl_knn.fit(x_train, y_train)
  # skl_accuracy = skl_knn.score(x_test, y_test)
  # print('Accuracy of skl_knn: ', skl_accuracy)