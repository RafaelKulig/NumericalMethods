from typing import Callable


class Solutions:

    @staticmethod
    def bisection(
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
        if error <= 0 or max_iter <= 0:
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

    @staticmethod
    def fixed_point(
        g: Callable[[float], float], 
        x0: float, 
        error: float, 
        max_iter: int
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
        if error <= 0 or max_iter <= 0:
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

    @staticmethod
    def newton_raphson(
        f: Callable[[float], float],
        df: Callable[[float], float],
        x0: float,
        error: float,
        max_iter: int,
    ):
        """
        Newton-Raphson method to find a root of the function f.
        Args:
            f: The function for which to find the root.
            df: The derivative of the function f.
            x0: The initial guess.
            error: The acceptable error margin.
            max_iter: The maximum number of iterations to perform.
        Returns:
            A tuple containing the root and the number of iterations performed.
        Raises:
            ValueError: If the method fails to converge within the maximum number of iterations.
        """
        if error <= 0 or max_iter <= 0:
            raise ValueError("Error and max_iter must be positive values.")
        i = 0
        x_n = x0
        while i <= max_iter:
            df_xn = df(x_n)
            if df_xn == 0:
                raise ValueError("Derivative is zero. No solution found.")
            x_n1 = x_n - f(x_n) / df_xn
            if abs(x_n1 - x_n) < error:
                return x_n1, i
            x_n = x_n1
            i += 1
        raise ValueError("Method failed after maximum iterations")

    @staticmethod
    def secant(
        f: Callable[[float], float], 
        x0: float, 
        x1: float, 
        error: float, 
        max_iter: int
    ):
        """
        Secant method to find a root of the function f.
        Args:
            f: The function for which to find the root.
            x0: The first initial guess.
            x1: The second initial guess.
            error: The acceptable error margin.
            max_iter: The maximum number of iterations to perform.
        Returns:
            A tuple containing the root and the number of iterations performed.
        Raises:
            ValueError: If the method fails to converge within the maximum number of iterations.
        """
        if error <= 0 or max_iter <= 0:
            raise ValueError("Error and max_iter must be positive values.")
        i = 0
        while i <= max_iter:
            f_x0 = f(x0)
            f_x1 = f(x1)
            if f_x1 - f_x0 == 0:
                raise ValueError("Division by zero. No solution found.")
            x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
            if abs(x2 - x1) < error:
                return x2, i
            x0, x1 = x1, x2
            i += 1
        raise ValueError("Method failed after maximum iterations")

    @staticmethod
    def regula_falsi(
        f: Callable[[float], float], 
        a: float, 
        b: float, 
        error: float, 
        max_iter: int
    ):
        """
        Regula Falsi method to find a root of the function f in the interval [a, b].
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
        if error <= 0 or max_iter <= 0:
            raise ValueError("Error and max_iter must be positive values.")
        if f(a) * f(b) >= 0:
            raise ValueError("f(a) and f(b) must have different signs.")
        F_a = f(a)
        F_b = f(b)
        i = 0
        while i <= max_iter:
            if (F_x := f(x := (a * F_b - b * F_a) / (F_b - F_a))) == 0 or abs(
                F_x
            ) < error:
                return x, i

            if F_a * F_x > 0:
                a, F_a = x, F_x
            else:
                b, F_b = x, F_x
            i += 1
        raise ValueError("Method failed after maximum iterations")

    @staticmethod
    def muller(
        f: Callable[[float], float],
        x0: float,
        x1: float,
        x2: float,
        error: float,
        max_iter: int,
    ):
        """
        Muller method to find a root of the function f.
        Args:
            f: The function for which to find the root.
            x0: The first initial guess.
            x1: The second initial guess.
            x2: The third initial guess.
            error: The acceptable error margin.
            max_iter: The maximum number of iterations to perform.
        Returns:
            A tuple containing the root and the number of iterations performed.
        Raises:
            ValueError: If the method fails to converge within the maximum number of iterations.
        """
        if error <= 0 or max_iter <= 0:
            raise ValueError("Error and max_iter must be positive values.")
        i = 0
        while i <= max_iter:
            f_x0 = f(x0)
            f_x1 = f(x1)
            f_x2 = f(x2)

            h0 = x1 - x0
            h1 = x2 - x1
            if h0 == 0 or h1 == 0:
                raise ValueError("Division by zero. No solution found.")
            delta0 = (f_x1 - f_x0) / h0
            delta1 = (f_x2 - f_x1) / h1
            a = (delta1 - delta0) / (h1 + h0)
            b = a * h1 + delta1
            c = f_x2

            discriminant = b**2 - 4 * a * c
            if discriminant < 0:
                raise ValueError("Complex root encountered. No solution found.")
            sqrt_discriminant = discriminant**0.5

            if abs(b + sqrt_discriminant) > abs(b - sqrt_discriminant):
                denominator = b + sqrt_discriminant
            else:
                denominator = b - sqrt_discriminant
            if denominator == 0:
                raise ValueError("Division by zero. No solution found.")
            x3 = x2 - (2 * c) / denominator

            if abs(x3 - x2) < error:
                return x3, i

            x0, x1, x2 = x1, x2, x3
            i += 1
        raise ValueError("Method failed after maximum iterations")
