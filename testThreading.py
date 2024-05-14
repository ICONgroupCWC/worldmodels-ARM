import os
from multiprocessing import Pool

def task(x):
    return x * x  # Example task, replace it with your actual task

if __name__ == "__main__":
    max_threads = os.cpu_count()  # Get the number of CPU cores
    print("Maximum number of threads:", max_threads)

    # Create a Pool with the maximum number of threads
    with Pool(max_threads) as pool:
        results = pool.map(task, range(10))  # Example: Apply the task function to a range of inputs
        print("Results:", results)
