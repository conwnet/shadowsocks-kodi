#!/usr/bin/env python
# -*- coding: utf-8 -*-
# shadowsocks service

from __future__ import absolute_import, division, print_function, \
    with_statement

import sys
import os
import logging

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))
from shadowsocks import shell, eventloop, tcprelay, udprelay, asyncdns

@shell.exception_handle(self_=False, exit_code=1)
def run(config):
    shell.check_python()

    # fix py2exe
    if hasattr(sys, "frozen") and sys.frozen in \
            ("windows_exe", "console_exe"):
        p = os.path.dirname(os.path.abspath(sys.executable))
        os.chdir(p)

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

