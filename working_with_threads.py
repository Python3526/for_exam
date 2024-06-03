import threading
from time import sleep


def print_numbers():
    for i in range(1, 5):
        print(i)
        sleep(1)


def print_letters():
    for i in 'ABCDE':
        print(i)
        sleep(1)


thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)


def start_threads():
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
