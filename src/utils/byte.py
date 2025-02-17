def decode(data: bytes):
    # decode 'data: bytes'
    return data.decode('utf-8').split('_')

def encode(data: str):
    # check if 'str' type received
    assert(type(data) is str)

    # create new variable
    length = len(data)

    if length < 10:
        data += '-' * (10 - length)

    return bytes(data, 'utf-8')