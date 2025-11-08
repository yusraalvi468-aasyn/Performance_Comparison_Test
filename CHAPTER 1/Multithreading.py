import time
from threading import Thread

array_size = 10_000_00
array = list(range(array_size))
result = [0] * array_size

def multiply(start, end):
    for i in range(start, end):
        result[i] = array[i] * 2

start_time = time.time()

thread1 = Thread(target=multiply, args=(0, array_size // 4))
thread2 = Thread(target=multiply, args=(array_size // 4, array_size // 2))
thread3 = Thread(target=multiply, args=(array_size // 2, 3 * array_size // 4))
thread4 = Thread(target=multiply, args=(3 * array_size // 4, array_size))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

end_time = time.time()

print("Multithreading Multiplication Completed")
print("Time Taken:", end_time - start_time, "seconds")
