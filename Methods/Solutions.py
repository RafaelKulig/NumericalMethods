from typing import Callable


class Solutions(object):
    def __init__(self):
        pass

    def bisection(
        self,
        f: Callable[[float], float],
        a: float,
        b: float,
        error: float,
        max_iter: int,
    ):
        """
        Bisection method to find a root of the function f in the interval [a, b].
        Args:
            f: The function for which to find the root.
            a: The start of the interval.
            b: The end of the interval.
            error: The acceptable error margin.
            max_iter: The maximum number of iterations to perform.
        Returns:
            A tuple containing the root and the number of iterations performed.
        Raises:
            ValueError: If the method fails to converge within the maximum number of iterations.
        """
        if (error or max_iter) <= 0:
            raise ValueError("Error and max_iter must be positive values.")
        if f(a) * f(b) >= 0:
            raise ValueError("f(a) and f(b) must have different signs.")
        F_a = f(a)
        i = 0
        while i <= max_iter:
            if (F_x := f(x := (a + b) / 2)) == 0 or (b - a) / 2 < error:
                return x, i

            if F_a * F_x > 0:
                a, F_a = x, F_x
            else:
                b = x
            i += 1
        raise ValueError("Method failed after maximum iterations")

    def fixed_point(
        self, g: Callable[[float], float], x0: float, error: float, max_iter: int
    ):
        """
        Fixed Point Iteration method to find a fixed point of the function g.
        Args:
            g: The function for which to find the fixed point.
            x0: The initial guess.
            error: The acceptable error margin.
            max_iter: The maximum number of iterations to perform.
        Returns:
            A tuple containing the fixed point and the number of iterations performed.
        Raises:
            ValueError: If the method fails to converge within the maximum number of iterations.
        """
        if (error or max_iter) <= 0:
            raise ValueError("Error and max_iter must be positive values.")
        i = 0
        x_n = x0
        while i <= max_iter:
            x_n1 = g(x_n)
            if abs(x_n1 - x_n) < error:
                return x_n1, i
            x_n = x_n1
            i += 1
        raise ValueError("Method failed after maximum iterations")
