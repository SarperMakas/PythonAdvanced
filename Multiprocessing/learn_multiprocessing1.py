import time
import multiprocessing

start = time.perf_counter()

def do_something():
    print("Sleep 1 second...")
    time.sleep(1)
    print("Done Sleeping...")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.perf_counter()

    print(f"Finished in {round(end-start, 2)} second(s)")