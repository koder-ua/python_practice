#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
Homework for Automatic Number Identification (ANI)
https://github.com/koder-ua/python-classes/blob/master/slides/pdf/FF_tasks.pdf
Slide #7
"""


def decode(string):
    """
    ANI decoder:
    - combine repeated characters (2333# -> 3)
    - remove single characters (1234 -> None)
    - repeat last character before "##"  (33## -> 33")

    :param string: string
    :return string: processed string
    """
    # split all repeated symbols as a standalone strings
    # string = ["".join(grp) for _, grp in itertools.groupby(string)]
    splitted_string = []
    n = 0
    k = 0
    while n < len(string):
        while k < len(string) - 1:
            if string[k] == string[k + 1]:
                k += 1
            else:
                break
        k += 1
        splitted_string.append(string[n:k])
        n = k
    # get first character from splitted strings + remove single-length strings
    string = "".join([i[0] for i in splitted_string if len(i) != 1])
    result = ""
    for i, v in enumerate(string):
        if v == "#":
            if i == 0 and len(string) > 1:  # checking leading '#' in string
                continue
            elif i == 0:
                return None
            else:
                result += string[i - 1]
        else:
            result += string[i]
    return result


def test_decode():
    assert decode("") == ""
    assert decode("1") == ""
    assert decode("11111") == "1"
    assert decode("11#") == "1"
    assert decode("11##") == "11"
    assert decode("11122234###55") == "1225"
    assert decode("##") is None
    assert decode("12345##") is None
    assert decode("221133444##") == "21344"
    assert decode("###33###22##") == "3322"
    assert decode("###33###22##1#") == "3322"

    print("Passed successfully")


def main():
    "main"
    test_decode()
    return 0


if __name__ == "__main__":
    exit(main())
