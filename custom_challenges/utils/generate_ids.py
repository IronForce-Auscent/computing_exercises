import hashlib, datetime

def generate_id(challenge_name):
    time_of_creation = datetime.datetime.now)
    string_to_hash = challenge_name + str(time_of_creation)
    hashed_string = hashlib.sha256(string_to_hash.encode()).hexdigest()
    unique_id = hashed_string[:16]
    return unique_id