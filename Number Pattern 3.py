## Read input as specified in the question.
## Print output as specified in the question.
def generate_pattern(rows):
    for i in range(1, rows + 1):
        row = ""
        
        for j in range(1, i + 1):
            if j == 1 or j == i:
                row += str(1)
            else:
                row += str(2)
        
        print(row)

# Get the number of rows from the user
num_rows = int(input())

# Generate the pattern
generate_pattern(num_rows)
