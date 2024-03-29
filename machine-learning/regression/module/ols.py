import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


class OLS:
    """ 
    Ordinary Least Squares Linear Regression
    """

    def __init__(self):
        pass


    def augment(self, x):

        return np.hstack((np.ones_like(x), x))


    def fit(self, x, y):

        X = self.augment(x)

        self.beta = np.linalg.inv(X.T @ X) @ X.T @ y

        return self


    def predict(self, x):

        X = self.augment(x)

        return X @ self.beta


    def score(self, x, y):

        n = len(x)

        #x, y = np.ravel(x), np.ravel(y)

        x_, y_ = x.mean(), y.mean()

        SS = np.var(x) ** 0.5 * np.var(y) ** 0.5

        R = sum(((x[i, 0] - x_) * (y[i, 0] - y_) for i in range(n))) / n / SS
        
        return R**2
        


if __name__ == '__main__':
   
    # Input column vectors to OLS class
    x = np.arange(10).reshape(-1, 1)
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12]).reshape(-1, 1)

    # Train a linear regression with my OLS class
    myLR = OLS().fit(x, y)

    # Predict at inputs
    yhat = myLR.predict(x)

    # Test against scikit-learn
    lr = LinearRegression().fit(x, y)
    assert np.allclose(yhat, lr.predict(x))

    # Score
    score = myLR.score(x, y)
    print("OLS R^2 value: {:>2.3f}".format(score))

    # Plot observations and LR prediction
    grid = np.linspace(0, 10)
    plt.scatter(x, y)
    plt.plot(x, yhat)
    plt.show()
