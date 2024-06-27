#!/usr/bin/python3

if __name__ != '__main__':

    def pascal_triangle(n):
        """
        Generate Pascal's Triangle up to the nth row.

        Parameters:
        n (int): The number of rows to generate.

        Returns:
        list: A list of lists representing Pascal's Triangle up to the nth row.

        Raises:
        ValueError: If n is less than or equal to 0.

        Note:
        The first row is represented as [1].
        Each subsequent row  is generated by summing the adjacent elements in the previous row.
        """
        if n <= 0:
            raise ValueError("n must be greater than or equal to 1")

        triangle = [[1] * i for i in range(1, n+1)]

        for i in range(2, n):
            for j in range(1, i):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

        return triangle


else:
    print("Usage: This module must be imported to work")
