import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge


class RidgeRegression:
    """ 
    Ridge Regression
    """

    def __init__(self, alpha=1.0):

        self.alpha = alpha


    def augment(self, x):

        return np.hstack((np.ones_like(x), x))


    def fit(self, x, y):

        X = self.augment(x)

        # Regularization matrix
        aI = np.diag([self.alpha] * len(X.T))

        # Don't regularize the intercept
        aI[0][0] = 0

        self.beta = np.linalg.inv(X.T @ X + aI) @ X.T @ y

        return self


    def predict(self, x):

        X = self.augment(x)

        return X @ self.beta


    def score(self, x, y):

        n = len(x)

        x_, y_ = x.mean(), y.mean()

        SS = np.var(x) ** 0.5 * np.var(y) ** 0.5

        R = sum(((x[i, 0] - x_) * (y[i, 0] - y_) for i in range(n))) / n / SS
        
        return R**2
        

if __name__ == '__main__':
   
    # Input column vectors to OLS class
    x = np.arange(10).reshape(-1, 1)
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12]).reshape(-1, 1)

    # Train a linear regression with my OLS class
    myRidge = RidgeRegression(alpha=0.1).fit(x, y)

    # Predict at inputs
    yhat = myRidge.predict(x)

    # Test against scikit-learn
    ridge = Ridge(alpha=0.1).fit(x, y)
    assert np.allclose(yhat, ridge.predict(x))

    # Score
    score = myRidge.score(x, y)
    print("Ridge Regression R^2 value: {:>2.3f}".format(score))

    # Plot observations and LR prediction
    grid = np.linspace(0, 10)
    plt.scatter(x, y)
    plt.plot(x, yhat)
    plt.show()
