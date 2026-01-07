# Chapter 06 – Distributed Systems and Network Communication

This chapter focuses on **distributed computing** and **network-based communication** using Python. It demonstrates three approaches for executing tasks across processes or machines, ranging from high-level frameworks to low-level socket programming.

The goal is to understand how **parallel tasks**, **remote communication**, and **network protocols** work in real-world distributed systems.

---

## Topics Covered

### 1. Celery – Distributed Task Queue
Celery is a high-level framework used to execute tasks asynchronously using background workers.

**Key Features**
- Uses a message broker such as RabbitMQ or Redis
- Computational tasks (e.g., GCD and LCM) are defined as background jobs
- Workers execute tasks independently of the client

**Workflow**
1. Client submits a task
2. Task is sent to the message broker
3. Worker picks up and executes the task asynchronously
4. Result is returned to the client

**Use Case**
- Background job processing
- Distributed computation
- Scalable parallel task execution

---

### 2. Pyro4 – Remote Method Invocation (RMI)
Pyro4 allows Python objects to be accessed remotely as if they were local.

**Key Features**
- Uses a Name Server to locate remote objects
- Supports object-oriented distributed systems
- Communication is handled using proxies

**Demonstration**
- A daisy-chain topology is implemented:
  - Server 1 → Server 2 → Server 3 → Server 1
- Messages and mathematical parameters flow through each server sequentially

**Use Case**
- Remote procedure calls
- Distributed object-oriented applications

---

### 3. Sockets – Low-Level TCP/IP Communication
Socket programming provides direct access to network communication using raw data streams.

**Key Features**
- Uses TCP/IP protocol
- No abstraction layer; communication logic is handled manually

**Demonstrations**
- **Math Server:** Accepts inputs like `48,18` and returns computed results
- **File Transfer:** Sends and receives binary files (e.g., `mytext.txt`) over a network

**Use Case**
- Custom network protocols
- File transfer systems
- Low-level network programming

---

### Technology Comparison

| Technology | Abstraction Level | Purpose | Scaling Method |
|------------|-----------------|--------|----------------|
| Celery     | High            | Asynchronous task execution | Horizontal worker scaling |
| Pyro4      | High            | Remote object communication | Object proxy mechanism |
| Sockets    | Low             | Custom networking & data transfer | Byte-stream communication |

