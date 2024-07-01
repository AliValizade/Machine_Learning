import numpy as np
from sklearn.model_selection import train_test_split


def my_train_test_split(X, y, test_size=0.2, random_state=None):
    num_of_samples = X.shape[0]
    
    # Shuffle the data
    indexes = np.arange(num_of_samples)
    np.random.shuffle(indexes)
    
    # Calculate the size of the test data
    num_of_test = int(num_of_samples * test_size)
    
    # Split indices for train and test
    test_indices = indexes[:num_of_test]
    train_indices = indexes[num_of_test:]
    
    # Split the data
    X_train, X_test = X[train_indices], X[test_indices]
    y_train, y_test = y[train_indices], y[test_indices]
    
    return X_train, X_test, y_train, y_test

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = np.array([1, 2, 3, 4, 5])

# Test my function
X_train, X_test, y_train, y_test = my_train_test_split(X, y, test_size=0.4, random_state=42)

# # Test Sklearn function
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)


print(f"✅ X_train:\n{X_train}")
print('============')
print(f"✅ X_test:\n{X_test}")
print('============')
print(f"✅ y_train:\n{y_train}")
print('============')
print(f"✅ y_test:\n{y_test}")
