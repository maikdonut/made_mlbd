#!/usr/bin/python

import sys
import csv


CHUNK = 50


def read_input(file):
    reader = csv.reader(file, delimiter=',')
    next(reader, None)
    ind = 1
    prices = []
    for price in reader:
        try:
            if ind < CHUNK:
                prices.append(float(price[0]))
                ind += 1
            else:
                yield prices + [float(price[0])]
                ind = 1
                prices.clear()
        except ValueError:
            continue
    yield prices


def main():
    data = read_input(sys.stdin)
    for prices in data:
        if len(prices):
            print(len(prices), prices.mean(), prices.var(), sep=' ')


if __name__ == "__main__":
    main()
