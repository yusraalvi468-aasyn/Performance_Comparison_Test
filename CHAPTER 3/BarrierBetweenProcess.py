from multiprocessing import Process, Barrier
import time

def player(barrier, id):
    print(f"Player {id} ready")
    time.sleep(1)
    barrier.wait()
    print(f"Player {id} started together")

if __name__ == "__main__":
    barrier = Barrier(3)
    for i in range(3):
        Process(target=player, args=(barrier,i)).start()
