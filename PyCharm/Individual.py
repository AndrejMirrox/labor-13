#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys


def summator(*a):
    if a:
        min_i = a.index(min(a))
        if min_i != len(a)-1:
            return math.fsum(a[min_i+1:])
        else:
            return None
    else:
        return None


if __name__ == "__main__":
    answer = summator(42, 15, 33, 10, 12, 12)
    if answer is None:
        print(f"Невозможно вычислить", file=sys.stderr)
    else:
        print(f"Сумма аргуметов после мин.: {answer}")
