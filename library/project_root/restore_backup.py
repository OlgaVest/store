import os
import zipfile
from datetime import datetime

BASE_DIR = os.getcwd()
BACKUP_DIR = os.path.join(BASE_DIR, "backups")
RESTORE_DIR = os.path.join(BASE_DIR, "restored_data")

def get_latest_backup():
    """Находит самый новый zip-архив в папке backups/"""
    zip_files = [f for f in os.listdir(BACKUP_DIR) if f.endswith(".zip")]
    if not zip_files:
        raise FileNotFoundError("❌ Нет zip-файлов в папке backups/")
    
    zip_files.sort(reverse=True)  # сортировка по убыванию
    return os.path.join(BACKUP_DIR, zip_files[0])

def extract_backup(zip_path):
    if not os.path.exists(RESTORE_DIR):
        os.makedirs(RESTORE_DIR)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(RESTORE_DIR)
        print(f"✅ Архив извлечён в: {RESTORE_DIR}")
        print(f"📁 Содержимое архива:")
        for name in zip_ref.namelist():
            print(f"   - {name}")

if __name__ == "__main__":
    zip_file = get_latest_backup()
    print(f"🗂️ Восстановление из: {zip_file}")
    extract_backup(zip_file)