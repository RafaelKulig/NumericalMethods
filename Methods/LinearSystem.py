class LinearSystem:
    """
    A class to solve a system of linear equations using Gaussian elimination.
    Attributes:
        coefficients (list): A list of lists representing the coefficient matrix.
        constants (list): A list representing the constant terms of the equations.

    Methods:
        gauss_elimination(): Solves the system of equations using Gaussian elimination.
    """
    def __init__(self, coefficients: list, constants: list):
        self.coefficients = [row[:] for row in coefficients]  # Deep copy to avoid modifying the original matrix
        self.constants = constants[:]
        if len(coefficients) != len(constants):
            raise ValueError("The number of equations must match the number of constants.")
        if any(len(row) != len(coefficients) for row in coefficients):
            raise ValueError("All rows in the coefficient matrix must have the same length.")
        if not all(isinstance(c, (int, float)) for c in constants):
            raise ValueError("All constants must be numeric values.")
        if not all(isinstance(row, list) for row in coefficients):
            raise ValueError("Coefficients must be provided as a list of lists.")
        

    def gauss_elimination(self):
        """ 
        Solves the system of linear equations using Gaussian elimination.
        Returns:
            list: A list containing the solution to the system of equations.
        Raises:
            ValueError: If the matrix is singular or nearly singular, or if the input is invalid.
        """

        n = len(self.constants)
        solution = [0] * n  # Initialize the solution vector with zeros

        # Transform the matrix to upper triangular form
        for k in range(n): # Iterate over each column
            pivot=self.coefficients[k][k] # Get the pivot element
            if pivot == 0:
                raise ValueError("Matrix is singular or nearly singular.")
            for i in range(k + 1, n): # Iterate over each row below the current row
                factor = self.coefficients[i][k] / pivot # Calculate the factor to eliminate the variable
                self.constants[i] -= factor * self.constants[k] # Adjust the constant term accordingly
                for j in range(k, n): # Iterate over each column to the right of the current column
                    self.coefficients[i][j] -= factor * self.coefficients[k][j] # Eliminate the variable in the current row
        
        # Back substitution to find the solution
        for i in range(n - 1, -1, -1): # Back substitution
            s=sum(self.coefficients[i][j] * solution[j] for j in range(i + 1, n)) # Calculate the sum of known variables
            solution[i] = (self.constants[i] - s) / self.coefficients[i][i] # Solve for the current variable
        return solution
    
test_linear_system = LinearSystem(
    coefficients=[[2, 1, -1], [1, -1, 2], [1, 2, 3]],
    constants=[8, 3, 7]
)

try:
    solution = test_linear_system.gauss_elimination()
    print("Solution:", solution)
except ValueError as e:
    print("Error:", e)