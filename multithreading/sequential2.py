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
    parser.add_argument("--threads", "-t", type=int, choices=range(1,11),metavar="[1-10]", help="Number of threads to start [range 1-10]", required=True)
    args = parser.parse_args()

    print(args.threads)
    tasks = []

    for i in range(args.threads):
        task(i, random.randint(0, 3))

    print(threading.active_count())
    print(threading.enumerate())
    print(time.perf_counter())


