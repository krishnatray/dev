#!/usr/bin/python3

import time
import threading
import random 
import argparse

def task(id, sleep_duration):
    print(f"=> starting task #{id} for {sleep_duration} seconds")
    time.sleep(sleep_duration)
    print(f":) task #{id} done!")


if __name__ == "__main__":

    # CLI arguments
    parser = argparse.ArgumentParser(description="Python Multithreading Demo")
    parser.add_argument("--threads", "-t", type=int,choices=range(1,10001),metavar="[1-10000]",  help="Number of threads to start [range 1-10000]", required=True)
    args = parser.parse_args()

    print(args.threads)
    tasks = []

    for i in range(args.threads):
        tasks.append( threading.Thread(target = task, args=(i, random.randint(0, 3))))
        tasks[i].start()

    print(threading.active_count())
    print(threading.enumerate())

    for i in range(args.threads):
        tasks[i].join()


    print(threading.active_count())
    print(threading.enumerate())
    print(time.perf_counter())


