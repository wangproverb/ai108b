from keras.datasets import boston_housing
(X_train, y_train), (X_test, y_test) = boston_housing.load_data()
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)