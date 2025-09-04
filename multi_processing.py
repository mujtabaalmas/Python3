# from multiprocessing import Process


# def print_func(continent='Asia'):
#     print('The name of continent is : ', continent)

# if __name__ == "__main__":  # confirms that the code is under main function
#     names = ['America', 'Europe', 'Africa']
#     procs = []
#     proc = Process(target=print_func)  # instantiating without any argument
#     procs.append(proc)
#     proc.start()

#     # instantiating process with arguments
#     for name in names:
#         # print(name)
#         proc = Process(target=print_func, args=(name,))
#         procs.append(proc)
#         proc.start()

#     # complete the processes
#     for proc in procs:
#         proc.join()

# import multiprocessing as mp 
# import math
# import time

# results_a = []
# results_b = []
# results_c = []

# def calculation_a(numbers):
#     for number in numbers:
#         results_a.append(math.sqrt(number **2))


# def calculation_b(numbers):
#     for number in numbers:
#         results_b.append(math.sqrt(number **3))

# def calculation_c(numbers):
#     for number in numbers:
#         results_c.append(math.sqrt(number **4))

# if __name__ == '__main__':

#     number_list = list(range(3000000))

#     p1 = mp.Process(target=calculation_a, args=(number_list,))
#     p2 = mp.Process(target=calculation_b, args=(number_list,))
#     p3 = mp.Process(target=calculation_c, args=(number_list,))

#     start = time.time()
#     p1.start()
#     p2.start()
#     p3.start()
#     end = time.time()

#     print("Execution time with multiprocessing: ",round(end-start,5),end=' sec')

#     start = time.time()
#     calculation_a(number_list)
#     calculation_b(number_list)
#     calculation_c(number_list)
#     end = time.time()

#     print("\nExecution time without mucltiprocessing: ",round(end-start,5),end=' sec')

from multiprocessing import Lock, Process, Queue, current_process
import time
import queue # imported for using queue.Empty exception
import multiprocessing

local_number_of_cpu = multiprocessing.cpu_count() #to get no. of cpu in laptop for process

def do_job(tasks_to_accomplish, tasks_that_are_done):
    while True:
        try:
            '''
                try to get task from the queue. get_nowait() function will 
                raise queue.Empty exception if the queue is empty. 
                queue(False) function would do the same task also.
            '''
            task = tasks_to_accomplish.get_nowait()
        except queue.Empty:

            break
        else:
            '''
                if no exception has been raised, add the task completion 
                message to task_that_are_done queue
            '''
            print(task,sep='')
            tasks_that_are_done.put(task + ' is done by ' + current_process().name)
            time.sleep(.000001)
    return True


def main():
    number_of_task = 10
    #print("Number of cpu : ", multiprocessing.cpu_count())
    number_of_processes = local_number_of_cpu
    tasks_to_accomplish = Queue()
    tasks_that_are_done = Queue()
    processes = []

    for i in range(number_of_task):
        tasks_to_accomplish.put("Task no " + str(i+1))

    # creating processes
    for w in range(number_of_processes):
        p = Process(target=do_job, args=(tasks_to_accomplish, tasks_that_are_done))
        processes.append(p)
        p.start()

    # completing process
    for p in processes:
        p.join()

    # print the output
    while not tasks_that_are_done.empty():
        print(tasks_that_are_done.get())

    return True


if __name__ == '__main__':
    main()