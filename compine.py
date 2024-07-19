# Define the prefix and suffix
prefix = "KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qZUL"
suffix = "zzzzzz"

# Read the original file, modify each line, and write to a new file
with open('random_output.txt', 'r') as infile, open('modified_output.txt', 'w') as outfile:
    for line in infile:
        # Strip the newline character from the end of the line
        modified_line = prefix + line.strip() + suffix
        # Write the modified line to the new file
        outfile.write(modified_line + '\n')
