import os
from datetime import datetime

BASE_DIR = os.getcwd()
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
LOG_FILE = os.path.join(BASE_DIR, "logs", "file_creation_log.txt")

# Данные: имя файла, текст и кодировка
files_to_create = [
    ("utf8_text.txt", "Привет, мир! Это UTF-8.", "utf-8"),
    ("latin1_text.txt", "Bonjour tout le monde! Ça va?", "iso-8859-1"),
    ("ascii_text.txt", "Hello, world! Plain ASCII.", "ascii")
]

def create_files():
    log_lines = []

    for filename, text, encoding in files_to_create:
        path = os.path.join(RAW_DIR, filename)
        try:
            with open(path, "w", encoding=encoding) as f:
                f.write(text)
            log_line = f"{datetime.now()} - Файл создан: {filename} (кодировка: {encoding})"
        except Exception as e:
            log_line = f"{datetime.now()} - Ошибка при создании файла {filename}: {e}"
        print(log_line)
        log_lines.append(log_line)

    return log_lines

def write_log(log_lines):
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        for line in log_lines:
            log.write(line + "\n")

if __name__ == "__main__":
    logs = create_files()
    write_log(logs)