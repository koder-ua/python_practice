#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
Homework for Gnome Sort
https://github.com/koder-ua/python-classes/blob/master/slides/pdf/FF_tasks.pdf
Slide #9
"""


def gnome_sort(array):
    """
    Gnome sort implementation

    :param array: list of int
    """
    i = 0
    while i < len(array)-1:
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            if i != 0:
                i -= 1
        else:
            i += 1
    return array


def test_gnome_sort():
    assert gnome_sort([3, 1, 2]) == [1, 2, 3]
    assert gnome_sort([5, 4, 7, 8, 23, 13, 9]) == [4, 5, 7, 8, 9, 13, 23]
    assert gnome_sort([-4, -1, 5, 3, 0, 2]) == [-4, -1, 0, 2, 3, 5]
    assert gnome_sort([10, -2, 6, 2, 2, 1]) == [-2, 1, 2, 2, 6, 10]
    assert gnome_sort([1]) == [1]
    assert gnome_sort([9, 8, 7, 6, 5, 4, 0, -1]) == [-1, 0, 4, 5, 6, 7, 8, 9]
    assert gnome_sort([]) == []

    print("Passed successfully")


def main():
    "main"
    test_gnome_sort()
    return 0


if __name__ == "__main__":
    exit(main())
