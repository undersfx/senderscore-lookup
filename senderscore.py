#!/usr/bin/env python3

import socket

def get_senderscore(ip):
    '''Retrieve the score of a IP from SenderScore aplication'''

    try:
        socket.inet_aton(ip)
    except OSError:
        print('Not a valid IP.')
        return

    tmp = ip.split('.')
    backwards = '{}.{}.{}.{}'.format(tmp[3], tmp[2], tmp[1], tmp[0])
    replists = ['score.senderscore.com']
    lookup_results = {}

    for rl in replists:
        host = '{}.{}'.format(backwards, rl)
        ret = socket.gethostbyname(host)
        if ret:
            lookup_results[rl] = ret

    scores = {}

    for k in lookup_results.keys():
        v = lookup_results[k].split('.')[3]
        scores[k] = v

    return scores

if __name__ == '__main__':
    # TODO: argparse/sys.args
