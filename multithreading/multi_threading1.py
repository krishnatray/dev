#!/usr/bin/python3
import time
import threading

def task1():
    print("=> starting task1")
    time.sleep(2)
    print(":) task1 done!")

def task2():
    print("=> starting task2")
    time.sleep(3)
    print(":) task2 done!")

def task3():
    print("=> starting task3")
    time.sleep(1)
    print(":) task3 done!")


x = threading.Thread(target = task1, args=())
x.start()

y = threading.Thread(target = task2, args=())
y.start()

z = threading.Thread(target = task3, args=())
z.start()

# threading.Thread(target = task1, args=()).start()
# threading.Thread(target = task2, args=()).start()
# threading.Thread(target = task3, args=()).start()


print(threading.active_count())
print(threading.enumerate())

x.join()
y.join()
z.join()



print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())



# for task in x: i.start()