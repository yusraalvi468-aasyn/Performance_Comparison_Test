import threading
import time

traffic_signal = threading.Event()

def car(id):
    print(f"Car {id} is waiting for green light...")
    traffic_signal.wait() 
    print(f"Car {id} is now moving.")

def traffic_controller():
    print("Red Light! Cars must wait...")
    time.sleep(3)
    print("Green Light! Cars can go now.")
    traffic_signal.set()   

threads = []
for i in range(1, 4):
    t = threading.Thread(target=car, args=(i,))
    threads.append(t)
    t.start()

controller = threading.Thread(target=traffic_controller)
controller.start()

for t in threads:
    t.join()
controller.join()
