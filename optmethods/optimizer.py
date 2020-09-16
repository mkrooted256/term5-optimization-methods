from abc import ABC, abstractmethod


class Optimizer(ABC):

    def __init__(self):
        super().__init__()
        self._history = []

    @abstractmethod
    def optimize(self, f):
        """
        Find extreme points and values of f

        Arguments
        ---------
            f : R^n -> R
                function to optimize

        Example
        -------
            def f(x):
                return x**2 + 4
            optimizer = SomeOptimizer(parameters ...)
            (xmin, ymin) = optimizer.optimize(f)
        """
        pass

    def get_history(self):
        return self._history

    def reset_history(self):
        self._history = []