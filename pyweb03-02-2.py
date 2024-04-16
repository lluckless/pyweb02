import time
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_list(numbers):
    result = [factorize(num) for num in numbers]
    return result

# Приклад використання
start_time = time.time()
a, b, c, d = factorize_list([128, 255, 99999, 10651060])
end_time = time.time()
logger.debug(f"Синхронна версія зайняла {start_time - end_time} секунд")

