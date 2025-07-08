import os
import json
from datetime import datetime
import chardet

BASE_DIR = os.getcwd()
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
OUTPUT_FILE = os.path.join(BASE_DIR, "output", "processed_data.json")

def detect_encoding(file_path):
    with open(file_path, "rb") as f:
        result = chardet.detect(f.read())
    return result["encoding"]

def invert_case(text):
    return text.swapcase()

def get_file_info(processed_filename):
    # Восстанавливаем имя оригинального файла
    original_filename = processed_filename.replace("_processed", "")
    raw_path = os.path.join(RAW_DIR, original_filename)
    processed_path = os.path.join(PROCESSED_DIR, processed_filename)

    encoding = detect_encoding(raw_path)
    with open(raw_path, "r", encoding=encoding) as f:
        original_text = f.read()

    with open(processed_path, "r", encoding="utf-8") as f:
        processed_text = f.read()

    file_stat = os.stat(processed_path)
    return {
        "filename": processed_filename,
        "original_text": original_text,
        "processed_text": processed_text,
        "size_bytes": file_stat.st_size,
        "last_modified": datetime.fromtimestamp(file_stat.st_mtime).isoformat()
    }

def serialize_all():
    data = []
    for fname in os.listdir(PROCESSED_DIR):
        if fname.endswith("_processed.txt"):
            try:
                info = get_file_info(fname)
                data.append(info)
                print(f"✅ Добавлен в JSON: {fname}")
            except Exception as e:
                print(f"❌ Ошибка с файлом {fname}: {e}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out_file:
        json.dump(data, out_file, indent=4, ensure_ascii=False)
        print(f"\n📁 Данные сериализованы в: {OUTPUT_FILE}")

if __name__ == "__main__":
    serialize_all()