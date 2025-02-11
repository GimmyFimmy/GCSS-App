def decode(data: bytes):
    # decode 'data: bytes'
    return data.decode('utf-8').split('_')

def encode(data: [str], gesture: str):
    # check if 'str' type received
    assert(type(gesture) is str)

    # create new variable
    keys = ""

    # go through 'data'
    for line in data[3:]:
        # split 'line: str' on 'key: str' and 'value: str'
        key, value = line.split('=')

        # check if 'value: str' exists
        if value == gesture:
            # add 'key: str'
            keys += key + "_"

    # encode 'keys: str'
    return keys.encode('utf-8')