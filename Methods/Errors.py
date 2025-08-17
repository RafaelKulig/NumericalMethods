class Errors:
    """
    A class to calculate different types of errors between true values and approximate values.
    """
    @staticmethod
    def absolute_error(true_value, approx_value):
        """
        Calculate the absolute error between the true value and the approximate value.

        :param true_value: The true value.
        :param approx_value: The approximate value.
        :return: The absolute error.
        """
        return abs(true_value - approx_value)

    @staticmethod
    def relative_error(true_value, approx_value):
        """
        Calculate the relative error between the true value and the approximate value.

        :param true_value: The true value.
        :param approx_value: The approximate value.
        :return: The relative error.
        """
        if true_value == 0:
            raise ValueError("True value cannot be zero for relative error calculation.")
        return abs((true_value - approx_value) / true_value)

    @staticmethod
    def percentage_error(true_value, approx_value):
        """
        Calculate the percentage error between the true value and the approximate value.

        :param true_value: The true value.
        :param approx_value: The approximate value.
        :return: The percentage error.
        """
        if true_value == 0:
            raise ValueError("True value cannot be zero for percentage error calculation.")
        return abs((true_value - approx_value) / true_value) * 100