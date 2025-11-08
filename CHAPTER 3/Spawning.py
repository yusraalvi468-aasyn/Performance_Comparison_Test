from multiprocessing import Process
import time

def worker(task):
    print(f"Worker is doing: {task}")
    time.sleep(1)

if __name__ == "__main__":
    p1 = Process(target=worker, args=("Washing",))
    p2 = Process(target=worker, args=("Cleaning",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("All work done.")
