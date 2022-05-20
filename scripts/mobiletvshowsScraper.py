from threading import Thread, Lock
mutex = Lock()
counter: int = 0

def increment():
    global counter
    mutex.acquire()
    counter += 1
    mutex.release()

def main():

    vec = []
    for i in range(10):
        t = Thread(target=increment)
        vec.append(t)
    for t in vec:
        t.start()
    for t in vec:
        t.join()
    print(f'counter = {counter}')

if __name__ == '__main__':
    main()

