import multiprocessing

def producer(queue):
    for i in range(5):
        queue.put(i)

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f'Consumed {item}')

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    
    prod = multiprocessing.Process(target=producer, args=(queue,))
    cons = multiprocessing.Process(target=consumer, args=(queue,))
    
    prod.start()
    cons.start()
    
    prod.join()
    queue.put(None)  # Signal the consumer to exit
    cons.join()

"""
Consumed 0
Consumed 1
Consumed 2
Consumed 3
Consumed 4
"""