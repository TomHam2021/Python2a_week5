import queue
import time
import threading
from urllib.request import urlopen, Request
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

# https://www.geeksforgeeks.org/how-to-use-threadpoolexecutor-in-python3/
# Threading allows parallelism of code and Python language has two ways to achieve its 1st is via multiprocessing
# module and 2nd is via multithreading module. Multithreading is well suited to speed up I/O bound tasks like
# making a web request, or database operations, or reading/writing to a file. In contrast to this CPU intensive
# tasks like mathematical computational tasks are benefited the most using multiprocessing.
# This happens due to GIL (Global Interpreter Lock).


# Header with user agent is needed to allow access for scraping
HEADER = {'User-Agent': 'Mozilla/5.0'}
URLS = ['https://www.volvocars.com/se',
        'https://consid.se/',
        'https://stackoverflow.com/',
        'https://9gag.com/',
        'https://www.yahoo.com',
        'https://www.reddit.com',
        'https://www.youtube.com',
        'https://9gag.com/',
        'https://twitter.com/',
        'https://www.volvocars.com/se',
        'https://consid.se/',
        'https://www.reddit.com',
        'https://www.youtube.com',
        'https://stackoverflow.com',
        'https://www.aftonbladet.se/',
        'https://www.volvocars.com/se',
        'https://www.aftonbladet.se/',
        'https://www.volvocars.com/se',
        'https://www.yahoo.com',
        'https://consid.se/',
        'https://www.youtube.com',
        'https://9gag.com/',
        'https://stackoverflow.com/',
        'https://www.volvocars.com/se',
        'https://www.yahoo.com',
        'https://www.reddit.com/',
        'https://consid.se/',
        'https://9gag.com/',
        'https://twitter.com/',
        'https://stackoverflow.com/',
        'https://www.aftonbladet.se/',
        'https://twitter.com/']


def timer(func):
    # Timer is a function you might recognize from last week's assignment but
    # with a slight modification, this time the decorator returns the execution
    # time as well as printing it. This is for gathering the runtime such that
    # the functions performances can be compared in the main function
    def timer_wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        exec_time = end-start
        print(f"Execution time: {(exec_time):.7f} seconds ({func.__name__})")
        return exec_time
    return timer_wrapper


def request_and_open(URL):
    # request_and_open sends a request to a URL and fetches the information.
    # The functions return value is currently unused and simply there in case
    # of if you want to toy around with the information gathered or maybe
    # continue building upon the assignment afterwards.
    request = Request(URL, headers=HEADER)
    url_info_byte = urlopen(request, timeout=20).read()
    url_info_string = url_info_byte.decode("utf-8")
    return url_info_string  # not used..


@timer
def request_single():
    for url in URLS:
        request_and_open(url)


@timer
def request_pool(num_threads):
    # https://www.geeksforgeeks.org/how-to-use-threadpoolexecutor-in-python3/
    # In the request_pool function implement a ThreadPoolExecutor. The executor
    # is a context manager so use it as such. The executor should then map the
    # urls to the request_and_open function using map
    with ThreadPoolExecutor(num_threads) as executor:
        executor.map(request_and_open, URLS)


@timer
def request_queue(num_threads):
    # Create a queue object and put all the urls into it
    queue = Queue()
    for url in URLS:
        queue.put(url)

    def worker(queue):
        # Define a worker function inside the request_queue function that takes as
        # input the queue and calls the request_and_open function. The queue
        # should then mark this task as done
        while not queue.empty():
            request_and_open(queue.get())
            queue.task_done()

    # Create threads up to the num_threads and place the threads to work on the
    # worker queue function. Start the threads ..
    for _ in range(num_threads):
        threading.Thread(target=worker, args=(queue,)).start()
    # .. and then make the main thread wait for the queue to join.
    queue.join()


def main():
    num_threads = [2, 4, 8, 16, 32, 8192]
    num_iterations = 3
    mean_times_pool = []
    mean_times_queue = []

    print(f"Number of threads: 1. Executing...")
    # Main runs the three different request functions and gathers the runtime
    # for each of the functions
    total_time_single = sum(request_single() for _ in range(num_iterations))
    # and then obtains the mean runtime by dividing
    # with the number of iterations.
    mean_time_single = total_time_single/num_iterations

    for i in num_threads:
        # In the for-loop that iterates over num_threads the request_pool and
        # request_queue functions are called using varying number of threads.
        # This is one of the main focuses of the assignment, which is to judge
        # how number of threads improve or decreases performance and compare
        # the Threadpool approach with the queue.
        print(f"Number of threads: {i}. Executing...")
        total_time_pool = sum(request_pool(i) for _ in range(num_iterations))
        total_time_queue = sum(request_queue(i) for _ in range(num_iterations))
        mean_times_pool.append(total_time_pool/num_iterations)
        mean_times_queue.append(total_time_queue/num_iterations)

    print(f"The mean time using single thread: {mean_time_single}")
    print(f"The mean times using thread pool executor are: {mean_times_pool}")
    print(f"The mean times using queue.Queue workers are: {mean_times_queue}")


if __name__ == "__main__":
    main()
'''
Output:
The mean time using single thread: 19.091560920079548
num_threads: 
>> [2,    4,    8,    16,   32,  8192]
The mean times using thread pool executor are: 
>> [8.89, 5.34, 3.10, 2.44, 4.09, 4.63]
The mean times using queue.Queue workers are: 
>> [9.80, 7.51, 3.69, 3.65, 4.77, 10.76]

Snabbast här är : ThreadPoolExecutor och 16 threads

'''
