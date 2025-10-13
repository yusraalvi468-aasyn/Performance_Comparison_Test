import time
import threading
import multiprocessing

def calculate_square(n):
    total = 0
    for i in range(1, n * 100000):
        total += i * i
    return total

def thread_worker(n):
    calculate_square(n)

def process_worker(n):
    calculate_square(n)

if __name__ == "__main__":
    numbers = [5, 10, 15, 20, 25]

    print(" PERFORMANCE COMPARISON: MULTIPROCESSING vs MULTITHREADING  ")

    # MULTIPROCESSING 
    start = time.time()
    processes = []
    for num in numbers:
        p = multiprocessing.Process(target=process_worker, args=(num,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    process_time = time.time() - start
    print(f"\n🔹 Multiprocessing completed in {process_time:.2f} seconds")

    # MULTITHREADING 
    start = time.time()
    threads = []
    for num in numbers:
        t = threading.Thread(target=thread_worker, args=(num,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    thread_time = time.time() - start
    print(f"🔹 Multithreading completed in {thread_time:.2f} seconds")

    # RESULT
    print("\n   COMPARISON RESULT  ")
    print(f"Multiprocessing time: {process_time:.2f} seconds")
    print(f"Multithreading time: {thread_time:.2f} seconds")

    if process_time < thread_time:
        print("Multiprocessing is faster for CPU-bound tasks.")
    else:
        print("Multithreading performed faster (unusual for CPU-heavy tasks).")
