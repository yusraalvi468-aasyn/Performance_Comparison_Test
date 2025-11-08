from multiprocessing import Process
import time

def work():
    while True:
        print("Working...")
        time.sleep(1)

if __name__ == "__main__":
    p = Process(target=work)
    p.start()
    time.sleep(3)
    p.terminate()
    print("Process stopped")
