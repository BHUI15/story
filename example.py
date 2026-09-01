import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor
import asyncio

async def do_async_work(task_id, duration = 0.1):
    await asyncio.sleep(duration)
    return f"Async Task {task_id} completed"

async def run_async_tasks(tasks: int = 5):
    test_list = [do_async_work(i, duration=0.1) for i in range(tasks)]
    results = await asyncio.gather(*test_list)
    return list(results)

def do_cpu_work(task_id, iterations = 1000000):
    total = 0
    for i in range(iterations):
        total += i * i
    return f"CPU Task {task_id} completed with total {total}"


def run_process_pool(tasks: int = 5, max_workers: int = 5):
    results: list[str] = []
    
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures =[executor.submit(do_cpu_work, i, iterations=1000000) for i in range(tasks)]
        
        for future in as_completed(futures):
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                print(f"Task generated an exception: {e}")
    
    return results


# simulate io bound task; Thread is great for io bound tasks, while Process is great for cpu bound tasks
def do_work(task_id, duration = 0.1):
    time.sleep(duration)
    return f"Task {task_id} completed"

# def run_sync_tasks(tasks: int =5):
#     results: list[str] = []
    
#     for i in range(tasks):
#         result = do_work(i, duration=0.1)
#         results.append(result)
#     return results

def run_threading(tasks: int =5, max_workers: int = 5):
    results: list[str] = []
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures =[executor.submit(do_work, i, duration=0.1) for i in range(tasks)]
        
        for future in as_completed(futures):
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                print(f"Task generated an exception: {e}")
    
    return results


if __name__ == "__main__":
    start_time = time.perf_counter()
    results = asyncio.run(run_async_tasks(tasks=5))
    elapsed_time = time.perf_counter() - start_time

    print("Async Task Results:")
    for result in results:
        print(f" {result}")
    
    print(f"\nTotal time taken: {elapsed_time:.2f} seconds")
    print("Note: Tasks ran concurrently using asyncio (asynchronous execution)")

