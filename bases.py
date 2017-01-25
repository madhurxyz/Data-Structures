#!python

import string

def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    assert 2 <= base <= 36

    length = len(str_num)
    decode_sum = 0
    for i in range(0,length):
        int_num = int(str_num[i])
        conversion = base**(length - i - 1)
        decode_num = int_num*conversion
        decode_sum += decode_num

    return decode_sum

def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    assert 2 <= base <= 36

    remainder_str = ""
    stop = False
    while stop is False:
        remainder = num%base
        remainder_str += str(remainder)
        num = num/base
        if num is 0:
            stop = True

    #reverses remainder string
    e = remainder_str[::-1]
    print e
    return e

def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """
    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36

    d = decode(str_num, base1)
    e = encode(d, base2)



def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        str_num = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        result = convert(str_num, base1, base2)
        print('{} in base {} is {} in base {}'.format(str_num, base1, result, base2))
    else:
        print('Usage: {} number base1 base2'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
