from concurrent.futures import ThreadPoolExecutor, as_completed
import time

start = time.perf_counter()

def do_something(seconds):
    # print(f"Sleep {seconds} second...")
    time.sleep(seconds)
    return f"Done Sleeping {seconds}..."


with ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    """
    # we are not waiting for all of the threads to finish
    results = [executor.submit(do_something, sec) for sec in secs]

    for f in as_completed(results):
        print(f.result())
    """

    # we wait to finish 5 second thread for printing all of the answers
    results = executor.map(do_something, secs)
    for result in results:
        print(result)



"""
threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
"""

end = time.perf_counter()

print(f"Finished in {round(end-start, 2)} second(s)")

