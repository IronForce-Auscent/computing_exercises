import hashlib, datetime

def generate_id(file_name):
    current_datetime = datetime.datetime.now()
    string_to_hash = file_name + current_datetime
    hashed_id = hashlib.sha256(string_to_hash.encode())
    return hashed_id[:16]