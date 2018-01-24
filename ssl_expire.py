#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import socket
import ssl
import datetime


def check_hostname(hostname):
    """Check hostname."""
    try:
        socket.gethostbyname(hostname)
        return True
    except socket.error:
        return False


def ssl_match_hostname(certinfo, hostname):
    """Return True if valid. False is invalid."""
    if 'subjectAltName' in certinfo:
        for typ, val in certinfo['subjectAltName']:
            if typ == 'DNS' and val == hostname:
                return True
            else:
                return False
    else:
        return False


def ssl_expire_days(hostname, portnum):
    """Get the number of days left in a cert's lifetime."""
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
    try:
        ctx = ssl.create_default_context()
        ctx.options &= ~ssl.OP_NO_SSLv3
        conn = ctx.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
        conn.settimeout(2.0)
        conn.connect((hostname, portnum))
    except ssl.SSLError:
        return False

    ssl_info = conn.getpeercert()
    if ssl_match_hostname(ssl_info, hostname):
        expire_in = datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt) - datetime.datetime.utcnow()
        return expire_in.days
    else:
        return False


def main():
    """Invoke Argparse if connection available."""
    parser = argparse.ArgumentParser()
    parser.add_argument('host', help='Specify an host to connect to.')
    parser.add_argument('-p', '--port', help='Specify a port to connect to.', type=int, default=443)
    args = parser.parse_args()

    host = args.host
    port = args.port

    if check_hostname(host):
        left = ssl_expire_days(host, port)
        print(left)

if __name__ == '__main__':
    main()
