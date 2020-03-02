#!/usr/bin/env python3

from argparse import ArgumentParser
import socket
import sys
import os


def validade_ip(ip):
    try:
        socket.inet_aton(ip)
    except OSError:
        print('Error: Not a valid IP', file=sys.stderr)
        os.sys.exit(1)


def get_senderscore(ip):
    '''Retrieve the score of a IP from Sender Score aplication'''

    validade_ip(ip)

    ip = ip.split('.')
    backwards = '{}.{}.{}.{}'.format(*list(reversed(ip)))
    rdns = '{}.{}'.format(backwards, 'score.senderscore.com')

    try:
        host = socket.gethostbyname(rdns)
    except socket.gaierror:
        print('Error: No score found', file=sys.stderr)
        os.sys.exit(1)

    reputation = host.split('.')[3]

    return reputation


def main():
    args = parser.parse_args()

    score = get_senderscore(args.ip)

    if score:
        print('{} has senderscore {}'.format(args.ip, score))


parser = ArgumentParser(prog='Sender Score Lookup',
                        description='Retrieve the score from Sender Score.',
                        fromfile_prefix_chars='@',
                        argument_default='s')

parser.add_argument('ip',
                    action='store',
                    help='IP to be tested by Sender Score')

if __name__ == '__main__':
    main()
