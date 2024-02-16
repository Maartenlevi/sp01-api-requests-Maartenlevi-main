from api_requests_sim import *
import numpy as np
import time
import priority_queue
import heapq
import timeit


def brute_force(sim_length=100000):
    """ Brute force implementation for finding the highest priority api request """
    global i, start, duration
    i = 0
    api_requests = np.array([])
    start = time.time()
    while i < sim_length:
        api_requests = np.append(api_requests, generate_api_requests(nr_of_new_api_requests))
        api_requests = brute_force_get_api_requests(api_requests)
        i += 1
    duration = time.time() - start
    # convert duration to minutes and seconds
    minutes = int(duration // 60)
    seconds = duration % 60
    print(f"brute force: {minutes} minutes and {seconds} seconds")


def library_priority_queue(sim_length=100000):
    """
    Very optimized version of priority_queue (min-heap)
    """

    global start, i, nr_of_new_api_requests, p, duration
    start = time.time()
    i = 0
    api_requests_pq = []
    while i < sim_length:
        api_requests = generate_api_requests(nr_of_new_api_requests)
        for p in api_requests:
            start_push = timeit.default_timer()
            heapq.heappush(api_requests_pq, p)
            duration_push = timeit.default_timer() - start_push
        start_pop = timeit.default_timer()
        heapq.heappop(api_requests_pq)
        duration_pop = timeit.default_timer() - start_pop

        i += 1
    duration_lib = time.time() - start
    # convert duration to minutes and seconds
    minutes = int(duration_lib // 60)
    seconds = duration_lib % 60
    print(f"lib heapq: {minutes} minutes and {seconds} seconds\n push: {duration_push} seconds\n  pop: {duration_pop} seconds\n")
    return duration_lib

def student_priority_queue(sim_length=100000):
    """ This uses your own implementation of priority queue! """
    global start, i, nr_of_new_api_requests, p, duration
    start = time.time()
    i = 0
    api_requests_pq_custom = []
    while i < sim_length:
        api_requests = generate_api_requests(nr_of_new_api_requests)
        for p in api_requests:
            start_insert = timeit.default_timer()
            priority_queue.insert(api_requests_pq_custom, p)
            duration_insert = timeit.default_timer() - start_insert
        start_pop = timeit.default_timer()
        priority_queue.pop(api_requests_pq_custom)
        duration_pop = timeit.default_timer() - start_pop
        i += 1
    duration_student = time.time() - start

    #convert duration to minutes and seconds
    minutes = int(duration_student // 60)
    seconds = duration_student % 60
    print(f"custom min heap: {minutes} minutes and {seconds} seconds\n insert: {duration_insert} seconds\n  pop: {duration_pop} seconds\n")
    return duration_student

def test_priority_queue(sim_length):
    for sim_length in sim_length:
        print(f"\nSim length: {sim_length}")

        duration_lib = library_priority_queue(sim_length)
        duration_student = student_priority_queue(sim_length)

        speed_factor = round(duration_student / duration_lib, 2)
        print(f"Your implementation is {speed_factor}x slower")

        #brute_force(sim_length)

sim_length = [100000]
test_priority_queue(sim_length)