# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):

    max1 = max(numbers)

    remaining = [n for n in numbers if n != max1]

    max2 = max(remaining) if remaining else None

    return (max1, max2)

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    return sorted(set(numbers))

# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = []
    total = 0

    for num in arr:
        total += num
        result.append(total)

    return result
# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    return lst[::step]

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    return sum(a * b for a, b in zip(list1, list2))

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    row_m1 = len(matrix1)
    col_m1 = len(matrix1[0])
    row_m2 = len(matrix2)
    col_m2 = len(matrix2[0])

    result = [[0 for _ in range(col_m2)] for _ in range(row_m1)]

    for i in range(row_m1):
        for j in range(col_m2):
            for k in range(col_m1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result