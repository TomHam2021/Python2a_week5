# Using threads
# • Threads are a way of splitting execution of your code so that things can happen in parallel
# • Threads share memory and can use queues, locks, semaphores and barriers to synchronize
# • In Python, threads are useful for I/O-bound operations
'''
import threading
import time

def hello(i):
    print(i, end=" ")

for i in range(10):
    # skapar en tråd för varje for loop
    threading.Thread(target=hello, args=(i,)).start()

# Output: 0 1 2 3 4 5 6 7 8 9
'''
# Daemon threads
# • Threads and processes that run in the background are called deamons
# • A deamon thread lives until the main thread is terminated
import threading
import time


def hello(i):
    print(i, end=" ")
    time.sleep(0.01)
    print(i, end=" ")


for i in range(10):
    threading.Thread(target=hello, args=(i,), daemon=True).start()
# sleep(0.1) --> Output: 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9
# sleep(0.01) --> Output: 0 1 2 3 4 5 0 6 17  2 8 3 9 4 5 6 7 8 9
