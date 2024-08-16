import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Select box for operation
operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

# Function to perform calculations
def calculate(num1, num2, operation):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

# Button to perform calculation
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.write(f"The result is: {result}")
