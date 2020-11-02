import textwrap
import string


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

    3
    lines is 5 = 2n-1
    pad is 9 = (2n-1)+(2n-2) -> 4n-3
    ----c----
    --c-b-c--
    c-b-a-b-c
    --c-b-c--
    ----c----
    """
    alphabet = string.ascii_lowercase
    pad = 4*n-3
    filler = '-'
    initial = [alphabet[n-1]]
    top = [alphabet[n-1].center(pad, filler)]

    for i in range(n-2, -1, -1):
        initial.append(alphabet[i])
        sub_list = initial[:-1]+[alphabet[i]]+list(reversed(initial[:-1]))
        sub_seq = filler.join(sub_list).center(pad, filler)
        top.append(sub_seq)

    bot = list(reversed(top[:-1]))
    result = '\n'.join(top + bot)
    print(result)
    return


def capitalize(s):
    s = string.capwords(s, ' ')
    return s


def minion_game(s):
    """
    Kevin and Stuart want to play the 'The Minion Game'.

    Game Rules

    Both players are given the same string, S.
    Both players have to make substrings using the letters of the string S.
    Stuart has to make words starting with consonants.
    Kevin has to make words starting with vowels.
    The game ends when both players have made all possible substrings.

    Scoring
    A player gets +1 point for each occurrence of the substring in the string S.

    For Example:
    String S = BANANA
    Kevin's vowel beginning word = ANA
    Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

    Your task is to determine the winner of the game and their score.

    Output Format
    Print one line: the name of the winner and their score separated by a space.
    If the game is a draw, print Draw.
    """
    # your code goes here
    return
