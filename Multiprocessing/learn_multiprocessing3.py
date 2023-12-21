from concurrent.futures import ProcessPoolExecutor
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleep {seconds} second...")
    time.sleep(seconds)
    return "Done Sleeping..."

if __name__ == "__main__":

    with ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 1)
        print(f1.result())  # return value

    end = time.perf_counter()

    print(f"Finished in {round(end-start, 2)} second(s)")