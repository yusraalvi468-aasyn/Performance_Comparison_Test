# Chapter 2 — Thread Synchronization Using Locks, Semaphores, Barriers, Events, and Conditions

This chapter focuses on **synchronization mechanisms** used when multiple threads access shared data or need coordinated execution.
These synchronization tools prevent data corruption, race conditions, and ensure threads operate in the correct order.

The chapter includes **real-world analogies** and Python examples for each concept.

---

## Included Python Files

| File Name                 | Synchronization Mechanism | Real-Life Concept Example                                      | Purpose                                                                 |
|--------------------------|--------------------------|-----------------------------------------------------------------|-------------------------------------------------------------------------|
| `SemaphoreCustomer.py` | Semaphore                | *Only 2 customers are allowed inside a small shop at a time*    | Controls how many threads can access a shared resource simultaneously. |
| `BarrierGame.py`   | Barrier                  | *Game waits until all players are "ready" to start together*    | Makes threads wait until all threads reach a certain point.            |
| `EventTraffic.py`     | Event                    | *Traffic signal telling cars when to move*                      | One thread triggers other threads to continue execution.               |
| `ConditionResturant.py` | Condition                | *Waiter waits until food is prepared before serving*            | Allows threads to wait for certain conditions to be true.             |
| `RLockData.py`     | Reentrant Lock (RLock)   | *A resource requires step-by-step updates without interruption* | Allows a thread to acquire the same lock multiple times safely.       |

---

## 1. Semaphore (`SemaphoreCustomer.py`)

### Concept
A **Semaphore** limits how many threads can access a shared resource at the same time.

### Real-Life Example
> A small shop that allows only **2 customers inside** at once.

### Characteristics
- Controls concurrency (limits access count).
- Prevents resource overload.
- Useful where limited resources exist (e.g., printers, database connections).

---

## 2. Barrier (`BarrierGame.py`)

### Concept
A **Barrier** forces all threads to reach a common checkpoint before any thread proceeds.

### Real-Life Example
> A multiplayer game waits until *all players click "Ready"* before starting.

### Characteristics
- Ensures synchronized progression.
- Useful in scientific computing where stages must align.

---

## 3. Event (`EventTraffic.py`)

### Concept
An **Event** acts like a signal. One thread *sets the event*, and other threads wait for it.

### Real-Life Example
> A **green traffic light** signals cars to move.

### Characteristics
- One-to-many communication.
- Used where a trigger or signal starts multiple actions.

---

## 4. Condition (`ConditionResturant.py`)

### Concept
A **Condition** makes threads wait for some shared data to reach a required state.

### Real-Life Example
> A **waiter** waits until the **chef says "order is ready"** before serving.

### Characteristics
- Works with shared resource monitoring.
- Allows fine-grained thread coordination.

---

## 5. RLock — Resturant Lock (`RLockData.py` )

### Concept
An **RLock** allows the same thread to acquire the same lock multiple times without deadlocking itself.

### Real-Life Example
> Updating a resource in **steps**—the thread must stay in control until the update is fully finished.

### Characteristics
- Prevents self-deadlocking.
- Common when functions within a thread call other locked functions.

---

## Chapter Summary

| Mechanism   | Best Used When...                                                            |
|-------------|------------------------------------------------------------------------------|
| Semaphore   | Limited resources must be shared safely (e.g., only 3 database connections). |
| Barrier     | All threads must synchronize before proceeding (e.g., stage computations).   |
| Event       | A trigger must signal other threads to start/stop.                           |
| Condition   | Threads wait for data or state changes.                                      |
| RLock       | Same thread must safely re-lock during nested function calls.                |

---

## Conclusion

This chapter explains how **thread synchronization** prevents race conditions and ensures predictable, coordinated behavior in multi-threaded programs. Choosing the right tool depends on the nature of the shared resources and the required coordination pattern.

---
