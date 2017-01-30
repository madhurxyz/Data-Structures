#!python

def in_string(super_str, sub_str):
    assert isinstance(super_str, str)
    assert isinstance(sub_str, str)

    return in_string_iterative(super_str, sub_str)
    # return in_string_recursive(super_str, sub_str)

def clean(string):
    new_str = string.lower().replace(' ', '')
    delete = '!()-[]{};:"\,<>./?@#$%^&*_~\x80\x98\x99\x94\''
    clean_str = ''
    for letter in new_str:
        if letter not in delete:
            clean_str += letter
    return clean_str


def in_string_iterative(super_str, sub_str):
    sp_str = clean(super_str)
    sb_str = clean(sub_str)
    sp_len = len(sp_str)
    sb_len = len(sb_str)
    first = 0
    last = sb_len
    check_str = ""
    while last <= sp_len:
        for sub_index in range(first, last):
            check_str = sp_str[first:last]
        if check_str == sb_str:
            return True
        else:
            first += 1
            last += 1
    return False

def in_string_recursive(super_str, sub_str):
    return True

def main():
    import sys
    if len(sys.argv) > 1:
        super_str = sys.argv[1]
        args = sys.argv[2:]
        if len(args) > 0:
            for arg in args:
                in_str = in_string(super_str, arg)
                result = 'PASS' if in_str else 'FAIL'
                str_in = 'in' if in_str else 'not in'
                print('{}: {} is {} {}'.format(result, repr(arg), str_in, repr(super_str)))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('The program checks if string2..stringN are sub strings of string1')

if __name__ == '__main__':
    main()
