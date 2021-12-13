"""
Student: May Lindenberg
ID: 203132949
Assignment no. 3
Program: matrix.py
"""

def matrix_scalar_mult(matrix, scalar):
    multm = [[matrix[j][i]*scalar for i in range(len(matrix[0]))] for j in range(len(matrix))]
    return multm

def matrix_add(matrix_a, matrix_b):
    matrixab = [[matrix_a[j][i]+matrix_b[j][i] for i in range(len(matrix_a))] for j in range(len(matrix_a))]
    return matrixab

def matrix_mult(matrix_a, matrix_b):
    matrixab = [[sum(a*b for a, b in zip(a_row, b_col)) for b_col in zip(*matrix_b)] for a_row in matrix_a]
    return matrixab

def identy_matrix(n):
    matrix_i = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
    return matrix_i

def matrix_polynom(matrix_a, p):
    ls = []
    im =identy_matrix(len(p))
    mm = matrix_mult(matrix_a, matrix_a)
    for i in range(len(p)):
        if i < 1:
            ls = (matrix_scalar_mult(im, p[i]))
        elif i == 1:
            ls = matrix_add(matrix_scalar_mult(matrix_a, p[i]), ls)
        else:
            ls = matrix_add(matrix_scalar_mult(mm, p[i]), ls)
            mm = matrix_mult(matrix_a, mm)
    return ls

def string_to_list(str):
    """this func turn a str of numbers to a list of floats"""
    ls = str.split(" ")
    numlist = [float(i) for i in ls if (i != "" and i != " ")]
    return numlist

def matrix_input(filepath):
    """this func reads a file and return the metrix and polynom multiplication"""
    file_input = open(filepath, "r")
    ls = []
    for i in file_input.readlines():
        if i == "\n":
            continue
        i = i.strip().split()
        for j in range(len(i)):
            i[j] = float(i[j])
        ls.append(i)
    matrix = ls[:-1]
    poly = ls[-1]
    return matrix_polynom(matrix, poly)

def matrix_out(matrix):
    """this func acceps a metrix and writes it in a matrix_out.txt"""
    file_out = open("matrix_out.txt", "w")
    str = ""
    for i in range(len(matrix)):
        for j in matrix[i]:
            str += f'{j:13.2f}'
        str += "\n"
    file_out.write(str)
    file_out.close()
    
def main():
    x = matrix_input("matrix_input.txt")
    matrix_out(x)
main()
