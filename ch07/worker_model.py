from multiprocessing import Process, Queue
import time

def worker(task_queue):
    while not task_queue.empty():
        task = task_queue.get()
        print(f"Worker {task} is processing")
        time.sleep(1)
        print(f"Worker {task} completed")

def main():
    task_queue = Queue()

    for i in range(10):
        task_queue.put(i)

    processes = [
        Process(target=worker, args=(task_queue, ))
        for _ in range(5)
    ]

    # Start the worker process
    for p in processes:
        p.start()

    # Wait for all workers process to finish
    for p in processes:
        p.join()

    print("All tasks completed.")

if __name__ == "__main__":
    main()
