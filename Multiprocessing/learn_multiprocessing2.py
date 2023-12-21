import time
import multiprocessing

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleep {seconds} second...")
    time.sleep(seconds)
    print("Done Sleeping...")

if __name__ == "__main__":

    processes = []

    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    end = time.perf_counter()

    print(f"Finished in {round(end-start, 2)} second(s)")