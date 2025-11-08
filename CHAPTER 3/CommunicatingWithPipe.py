from multiprocessing import Process, Pipe

def sender(conn):
    conn.send("Hello from sender")
    conn.close()

def receiver(conn):
    print(conn.recv())

if __name__ == "__main__":
    parent, child = Pipe()
    Process(target=sender, args=(child,)).start()
    Process(target=receiver, args=(parent,)).start()
