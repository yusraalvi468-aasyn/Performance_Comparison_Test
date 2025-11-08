import threading
import time

lock = threading.Lock()
piggy_bank = 0  

def add_money(amount, thread_name):
    global piggy_bank
    for i in range(5):   
        with lock:  
            print(f"{thread_name} is depositing...")
            temp = piggy_bank
            time.sleep(0.2)  
            piggy_bank = temp + amount
            print(f"{thread_name} updated balance to: {piggy_bank}")

t1 = threading.Thread(target=add_money, args=(10, "Person 1"))
t2 = threading.Thread(target=add_money, args=(20, "Person 2"))

t1.start()
t2.start()

t1.join()
t2.join()

print("\nFinal Balance in Piggy Bank:", piggy_bank)
