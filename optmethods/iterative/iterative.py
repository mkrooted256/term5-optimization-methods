import numpy as np
from ..optimizer import Optimizer

class OneDimIterative(Optimizer):
    def __init__(self, bounds, n):
        """
        Build 1D Iterative Optimizer obejct

        Parameters
        ----------
        bounds : array_like
            2-item array to define 1D function domain
        n : int
            sampling number - domain is sampled in n points

        """
        super().__init__()
        self.bounds = bounds
        self.n = n

    def optimize(self, f):
        X = np.linspace(self.bounds[0], self.bounds[1], self.n)
        Y = f(X)
        xmin = np.argmin(Y)
        return (xmin, Y[xmin])