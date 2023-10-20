import time
import threading

# Функция для создания файла с задержкой
def create_file_with_delay(filename):
    # Создаем файл
    with open(filename, 'w') as file:
        file.write("Содержимое файла")

    # Делаем задержку в 1 секунду
    time.sleep(1)

# Засекаем начальное время
start_time = time.time()

# Создаем 100 файлов
for i in range(100):
    filename = f"file_{i}.txt"
    create_file_with_delay(filename)
    print(f"Создан файл: {filename}")

# Засекаем конечное время
end_time = time.time()

# Время выполнения без многопоточности
print(f"Время выполнения без многопоточности: {end_time - start_time} секунд")

# Засекаем начальное время для многопоточного выполнения
start_time = time.time()

# Создаем 100 файлов с использованием многопоточности
threads = []
for i in range(100):
    filename = f"file_thread_{i}.txt"
    thread = threading.Thread(target=create_file_with_delay, args=(filename,))
    threads.append(thread)
    thread.start()

# Ожидаем завершения всех потоков
for thread in threads:
    thread.join()

# Засекаем конечное время для многопоточного выполнения
end_time = time.time()

# Время выполнения с многопоточностью
print(f"Время выполнения с многопоточностью: {end_time - start_time} секунд")
