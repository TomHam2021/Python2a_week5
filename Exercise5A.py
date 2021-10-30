from queue import Queue
from urllib.request import urlopen, Request
import os
import threading


HEADER = {'User-Agent': 'Mozilla/5.0'}

# Note: only URL:s ending on .jpg works
IMG_URLS = ["http://cdn.akc.org/content/article-body-image/lab_puppy_dog_pictures.jpg",
            "https://i.natgeofe.com/n/4f5aaece-3300-41a4-b2a8-ed2708a0a27c/domestic-dog_thumb_4x3.jpg",
            "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg",
            "https://media.npr.org/assets/img/2021/08/06/dog-4415649_wide-3ef4f36fb94397991ee6721a5c6929451178d914.jpg",
            "https://www.dogstrust.org.uk/help-advice/_images/164742v800_puppy-1.jpg",
            "https://cdn.pixabay.com/photo/2016/02/11/17/00/dog-1194087_960_720.jpg",
            "https://cdn.pixabay.com/photo/2016/02/19/15/46/labrador-retriever-1210559_960_720.jpg",
            "https://cdn.pixabay.com/photo/2017/02/16/11/13/dog-2071182_960_720.jpg",
            "https://cdn.pixabay.com/photo/2017/08/28/23/08/dog-2691631__340.jpg",
            "https://cdn.pixabay.com/photo/2020/01/15/19/54/leonberger-4768787__340.jpg",
            "https://cdn.pixabay.com/photo/2016/01/19/16/50/snowflakes-1149417__340.jpg",
            "https://cdn.pixabay.com/photo/2016/02/25/10/31/puppy-1221791__340.jpg",
            "https://cdn.pixabay.com/photo/2015/02/12/10/30/dog-633562__340.jpg",
            "https://cdn.pixabay.com/photo/2019/06/15/18/27/labrador-4276236__340.jpg",
            "https://cdn.pixabay.com/photo/2016/05/06/14/16/dog-1375938__340.jpg",
            "https://cdn.pixabay.com/photo/2017/03/08/13/06/dog-2126708__340.jpg",
            "https://cdn.pixabay.com/photo/2016/06/05/22/45/otter-1438381__340.jpg",
            "https://cdn.pixabay.com/photo/2014/10/22/14/43/otter-498046__340.jpg",
            "https://cdn.pixabay.com/photo/2017/10/23/23/43/otter-2883047__340.jpg"
            ]


SAVE_FOLDER = "C:\Temp\Lesson5PictureFolder"


def request_and_open(URL):
    request = Request(URL, headers=HEADER)
    url_info_byte = urlopen(request, timeout=20).read()
    return url_info_byte


def generate_queue():
    # Instantiate a variable called queue by making it a Queue object:
    queue = Queue()

    # Create a forloop and for each of the urls put the url into the queue.
    for url in IMG_URLS:
        # In the forloop type queue.put(url)
        queue.put(url)
        # The method put() adds an element to the queue represented by a Queue instance.
        # vanje item i kön får en web-url

    return queue


def worker(queue):
    # Now we will define the worker function, this function is meant to
    # instantiate a “worker” that     # takes an object from the queue and
    # works on it. While a worker is working on an object that object becomes
    # inaccessible and once finished the worker removes the object from the
    # queue. This solves the error of having threads colliding and working on
    # the same object

    # Creating a while loop that runs for as long as the queue is not empty
    while not queue.empty():
        url = queue.get()   # Set a variable url = queue.get()
        download_img(url)   # Run the download_img function with the url
        queue.task_done()   # Mark the task as done in the queue
        # Queue.task_done lets workers say when a task is done. Someone
        # waiting for all the work to be done with Queue.join will wait until
        # enough task_done calls have been made, not when the queue is empty.

# Here you can think of the threads as being the puppeteers for the workers,
# the threads control # the workers while they do their job. Good to remember
# that for a thread to work it needs to # have a target function and you need
# to start the thread for it to run. We advise you to read # some of the
# documentation or examples on stackoverflow before proceeding.

# https://medium.datadriveninvestor.com/the-most-simple-explanation-of-threads-and-queues-in-python-cbc206025dd1
# https://stackoverflow.com/questions/49637086/python-what-is-queue-task-done-used-for#49637357


def create_and_run_threads(queue):
    # Set a variable for the number of threads you want to run, 2 or 4 is a
    # good number for this small amount of data
    num_threads = 2
    # Create a for-loop that iterates over the range of the number of threads
    # variable (Note; we are not going to use the value from the forloop)
    for _ in range(num_threads):
        # For each iteration of the for-loop, create a thread that has target
        # as worker and with queue in the args. On the same line you can also
        # start the thread
        threading.Thread(target=worker, args=(queue,)).start()


def download_img(url):
    img_bytes = request_and_open(url)
    img_name = url.split("/")[-1]
    file_path = os.path.join(SAVE_FOLDER, img_name)

    with open(file_path, "wb") as img:
        img.write(img_bytes)
        print(f"Downloading image: {img_name}")


def main():
    queue = generate_queue()
    create_and_run_threads(queue)
    queue.join()
# When you call queue.join() in the main thread, all it does is block the main
# threads until the workers have processed everything that's in the queue.
# It does not stop the worker threads, which continue executing their infinite
# loops.
# If the worker threads are non-deamon, their continuing execution prevents
# the program from stopping irrespective of whether the main thread has
# finished.


if __name__ == "__main__":
    main()
