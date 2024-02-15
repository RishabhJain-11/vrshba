import numpy as np

def euclidean_distance(x1, x2):
    np.sqrt(np.sum(x1 - x2) ** 2)

class KNN:
    def __init__(self, k=3):
        self.k = k
    
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
        
    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return predictions
        
    def _predict(self, x):
        #Compute the distance
        
        #Get the Closest k
        
        #majority
    