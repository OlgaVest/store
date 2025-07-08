import json
import os
from jsonschema import validate, ValidationError, SchemaError

BASE_DIR = os.getcwd()
DATA_FILE = os.path.join(BASE_DIR, "output", "file_info.json")
SCHEMA_FILE = os.path.join(BASE_DIR, "schemas", "file_info_schema.json")

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema)
        print("✅ Данные соответствуют JSON Schema!")
    except ValidationError as e:
        print("❌ Ошибка валидации:")
        print(f"  - {e.message}")
        print(f"  - Путь: {'.'.join(map(str, e.path))}")
    except SchemaError as e:
        print("❌ Ошибка схемы:")
        print(e)

if __name__ == "__main__":
    json_data = load_json(DATA_FILE)
    schema = load_json(SCHEMA_FILE)
    validate_json(json_data, schema)