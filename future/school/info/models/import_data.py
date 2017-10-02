# -*- coding: utf-8 -*-

from .teachers import Teachers


def main():
    data_source = [
        {'name': 'A'},
        {'name': 'B'},
        {'name': 'C'},
        {'name': 'D'},
        {'name': 'E'}
    ]
    for data_dict in data_source:
        Teachers.create(**data_dict)
    return 'ok'


if __name__ == '__main__':
    main()
