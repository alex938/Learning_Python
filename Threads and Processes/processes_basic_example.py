from multiprocessing import Process
import multiprocessing

def work():
    print("Starting work")
    i = 0
    for _ in range(20000000):
        i += 1
    print("Finished work")

if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")
    processes = []
    for _ in range(5):
        p = Process(target=work, args=())
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()