# Базовый образ
FROM python:3.11-slim

# Рабочая директория
WORKDIR /app

# Копируем все файлы
COPY . /app

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Запуск
CMD python -m unittest discover -s . -p "test_*.py" && python main.py
