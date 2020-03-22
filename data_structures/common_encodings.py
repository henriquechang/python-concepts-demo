from array import array


def bytes_from_array(my_array: []):
    numbers = array('h', my_array)
    octets = bytes(numbers)
    return octets


def encode_decode(text: str, encode, decode):
    b = text.encode(encode)
    return b.decode(decode)
