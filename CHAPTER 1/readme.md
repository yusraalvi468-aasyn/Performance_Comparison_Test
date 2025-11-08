# Chapter 1 — Parallelism Using Arrays (Processes vs Threads vs Sequential Execution)

This chapter demonstrates how a simple computational task—multiplying elements of an array—behaves when executed in three different ways:

1. **Sequential Execution**
2. **Multithreading**
3. **Multiprocessing**

The purpose is to understand **how parallel execution affects performance**, especially for large datasets.

---

## Included Python Files

| File Name                   | Execution Method        | Description                                                                 |
|----------------------------|-------------------------|-----------------------------------------------------------------------------|
| `array_sequential.py`      | Sequential Execution    | Processes the array in a single loop, one element at a time.               |
| `array_threading.py`       | Multithreading          | Uses multiple threads to divide and compute portions of the array.         |
| `array_multiprocessing.py` | Multiprocessing         | Splits the array into chunks and processes them across multiple CPU cores. |

---

## 1. Sequential Execution (`array_sequential.py`)

### Overview
- Creates a numerical array.
- Multiplies each value inside a simple loop.
- Entire execution occurs in **one thread**, without any parallelism.

### Characteristics
- Simple and easy to understand.
- Performance slows down significantly as array size grows.
- Best only for **small datasets or basic demonstration**.

---

## 2. Multithreading Execution (`array_threading.py`)

### Overview
- Uses the `threading` module.
- The array is divided among multiple threads.
- Each thread performs multiplication on its assigned part.

### Characteristics
- Threads share memory, so no need for data transfer.
- Useful for **I/O-bound or moderately sized CPU tasks**.
- Performance improvement is limited for large, heavy computations due to the **GIL (Global Interpreter Lock)**.

---

## 3. Multiprocessing Execution (`array_multiprocessing.py`)

### Overview
- Uses the `multiprocessing` module and a process pool.
- Splits the array into chunks and distributes work to **multiple CPU cores**.

### Characteristics
- Achieves **true parallelism**.
- Best for **large arrays and CPU-intensive workload**.
- Requires `if __name__ == "__main__":` (especially on Windows) to avoid startup errors.
- Slightly more memory usage due to separate process memory spaces.

---

## Performance Comparison

| Array Size       | Sequential Execution Time       | Multithreading Time                               | Multiprocessing Time                  |
|------------------|--------------------------------|---------------------------------------------------|----------------------------------------|
| 100,000 elements | Slow                           | Faster than Sequential                            | Fastest                                |
| 300,000 elements | Very Slow                      | Moderate                                          | Fast                                   |
| 500,000 elements | Very Slow                      | Noticeable Speed Improvement                      | Very Fast                              |
| 1,000,000+       | Impractical / Too Slow         | Slower than Multiprocessing but Better than Sequential | **Most Efficient & Recommended** |

---

## Interpretation

- **Sequential** is simplest but becomes inefficient as the dataset grows.
- **Multithreading** reduces time moderately and works best when tasks are small or involve waiting (I/O).
- **Multiprocessing** gives the **highest performance** for large numeric workloads by utilizing multiple CPU cores.

---

## Conclusion

- Use **Sequential** only for small or simple tasks.
- Use **Multithreading** for medium workloads or I/O heavy tasks.
- Use **Multiprocessing** when dealing with large data arrays or CPU-intensive operations to achieve significant speed improvement.

---
