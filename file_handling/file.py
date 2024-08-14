file_path = "test.txt"

file = open(file_path, "r")

for line in file:
    print(line)

"""
Hello world
GeeksforGeeks
123 456
"""

file = open(file_path, "r")
print(file.read())

"""
Hello world
GeeksforGeeks
123 456
"""

with open(file_path) as file:
    data = file.read()
print(data)

"""
Hello world
GeeksforGeeks
123 456
"""

# read certain number of containers
file = open(file_path, "r")
print(file.read(5)) # Hello


# line wise split
with open(file_path) as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

"""
['Hello', 'world']
['GeeksforGeeks']
['123', '456']
"""


"""
Hello world
GeeksforGeeks
123 456
"""

with open(file_path, 'rb') as file:
   # Read the first 5 bytes
   file.seek(0) # Move the pointer to the start of the file
   first_five = file.read(5)
   print(f"First 5 bytes: {first_five}") # First 5 bytes: b'Hello'

   # Move the pointer to the beginning of the second line
   file.seek(6)  # 12th byte: directly after "Hello world\n"
   second_line = file.read(11)  # Read 11 bytes (length of b'world\nGeeks')
   print(f"Second line: {second_line}") # Second line: b'world\nGeeks'

   current_position = file.tell()
   print(f"Current file pointer position: {current_position}")
   # Current file pointer position: 17


# Open the file in binary read mode ('rb')
with open(file_path, 'rb') as file:
    # Move the file pointer to 3 bytes before the end of the file
    file.seek(-3, 2)  # '-3' to go back 3 bytes, '2' indicates the end of the file
    
    # Read the last 3 bytes
    last_three = file.read(3)
    print(f"Last three characters: {last_three.decode('utf-8')}")
    # Last three characters: 456

