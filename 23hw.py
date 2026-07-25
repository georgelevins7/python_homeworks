import asyncio
import time

tasks = [
    ("Downloading data", 3),
    ("Processing data", 2),
    ("Sending notification", 1),
    ("Saving results", 4),
]

async def do_task(name, duration):
    print(f"Starting task: {name}")
    await asyncio.sleep(duration)
    print(f"Completed task: {name}")
    return f"Task completed: {name}"

async def sequential_execution():
    start_time = time.perf_counter()
    results = []
    for name, duration in tasks:
        result = await do_task(name, duration)
        results.append(result)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return results, execution_time

async def concurrent_execution():
    start_time = time.perf_counter()
    coroutines = [do_task(name, duration) for name, duration in tasks]
    results = await asyncio.gather(*coroutines)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return results, execution_time

async def main():
    print("Sequential Execution:")
    sequential_results, sequential_time = await sequential_execution()
    for result in sequential_results:
        print(result)
    print(f"Total time for sequential execution: {sequential_time:.2f} seconds\n")

    print("Concurrent Execution:")
    concurrent_results, concurrent_time = await concurrent_execution()
    for result in concurrent_results:
        print(result)
    print(f"Total time for concurrent execution: {concurrent_time:.2f} seconds\n")

asyncio.run(main())