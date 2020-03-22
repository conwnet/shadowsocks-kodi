#!/usr/bin/env python
# -*- coding: utf-8 -*-
# helpers

import xbmcaddon

default_config = {
    'log-file': '/tmp/shadowsocks.log',
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
    'pid-file': '/tmp/shadowsocks.pid',
    'password': '',
    'libopenssl': None,
    'dns_server': None,
    'prefer_ipv6': False,
    'port_password': None,
    'server': '',
    'timeout': 300,
    'one_time_auth': False
}

def get_config():
    config = default_config.copy()

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

    return config

