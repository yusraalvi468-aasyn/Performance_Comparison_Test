import time

array_size = 10_000_00
array = list(range(array_size))

start = time.time()

result = []
for x in array:
    result.append(x * 2)  

end = time.time()

print("Sequential Multiplication Completed")
print("Time Taken:", end - start, "seconds")
