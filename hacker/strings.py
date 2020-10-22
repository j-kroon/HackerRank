import textwrap


def wrap(string, max_width):
    string_list = textwrap.wrap(string, max_width)
    paragraph = '\n'.join(string_list)
    return paragraph


def doormat(n, m):
    """
    Mat size must be n * m. ( is an odd natural number, and  is  times .)
    The design should have 'WELCOME' written in the center.
    The design pattern should only use |, . and - characters.
    :param m:
    :param n:
    :return:
    """
    pad = '-'
    filler = '.|.'
    middle = 'WELCOME'
    mat = []
    mid = middle.center(m, pad)
    error = 'Oops, try again!'

    try:
        for width in range(1, n, 2):
            mat.append((filler*width).center(m, pad))
        end = list(reversed(mat))
        mat.append(mid)
        mat = mat + end
        return '\n'.join(mat)
    except TypeError:
        return error


def print_formatted(number):
    """
    Given an integer, n, print the following values for each integer i from 1 to n:
    1. Decimal
    2. Octal
    3. Hexadecimal (capitalized)
    4. Binary
    The four values must be printed on a single line in the order specified above for each i from 1 to n. Each value
    should be space-padded to match the width of the binary value of n.
    :param number:
    :return:
    """
    # your code goes here
    # your code goes here
    result = []
    pad = len(f'{number:b}') + 1
    for i in range(1, number+1):
        plain = str(i).rjust(pad-1)
        octal = f'{i:o}'.rjust(pad)
        hexi = f'{i:X}'.rjust(pad)
        binary = f'{i:b}'.rjust(pad)
        row = plain + octal + hexi + binary
        result.append(row)
        print(row)
    return '\n'.join(result)


def rangoli(n):
    """
    You are given an integer, N. Your task is to print an alphabet rangoli of size N (Rangoli is a form of Indian folk
    art based on creation of patterns). The center of the rangoli has the first alphabet letter a, and the boundary has
    the  alphabet letter (in alphabetical order).

    :param n:
    :return:
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    return
