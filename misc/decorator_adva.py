import time

def timing_decorator(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        #print(f"Total time taken: {end - start:.6f} seconds")
        return result, end - start
    return wrapper

@timing_decorator
def use_decorator(s1):
    if len(s1) == 0:
        return 0
    if len(s1) == 1:
        return s1
    return use_decorator(s1[1:])[0] + s1[0]
    #return s1[::-1]

s1 = "RAHUL"

if __name__ == "__main__":
    result, total_time = use_decorator(s1)
    print(result)
    print(f"Total time taken: {total_time:.6f} seconds")
