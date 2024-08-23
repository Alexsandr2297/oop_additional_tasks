import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()  # Запускаем таймер
        self.elapsed_time = None  # Инициализируем атрибут elapsed_time
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()  # Останавливаем таймер
        self.elapsed_time = self.end_time - self.start_time  # Вычисляем время выполнения
        print(f"Execution time: {self.elapsed_time:.4f} seconds")  # Выводим результат


# Пример использования
with Timer() as timer:
    # блок кода, время выполнения которого нужно измерить
    time.sleep(2)  # Имитация долгой операции
    if timer.elapsed_time is not None:
        # код для проверки

        print("Execution time inside block:", timer.elapsed_time)  # Можно также получить время внутри блока
