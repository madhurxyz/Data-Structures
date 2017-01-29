#!python

import string


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    new_text = text.replace(" ", "").lower()
    delete = '!()-[]{};:"\,<>./?@#$%^&*_~\x80\x98\x99\x94\''
    letters = ''
    for letter in new_text:
        if letter not in delete:
            letters += letter

    left = 0
    right = len(letters)-1
    while left<=right:
        if letters[left] == letters[right]:
            left = left + 1
            right = right - 1
        else:
            return False
    return True


def is_palindrome_recursive(text, left=None, right=None):
    new_text = text.replace(" ", "").lower()
    delete = '!()-[]{};:"\,<>./?@#$%^&*_~\x80\x98\x99\x94\''
    letters = ''
    for letter in new_text:
        if letter not in delete:
            letters += letter

    if left is None and right is None:
        left = 0
        right = len(letters)-1

    if len(letters) <= 1:
        return True

    if left < right:
        if letters[left] == letters[right]:
            return True
        else:
            return is_palindrome_recursive(letters, left + 1, right - 1)

    return False

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
