#!/usr/bin/env python3

from argparse import ArgumentParser
import socket
import sys
import os


def is_valid_ip(ip: str):
    '''Validate the syntax of a IP.'''

    try:
        octets = ip.split('.')
        if not len(octets) == 4:
            return False

        socket.inet_aton(ip)
    except OSError:
        return False

    return True


def get_score(ip):
    '''Retrieve the score of a IP from Sender Score aplication.'''

    ip = ip.split('.')
    backwards = '{}.{}.{}.{}'.format(*list(reversed(ip)))
    rdns = '{}.{}'.format(backwards, 'score.senderscore.com')

    try:
        host = socket.gethostbyname(rdns)
    except socket.gaierror:
        return ''

    score = host.split('.')[3]

    return score


def cli(ip):
    '''Command line interface resolution'''

    if not is_valid_ip(ip):
        print('Error: Not a valid IP', file=sys.stderr)
        os.sys.exit(65)

    score = get_score(ip)

    if score:
        print('{} has senderscore {}'.format(ip, score))
    else:
        print('Error: No score found', file=sys.stderr)
        os.sys.exit(69)


def config_parser():
    '''Creates the parser object'''

    parser = ArgumentParser(prog='Sender Score Lookup',
                            description='Retrieve the score of a IP from Sender Score.',
                            fromfile_prefix_chars='@',
                            argument_default='s')

    parser.add_argument('ip',
                        action='store',
                        help='IP to be tested')

    return parser


def main():
    parser = config_parser()
    args = parser.parse_args()
    cli(args.ip)


if __name__ == '__main__':
    main()
