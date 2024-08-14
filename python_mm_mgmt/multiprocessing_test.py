import time
import multiprocessing

def compute_sum_of_squares(start, end):
    """Compute the sum of squares from start to end."""
    total = 0
    for i in range(start, end):
        total += i * i
    return total

def worker(start, end, result_queue):
    """Worker function to compute sum of squares."""
    total = compute_sum_of_squares(start, end)
    result_queue.put(total)

def single_core_task():
    """Compute the sum of squares on a single core."""
    start_time = time.time()
    result = compute_sum_of_squares(0, 10000000)
    end_time = time.time()
    print(f'Single core result: {result}')
    print(f'Single core time: {end_time - start_time:.2f} seconds')

def multi_core_task(num_cores):
    """Compute the sum of squares using multiple cores."""
    start_time = time.time()
    chunk_size = 10000000 // num_cores
    processes = []
    results = multiprocessing.Queue()

    for i in range(num_cores):
        start = i * chunk_size
        end = start + chunk_size
        p = multiprocessing.Process(target=worker, args=(start, end, results))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    total = 0
    while not results.empty():
        total += results.get()
    
    end_time = time.time()
    print(f'Multi-core result: {total}')
    print(f'Multi-core time: {end_time - start_time:.2f} seconds')

if __name__ == '__main__':
    # Use a fixed number of cores
    num_cores = multiprocessing.cpu_count()
    print(f"total core on which this program is run is :: {num_cores}")

    print("Running single-core task...")
    single_core_task()

    print("\nRunning multi-core task...")
    multi_core_task(num_cores)
