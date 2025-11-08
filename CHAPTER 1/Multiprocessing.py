import time
from multiprocessing import Pool

array_size = 10_000_00
array = list(range(array_size))

def multiply_chunk(chunk):
    return [x * 2 for x in chunk]

if __name__ == '__main__':   # <-- IMPORTANT LINE ✅

    start_time = time.time()

    chunk_size = array_size // 4
    chunks = [array[i:i + chunk_size] for i in range(0, array_size, chunk_size)]

    with Pool(processes=4) as pool:
        result_chunks = pool.map(multiply_chunk, chunks)

    result = []
    for part in result_chunks:
        result.extend(part)

    end_time = time.time()

    print("Safe Multiprocessing Completed ")
    print("Time Taken:", end_time - start_time, "seconds")
