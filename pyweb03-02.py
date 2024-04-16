import multiprocessing
import time
import logging

# Налаштування рівня логування
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_list(numbers):
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)
    result = pool.map(factorize, numbers)
    pool.close()
    pool.join()
    return result


# Приклад використання
if __name__ == "__main__":
    start_time = time.time()
    a, b, c, d = factorize_list([128, 255, 99999, 10651060])
    end_time = time.time()
    logger.debug(f"Асинхронна версія зайняла {start_time - end_time} секунд")
    

