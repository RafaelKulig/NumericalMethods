from typing import List,Tuple
class Interpolation:
    
    def __init__(self, x_values: List[float], y_values: List[float]):
        if len(x_values) != len(y_values):
            raise ValueError("x_values and y_values must have the same length.")    # Ensure both lists have the same length
        if len(set(x_values)) != len(x_values): # Check for distinct x_values
            raise ValueError("x_values must be distinct for interpolation.")
        self.x_values = x_values
        self.y_values = y_values
        self.n = len(x_values)

    def lagrange(self, x: float) -> float:

        """
        Compute the Lagrange interpolation polynomial at a given point x.
        Args:
            x: The point at which to evaluate the interpolation polynomial.
        Returns:
            The value of the interpolation polynomial at x.
        Raises:
            ValueError: If the x_values are not distinct.
        """
        result = 0.0
        for i in range(self.n):
            term = self.y_values[i]
            for j in range(self.n):
                if j != i:
                    term *= (x - self.x_values[j]) / (self.x_values[i] - self.x_values[j])
            result += term
        return result
    
    def _divided_differences(self) -> list:
        """Compute the divided differences table."""
        n = self.n
        coef = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            coef[i][0] = self.y_values[i]
        for j in range(1, n):
            for i in range(n - j):
                coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (self.x_values[i + j] - self.x_values[i]) 
        return coef

    def newton(self, x: float) -> float:
        """
        Compute the Newton interpolation polynomial at a given point x.
        Args:
            x: The point at which to evaluate the interpolation polynomial.
        Returns:
            The value of the interpolation polynomial at x.
        Raises:
            ValueError: If the x_values are not distinct.
        """ 
        coef = self._divided_differences()
        result = coef[0][0]
        term = 1.0
        for i in range(1, self.n):
            term *= (x - self.x_values[i - 1])
            result += coef[0][i] * term
        return result

    def linear_spline(self, x: float) -> float:
        """
        Compute the linear spline interpolation at a given point x.
        Args:
            x: The point at which to evaluate the linear spline.
        Returns:
            The value of the linear spline at x.
        Raises:
            ValueError: If x is outside the range of x_values.
        """
        if x < self.x_values[0] or x > self.x_values[-1]:
            raise ValueError("x is outside the range of x_values.")
        for i in range(self.n - 1):
            if self.x_values[i] <= x <= self.x_values[i + 1]:
                # Linear interpolation formula
                return self.y_values[i] + (self.y_values[i + 1] - self.y_values[i]) * (x - self.x_values[i]) / (self.x_values[i + 1] - self.x_values[i])
        raise ValueError("x is outside the range of x_values.")

    def cubic_spline(self, x: float) -> float:
        """
        Compute the cubic spline interpolation at a given point x.
        Args:
            x: The point at which to evaluate the cubic spline.
        Returns:
            The value of the cubic spline at x.
        Raises:
            ValueError: If x is outside the range of x_values.
        """
        if x < self.x_values[0] or x > self.x_values[-1]:
            raise ValueError("x is outside the range of x_values.")
        n = self.n
        h = [self.x_values[i + 1] - self.x_values[i] for i in range(n - 1)]
        alpha = [0] * (n - 1)
        for i in range(1, n - 1):
            alpha[i] = (3 / h[i]) * (self.y_values[i + 1] - self.y_values[i]) - (3 / h[i - 1]) * (self.y_values[i] - self.y_values[i - 1])
        l = [1] + [0] * (n - 1)
        mu = [0] * (n - 1)
        z = [0] * n
        for i in range(1, n - 1):
            l[i] = 2 * (self.x_values[i + 1] - self.x_values[i - 1]) - h[i - 1] * mu[i - 1]
            mu[i] = h[i] / l[i]
            z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]
        l[n - 1] = 1
        z[n - 1] = 0
        c = [0] * n
        b = [0] * (n - 1)
        d = [0] * (n - 1)
        for j in range(n - 2, -1, -1):
            c[j] = z[j] - mu[j] * c[j + 1]
            b[j] = (self.y_values[j + 1] - self.y_values[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
            d[j] = (c[j + 1] - c[j]) / (3 * h[j])
        for i in range(n - 1):
            if self.x_values[i] <= x <= self.x_values[i + 1]:
                dx = x - self.x_values[i]
                return self.y_values[i] + b[i] * dx + c[i] * dx**2 + d[i] * dx**3
        raise ValueError("x is outside the range of x_values.")
    