import threading
import time

start = time.perf_counter()

def do_something():
    print("Sleep 1 second...")
    time.sleep(1)
    print("Done Sleeping...")

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

# wait for threads to finish
t1.join()
t2.join()

end = time.perf_counter()

print(f"Finished in {round(end-start, 2)} second(s)")

