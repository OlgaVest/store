def validate_book_data(data):
    required_fields = ['title', 'author', 'genre']
    if not isinstance(data, dict):
        return False
    for field in required_fields:
        if field not in data or not isinstance(data[field], str) or not data[field].strip():
            return False
    return True
