import multiprocessing
import time
import sys

def function1():
    id =multiprocessing.current_process().pid
    print("My Process starting ", id)
    time.sleep(10)
    print("My Process stopping ", id)


def func2():
    id =multiprocessing.current_process().pid
    print(id, " started")
    sys.stdout.flush()
    time.sleep(10)
    print("My Process stopping ", id)
    sys.stdout.flush()





if __name__ == "__main__":
    service = multiprocessing.Process(target=function1)
    service.daemon = True
    service1 = multiprocessing.Process(target=func2)
    service1.daemon = False
    service.start()
    time.sleep(2)
    service1.start()

    service.join()
    service1.join()