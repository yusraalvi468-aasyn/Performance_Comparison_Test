# 🧮 Performance Comparison – Multiprocessing vs Multithreading

## 📘 Description  
This Python program compares how fast multiprocessing and multithreading perform when running a CPU-heavy task.

## ⚙️ How It Works  
- The function `calculate_square()` performs large calculations.  
- It runs once with multiple **processes** and once with multiple **threads**.  
- The program measures how long each method takes.

## 🧪 Example Output  
 PERFORMANCE COMPARISON: MULTIPROCESSING vs MULTITHREADING  

🔹 Multiprocessing completed in 0.26 seconds
🔹 Multithreading completed in 0.37 seconds

   COMPARISON RESULT
Multiprocessing time: 0.26 seconds
Multithreading time: 0.37 seconds
Multiprocessing is faster for CPU-bound tasks.

## 💡 Conclusion  
- **Multiprocessing** is faster for CPU-heavy work.  
- **Multithreading** is slower because Python allows only one thread to run at a time (due to the GIL).

## 🧑‍💻 Author  
**Yusra Alvi**
