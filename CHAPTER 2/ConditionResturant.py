import threading
import time

order_ready = False
condition = threading.Condition()

def chef():
    global order_ready
    print("Chef: Preparing the food...")
    time.sleep(3)
    with condition:
        order_ready = True
        print("Chef: Food is ready!")
        condition.notify()   

def waiter():
    global order_ready
    print("Waiter: Waiting for food...")
    with condition:
        condition.wait()     
        print("Waiter: Serving the food to the customer.")

t1 = threading.Thread(target=chef)
t2 = threading.Thread(target=waiter)

t1.start()
t2.start()

t1.join()
t2.join()
