#!/usr/bin/python

import sys


def main():
    total_chunk = 0
    total_mean = 0
    total_var = 0
    for line in sys.stdin:
        chunk, mean, var = line.strip().split()
        chunk = int(chunk_size)
        mean = float(mean)
        var = float(var)
        total_mean = (total_chunk * total_mean + chunk_size * mean) / (total_chunk + chunk_size)
        total_var = (total_chunk * total_var + chunk_size * var) / (total_chunk + chunk_size) + total_chunk * chunk_size * ((total_mean - mean) / (total_chunk_size + chunk_size)) ** 2
        total_chunk += chunk_size
    print(f'size = {total_chunk}, mean = {total_mean}')


if __name__ == "__main__":
    main()