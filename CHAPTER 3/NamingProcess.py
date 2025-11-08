from multiprocessing import Process, current_process

def work():
    print("Working:", current_process().name)

if __name__ == "__main__":
    p = Process(target=work, name="Data_Cleaner_Process")
    p.start()
    p.join()
