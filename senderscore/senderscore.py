#!/usr/bin/env python3

from argparse import ArgumentParser
import socket

def get_senderscore(ip):
    '''Retrieve the score of a IP from Sender Score aplication'''

    try:
        socket.inet_aton(ip)
    except OSError:
        print('Error: Not a valid IP')
        return

    tmp = ip.split('.')
    backwards = '{}.{}.{}.{}'.format(tmp[3], tmp[2], tmp[1], tmp[0])
    replists = ['score.senderscore.com']
    lookup_results = {}

    for rl in replists:
        host = '{}.{}'.format(backwards, rl)
        try:
            ret = socket.gethostbyname(host)
        except socket.gaierror as e:
            print('Error: No score found')
            return
        else:
            if ret:
                lookup_results[rl] = ret

    scores = {}

    for k in lookup_results.keys():
        v = lookup_results[k].split('.')[3]
        scores[k] = v

    return scores

parser = ArgumentParser(prog='Sender Score Lookup',
                        description='Retrieve the score of a IP from Sender Score aplication.',
                        fromfile_prefix_chars='@',
                        argument_default='s')

parser.add_argument('ip', action='store', help='IP to be tested by Sender Score')


def main():
    args = parser.parse_args()

    score = get_senderscore(args.ip)

    if score:
        print('{} has senderscore {}'.format(args.ip, score['score.senderscore.com']))


if __name__ == '__main__':
    main()
