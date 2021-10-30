import queue
import threading
import time


def func(q, thread_no):
    while True:
        task = q.get()
        time.sleep(2)
        q.task_done()
        print(f'Thread #{thread_no} is doing task #{task} in the queue.')


q = queue.Queue()

for i in range(4):
    worker = threading.Thread(target=func, args=(q, i,), daemon=True)
    worker.start()

for j in range(10):
    q.put(j)

q.join()
