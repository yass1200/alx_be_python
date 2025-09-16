# pattern_drawing.py

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop to control rows
while row < size:
    # For loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    # After finishing a row, move to the next line
    print()
    row += 1
