def encode_sixteen(remainder):
    if remainder is 10:
        remainder = "a"
    if remainder is 11:
        remainder = "b"
    if remainder is 12:
        remainder = "c"
    if remainder is 13:
        remainder = "d"
    if remainder is 14:
        remainder = "e"
    if remainder is 15:
        remainder = "f"
    return remainder

def decode_sixteen(num):
    if num is "a":
        num = 10
    if num is "b":
        num = 11
    if num is "c":
        num = 12
    if num is "d":
        num = 13
    if num is "e":
        num = 14
    if num is "f":
        num = 15
    return num
