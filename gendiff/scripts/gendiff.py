#!/usr/bin/env python3
import argparse
from gendiff.gendiff_func.generate_differece import generate_diff


def info():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        default='stylish',
                        type=str)
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


def main():
    info()


if __name__ == '__main__':
    main()
