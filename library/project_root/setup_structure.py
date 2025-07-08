import os
from datetime import datetime

# Базовая директория проекта (предположим, что скрипт запускается из project_root)
BASE_DIR = os.getcwd()

# Директории, которые нужно создать
folders = [
    "data/raw",
    "data/processed",
    "logs",
    "backups",
    "output"
]

def create_directories():
    log_lines = []
    for folder in folders:
        path = os.path.join(BASE_DIR, folder)
        try:
            os.makedirs(path, exist_ok=True)  # не вызывает ошибку, если папка уже есть
            log_line = f"{datetime.now()} - Директория создана (или уже существует): {path}"
            print(log_line)
            log_lines.append(log_line)
        except Exception as e:
            log_line = f"{datetime.now()} - Ошибка при создании {path}: {e}"
            print(log_line)
            log_lines.append(log_line)
    return log_lines

def write_log(log_lines):
    logs_path = os.path.join(BASE_DIR, "logs", "setup_log.txt")
    with open(logs_path, "a", encoding="utf-8") as log_file:
        for line in log_lines:
            log_file.write(line + "\n")

if __name__ == "__main__":
    logs = create_directories()
    write_log(logs)