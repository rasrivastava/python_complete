def read_large_file(file_path):
    """Generator that yields lines from a file one at a time."""
    with open(file_path, 'r') as file:
        for line in file:
            yield line

# Usage example: Processing each line
def process(line):
    """Placeholder function to process each line."""
    print(line.strip())  # Replace this with actual processing logic

# Using the generator to read and process the file
for line in read_large_file('large_file.txt'):
    process(line)


# Advantages of This Approach

# Memory Efficiency:
  # Only one line of the file is in memory at any given time,
  # regardless of the file's size.

# Simplicity:
  # The code is straightforward and easy to integrate
  # into larger processing pipelines.

# Scalability:
  # This method can handle very large files,
  # even those that exceed the available system memory.

