from secrets import choice

def generate_alphabet():
    lowercase_list, uppercase_list = [], []
    lowercase_string, uppercase_string = "", ""
    for l in range(97, 122):
        lowercase_string += chr(l)
        lowercase_list.append(chr(l))
    for u in range(65, 90):
        uppercase_string += chr(u)
        uppercase_list.append(chr(u))
    response = {
        'list-format': {
            'lowercase': lowercase_list,
            'uppercase': uppercase_list
        },
        'string-format': {
            'lowercase': lowercase_string,
            'uppercase': uppercase_string
        }
    }
    return response


def generate_random_string(string_len: int):
    selection = generate_alphabet()
    pass