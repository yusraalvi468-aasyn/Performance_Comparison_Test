from multiprocessing import Process, Queue

def worker(q):
    q.put("Message from worker")

if __name__ == "__main__":
    q = Queue()
    processes = [Process(target=worker, args=(q,)) for _ in range(3)]

    for p in processes: p.start()
    for p in processes: p.join()

    while not q.empty():
        print(q.get())
