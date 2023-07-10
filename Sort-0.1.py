import os
import shutil
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, cpu_count

def process_folder(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            _, ext = os.path.splitext(file)
            ext = ext[1:]
            os.makedirs(os.path.join(path, ext), exist_ok=True)
            shutil.move(os.path.join(root, file), os.path.join(path, ext, file))

def process_folder_parallel(path):
    with ThreadPoolExecutor() as executor:
        executor.submit(process_folder, path)

def factorize(*numbers):
    factors_list = []
    for number in numbers:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        factors_list.append(factors)
    return factors_list

if __name__ == '__main__':
    path = "Мотлох"
    numbers = [128, 255, 99999, 10651060]

    process_folder_parallel(path)
    a, b, c, d = factorize(*numbers)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]