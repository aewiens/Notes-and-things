import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


class OLS:
    """ 
    Ordinary Least Squares Linear Regression
    """

    def __init__(self):
        pass


    def augment_x(self, x):
        return np.hstack((np.ones_like(x), x))


    def fit(self, X, y):
        X = self.augment_x(X)
        self.beta = np.linalg.inv(X.T @ X) @ X.T @ y
        return self


    def predict(self, x):
        X = self.augment_x(x)
        return X @ self.beta
        


if __name__ == '__main__':
   
    # Input column vectors to OLS class
    x = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]).T
    y = np.array([[1, 3, 2, 5, 7, 8, 8, 9, 10, 12]]).T

    # Train a linear regression with my OLS class
    myLR = OLS().fit(x, y)

    # Predict at inputs
    yhat = myLR.predict(x)

    # Test against scikit-learn
    lr = LinearRegression().fit(x, y)
    assert np.allclose(yhat, lr.predict(x))

    # Plot observations and LR prediction
    grid = np.linspace(0, 10)
    plt.scatter(x, y)
    plt.plot(x, yhat)
    #plt.show()
