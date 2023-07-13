## Read input as specified in the question
## Print the required output in given format
def generate_pattern(rows):
    start_char = ord('A')  # Starting character ('A')

    for i in range(rows):
        row = ""
        current_char = start_char + i

        for j in range(i + 1):
            row += chr(current_char)
            current_char += 1

        print(row)

# Get the number of rows from the user
num_rows = int(input())

# Generate the pattern
generate_pattern(num_rows)
