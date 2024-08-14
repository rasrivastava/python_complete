import multiprocessing
import time

def print_numbers():
    """Function to print numbers from 1 to 5"""
    for i in range(1, 6):
        print(f'Number: {i}')
        time.sleep(1)

def print_letters():
    """Function to print letters A to E"""
    for letter in 'ABCDE':
        print(f'Letter: {letter}')
        time.sleep(1)

if __name__ == '__main__':
    # Create two processes
    p1 = multiprocessing.Process(target=print_numbers)
    p2 = multiprocessing.Process(target=print_letters)
    
    # Start the processes
    p1.start()
    p2.start()
    
    # Wait for both processes to complete
    p1.join()
    p2.join()
    
    print('Both processes have finished.')

"""
Letter: A
Number: 1
Letter: B
Number: 2
Letter: C
Number: 3
Number: 4
Letter: D
Number: 5
Letter: E
Both processes have finished.
"""