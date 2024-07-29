#!/usr/bin/python3

def matrix_divided(matrix, div):
    '''
    Matrix divider
    '''
    if not type(matrix[0]) is not list:
        raise TypeError()
    
    row_l = len(matrix[0])
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    
    result_matrix = []
    
    for row in matrix:
        if not isinstance(row, list) or len(row) != row_size:
            raise TypeError('Each row of the matrix must have the same size')
        
        new_row = []
        
        for value in row:
            if not isinstance(value, (float, int)):
                raise TypeError('matrix must be a matrix (array of arrays of integers/floats)')
            
            quotient = round(value / div, 2)
            new_row.append(quotient)
        
        result_matrix.append(new_row)
    
    return result_matrix

