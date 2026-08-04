def print_pyramid(rows):
    for i in range(1, rows + 1):
        # Print leading spaces
        print(" " * (rows - i), end="")
        # Print asterisks with a space in between
        print("* " * i)

# Change this number to alter the height of the pyramid
pyramid_height = 5
print_pyramid(pyramid_height)
