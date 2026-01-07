# Chapter 05 – Performance Comparison: Concurrency Models in Python

This project analyzes the behavior of **Asyncio**, **Multithreading**, and **Multiprocessing** across different computational tasks in Python.  
It demonstrates how different concurrency models perform under I/O-bound and CPU-bound workloads.

---

## **Analysis of Scripts**

### 1. Task Management (`asyncio_task_manipulation.py`)
- Demonstrates **cooperative multitasking** using `asyncio`.
- Confirms that `asyncio.sleep` allows other tasks to progress.
- CPU-bound tasks are safely offloaded to threads using `asyncio.to_thread`.

---

### 2. Execution Pools (`concurrent_futures_pooling.py`)
- Compares **Sequential**, **ThreadPool**, and **ProcessPool** execution.
- **Comparison Results:**
  - **Sequential:** Baseline performance
  - **Threads:** Efficient for I/O tasks; limited by Python’s GIL for CPU-bound math
  - **Processes:** Fastest for heavy computation, but has higher startup costs

---

### 3. Integrated Coroutines (`asyncio_and_futures.py`)
- Shows how `asyncio` can orchestrate both **simple async functions** and **heavy computations** efficiently.
- Integrates thread and process execution within the event loop.

---

### 4. Recursive Chaining (`asyncio_coroutine.py` & `asyncio_event_loop.py`)
- Explores **event loop persistence** and **recursive scheduling**.
- Highlights the importance of **termination conditions** in async loops to prevent infinite execution.

---

## **Technical Summary**

| Model            | Primary Use Case                 | Parallelism                   |
|-----------------|---------------------------------|-------------------------------|
| Asyncio         | Web servers, I/O tasks          | Cooperative (Single-core)     |
| Threading       | Waiting for responses/files     | Shared Memory (GIL limited)   |
| Multi-processing| Heavy math and data crunching   | True Parallel (Multi-core)    |

---


