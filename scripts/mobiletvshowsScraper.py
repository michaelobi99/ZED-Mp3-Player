from time import perf_counter

class Timer():
    def __init__(self):
        self.__start = 0
        self.__stop = 0
        self.__elapsedTime = 0
    def Start(self):
        self.__start = perf_counter()
    def Stop(self):
        self.__stop = perf_counter()
        self.__elapsedTime = self.__stop - self.__start
    def elapsedTime(self):
        return self.__elapsedTime


def main():
    timer = Timer()
    timer.Start()
    file = open(r'C:\Users\HP\PycharmProjects\file.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    number = [eval(line) for line in lines]
    even = lambda x: x % 2 == 0
    divide2 = lambda x: x // 2
    newList = list(map(divide2, list(filter(even, number))))
    print(f'length 0f list = {len(newList)}')
    timer.Stop()
    print(f'elapsed time = {timer.elapsedTime()} sec')

if __name__ == '__main__':
    main()