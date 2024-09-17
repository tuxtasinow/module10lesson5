import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())

def linear_execution(filenames):
    start_time = datetime.datetime.now()
    for filename in filenames:
        read_info(filename)
    end_time = datetime.datetime.now()
    print(f'Линейное выполнение заняло: {end_time - start_time} секунд')

# Многопроцессный вызов функции для всех файлов
def parallel_execution(filenames):
    start_time = datetime.datetime.now()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    end_time = datetime.datetime.now()
    print(f'Многопроцессное выполнение заняло: {end_time - start_time} секунд')

if __name__ == '__main__':
    filenames = [f'./file_{number}.txt' for number in range(1, 5)]

    # linear_execution(filenames)
    # parallel_execution(filenames)
