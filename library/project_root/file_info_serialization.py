import os
import json
from datetime import datetime

BASE_DIR = os.getcwd()
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
OUTPUT_FILE = os.path.join(BASE_DIR, "output", "file_info.json")


class FileInfo:
    def __init__(self, name, path, size, created, modified):
        self.name = name
        self.path = path
        self.size = size
        self.created = created
        self.modified = modified

    def to_dict(self):
        return {
            "name": self.name,
            "path": self.path,
            "size": self.size,
            "created": self.created,
            "modified": self.modified
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            path=data["path"],
            size=data["size"],
            created=data["created"],
            modified=data["modified"]
        )

def collect_file_info():
    file_infos = []
    for fname in os.listdir(PROCESSED_DIR):
        full_path = os.path.join(PROCESSED_DIR, fname)
        stat = os.stat(full_path)
        file_info = FileInfo(
            name=fname,
            path=full_path,
            size=stat.st_size,
            created=datetime.fromtimestamp(stat.st_ctime).isoformat(),
            modified=datetime.fromtimestamp(stat.st_mtime).isoformat()
        )
        file_infos.append(file_info)
        print(f"📝 Собрано: {fname}")
    return file_infos

def serialize_to_json(file_infos):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump([f.to_dict() for f in file_infos], f, indent=4, ensure_ascii=False)
    print(f"\n✅ Сериализация завершена: {OUTPUT_FILE}")

def deserialize_from_json():
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [FileInfo.from_dict(item) for item in data]


if __name__ == "__main__":
    file_info_list = collect_file_info()
    serialize_to_json(file_info_list)

    print("\n🔄 Проверка десериализации...")
    deserialized = deserialize_from_json()
    for file_info in deserialized:
        print(f"{file_info.name} | {file_info.size} байт | {file_info.modified}")