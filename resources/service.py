#!/usr/bin/env python
# -*- coding: utf-8 -*-
# shadowsocks service

from __future__ import absolute_import, division, print_function, \
    with_statement

import sys
import os
import logging
import xbmcaddon

from shadowsocks import eventloop, tcprelay, udprelay, asyncdns

config = {
    'log-file': '/var/log/shadowsocks.log',
    'verbose': False,
    'tunnel_remote_port': 53,
    'libmbedtls': None,
    'tunnel_port': 53,
    'local_port': 1080,
    'workers': 1,
    'fast_open': False,
    'server_port': 8388,
    'local_address': '127.0.0.1',
    'method': 'aes-256-cfb',
    'libsodium': None,
    'tunnel_remote': '8.8.8.8',
    'crypto_path': {
        'mbedtls': None,
        'openssl': None,
        'sodium': None
    },
    'password': '',
    'libopenssl': None,
    'dns_server': None,
    'prefer_ipv6': False,
    'port_password': None,
    'server': 'bash.pub',
    'timeout': 300,
    'one_time_auth': False
}

def check_python():
    info = sys.version_info
    if info[0] == 2 and not info[1] >= 6:
        print('Python 2.6+ required')
        sys.exit(1)
    elif info[0] == 3 and not info[1] >= 3:
        print('Python 3.3+ required')
        sys.exit(1)
    elif info[0] not in [2, 3]:
        print('Python version not supported')
        sys.exit(1)

def run():
    check_python()

    # fix py2exe
    # in fact, i don't think this may run on windows
    if hasattr(sys, "frozen") and sys.frozen in \
            ("windows_exe", "console_exe"):
        p = os.path.dirname(os.path.abspath(sys.executable))
        os.chdir(p)

    addon = xbmcaddon.Addon()
    config['server'] = addon.getSetting('server_addr')
    config['server_port'] = int(addon.getSetting('server_port'))
    config['method'] = addon.getSetting('method')
    config['password'] = addon.getSetting('password')
    config['local_address'] = addon.getSetting('local_addr')
    config['local_port'] = int(addon.getSetting('local_port'))
    config['timeout'] = int(addon.getSetting('timeout'))
    config['one_time_auto'] = addon.getSetting('one_time_auto') == 'True'
    config['fast_open'] = addon.getSetting('tcp_fast_open') == 'True'

    if config['server'] == '':
        logging.error('No SERVER_ADDR specified')
        sys.exit(1)

    logging.info("starting local at %s:%d" %
                 (config['local_address'], config['local_port']))

    dns_resolver = asyncdns.DNSResolver()
    tcp_server = tcprelay.TCPRelay(config, dns_resolver, True)
    udp_server = udprelay.UDPRelay(config, dns_resolver, True)
    loop = eventloop.EventLoop()
    dns_resolver.add_to_loop(loop)
    tcp_server.add_to_loop(loop)
    udp_server.add_to_loop(loop)

    loop.run()

