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
        results = executor.map(do_something, secs)

        for result in results:
            print(result)

    end = time.perf_counter()

    print(f"Finished in {round(end-start, 2)} second(s)")