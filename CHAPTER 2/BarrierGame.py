import threading
import time

# Barrier for 3 players
players_ready = threading.Barrier(3)

def player(id):
    print(f"Player {id} is preparing...")
    time.sleep(1)
    print(f"Player {id} is ready.")
    players_ready.wait()   # Wait until all players are ready
    print(f"Player {id} started the game!")

threads = []
for i in range(1, 4):
    t = threading.Thread(target=player, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
