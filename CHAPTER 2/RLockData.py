import threading
import time

lock = threading.RLock()
shared_value = 0

def update_value():
    global shared_value
    with lock:
        temp = shared_value
        temp += 1
        time.sleep(0.5)
        shared_value = temp
        print("Value updated to:", shared_value)

threads = []
for i in range(5):
    t = threading.Thread(target=update_value)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
