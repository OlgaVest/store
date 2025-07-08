import os
import zipfile
from datetime import datetime

BASE_DIR = os.getcwd()
DATA_DIR = os.path.join(BASE_DIR, "data")
BACKUP_DIR = os.path.join(BASE_DIR, "backups")

# Имя архива с текущей датой
today = datetime.now().strftime("%Y%m%d")
backup_name = f"backup_{today}.zip"
backup_path = os.path.join(BACKUP_DIR, backup_name)

def create_zip_backup():
    with zipfile.ZipFile(backup_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(DATA_DIR):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, DATA_DIR)  # путь внутри архива
                zipf.write(full_path, arcname)
                print(f"📦 Добавлено в архив: {arcname}")
    print(f"\n✅ Архив создан: {backup_path}")

if __name__ == "__main__":
    create_zip_backup()