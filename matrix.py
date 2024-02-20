import numpy as np
import streamlit as st

st.title('MATRIX OPERATION')
def matrix_input(matrix_num):
    st.header("",divider='rainbow')

# Define two matrices
#matrix_A = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])

#matrix_B = np.array([[9, 8, 7],[6, 5, 4],[3, 2, 1]])
    rows = st.number_input("enter the no of rows")
    cols = st.number_input("enter the no of columns")
    matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                element = st.number_input(f"Enter element at position ({i + 1}, {j + 1}):", key=f"matrix-{matrix_num}-{i}-{j}")
                row.append(element)
            matrix.append(row)

        return np.array(matrix)

def main():
    st.title("Matrix Input App")

    matrix_A = matrix_input(1)
    matrix_B= matrix_input(2)

    st.text("Entered Matrix B:")
    st.write(matrix1)

    st.text("Entered Matrix B:")
    st.write(matrix2)

if _name_ == "_main_":
    main()
# Matrix multiplication
matrix_multiply = np.dot(matrix_A, matrix_B)

# Matrix division (pseudo-inverse)
matrix_divide = np.linalg.pinv(matrix_B)

# Matrix addition
matrix_add = matrix_A + matrix_B

# Matrix subtraction
matrix_subtract = matrix_A - matrix_B

# Display results
st.write("Matrix A:\n", matrix_A)
st.write("Matrix B:\n", matrix_B)
st.write("Matrix Multiplication (A * B):\n", matrix_multiply)
st.write("Matrix Division (pseudo-inverse of B):\n", matrix_divide)
st.write("Matrix Addition (A + B):\n", matrix_add)
st.write("Matrix Subtraction (A - B):\n", matrix_subtract)

