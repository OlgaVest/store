import os
from datetime import datetime
import chardet  # Не забудь установить: pip install chardet

BASE_DIR = os.getcwd()
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
LOG_FILE = os.path.join(BASE_DIR, "logs", "processing_log.txt")

def detect_encoding(file_path):
    with open(file_path, "rb") as f:
        result = chardet.detect(f.read())
    return result["encoding"]

def invert_case(text):
    return text.swapcase()  # Заглавные -> строчные и наоборот

def process_files():
    log_lines = []

    for filename in os.listdir(RAW_DIR):
        raw_path = os.path.join(RAW_DIR, filename)
        try:
            encoding = detect_encoding(raw_path)
            with open(raw_path, "r", encoding=encoding) as f:
                original_text = f.read()

            transformed_text = invert_case(original_text)
            new_filename = filename.replace(".txt", "_processed.txt")
            processed_path = os.path.join(PROCESSED_DIR, new_filename)

            with open(processed_path, "w", encoding="utf-8") as f:
                f.write(transformed_text)

            log_line = f"{datetime.now()} - Обработан файл: {filename} → {new_filename} (исходная кодировка: {encoding})"
        except Exception as e:
            log_line = f"{datetime.now()} - ❌ Ошибка при обработке файла {filename}: {e}"

        print(log_line)
        log_lines.append(log_line)

    return log_lines

def write_log(logs):
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        for line in logs:
            log.write(line + "\n")

if __name__ == "__main__":
    logs = process_files()
    write_log(logs)