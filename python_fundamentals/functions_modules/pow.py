#!/usr/bin/env python3


def pow(a, b):
    if b < 0:
        denominator = 1
        for _ in range(-b):
            denominator *= a
        return 1.0 / denominator

    result = 1
    for _ in range(b):
        result *= a
    return result
    