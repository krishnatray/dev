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



task1()
task2()
task3()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
