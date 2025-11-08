from multiprocessing import Pool

def square(n):
    return n*n

if __name__ == "__main__":
    with Pool(4) as p:
        result = p.map(square, [1,2,3,4,5])
        print(result)
