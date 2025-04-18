import time
import concurrent.futures # thread pool executor (best to use with context)


start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return 'Done Sleeping'

with concurrent.futures.ThreadPoolExecutor() as executor:

    results = [executor.submit(do_something, 1) for _ in range(10)]
    
    for f in concurrent.futures.as_completed(results):
        print(f.result())


finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')

