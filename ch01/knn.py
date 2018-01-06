import numpy as np
from collections import Counter
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

class Knn(object):

  def train(self, X, y):
    self.X_train = X
    self.y_train = y
  
  def predict(self, X, k=1):
    dists = self.compute_distances(X)
    return self.predict_labels(dists, k=k)

  def compute_distances(self, X):
    num_test = X.shape[0]
    num_train = self.X_train.shape[0]
    dists = np.zeros((num_test, num_train)) 
    X_train_2 = self.X_train*self.X_train
    X_train_2 = np.sum(X_train_2, axis = 1)    
    X_train_2_repeat = np.array([X_train_2]*X.shape[0])
    
    X_2 = X*X
    X_2 = np.sum(X_2, axis = 1)
    X_2_repeat = np.array( [X_2]*self.X_train.shape[0]).transpose()
    X_dot_X_train = X.dot(self.X_train.T)
    
    dists = X_train_2_repeat + X_2_repeat - 2*X_dot_X_train
    dists = np.sqrt(dists)
    return dists

  def predict_labels(self, dists, k=1):
    num_test = dists.shape[0]
    y_pred = np.zeros(num_test)
    for i in range(num_test):
      dists_i = dists[i]
      closest_y = self.y_train[dists_i.argsort()[:k]]
      y_pred[i] = Counter(closest_y).most_common(1)[0][0]
    return y_pred

if __name__ == '__main__':
  iris_dataset = load_iris()
  X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)
  num_test = len(y_test)

  knn = Knn()
  knn.train(X_train, y_train)
  dists = knn.compute_distances(X_test)
  y_test_pred = knn.predict_labels(dists, k=3)

  num_correct = np.sum(y_test_pred == y_test)
  accuracy = float(num_correct) / num_test
  print('Got %d / %d correct => accuracy: %f' % (num_correct, num_test, accuracy))



