# Using queue.Queue
# • The queue.Queue data structure can be used to synchronize both threads and processes
import threading
import queue
q = queue.Queue()


def worker():
    while True:
        item = q.get()
        print(f"Item {item}.", end=" ")
        q.task_done()


threading.Thread(target=worker, daemon=True).start()
for item in range(3):
    q.put(item)
q.join()
print("All done!")

# Output: Item 0. Item 1. Item 2. All done!

# multi processes används för tunga beräkningar och
# multi threading används när man tex måste vänta på en web-sida
