import threading
import time

# Only 2 people can enter the shop at the same time
shop_semaphore = threading.Semaphore(2)

def customer(id):
    print(f"Customer {id} is waiting to enter the shop...")
    with shop_semaphore:
        print(f"Customer {id} entered the shop.")
        time.sleep(2)
        print(f"Customer {id} left the shop.")

threads = []
for i in range(1, 6):
    t = threading.Thread(target=customer, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
