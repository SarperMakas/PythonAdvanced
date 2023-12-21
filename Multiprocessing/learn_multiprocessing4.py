from concurrent.futures import ProcessPoolExecutor, as_completed
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleep {seconds} second...")
    time.sleep(seconds)
    return f"Done Sleeping... {seconds}"

if __name__ == "__main__":

    with ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = [executor.submit(do_something, sec) for sec in secs]

        for f in as_completed(results):
            print(f.result())

    end = time.perf_counter()

    print(f"Finished in {round(end-start, 2)} second(s)")