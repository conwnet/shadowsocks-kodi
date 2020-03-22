#!/usr/bin/env python
# -*- coding: utf-8 -*-
# run async task

import random
import time
import os
import logging
import signal

class AsyncTask:
    def __init__(self, task, pid_file = None):
        self.pid_file = pid_file
        if not pid_file:
            unique_id = str(int(time.time() * 10000))
            self.pid_file = '/tmp/async-task-' + unique_id + '.pid'
        self.task = task

    def start(self):
        pid = os.fork()
        assert pid != -1

        # main process record process pid
        if pid > 0:
            with open(self.pid_file, 'w') as f:
                f.write(str(pid))
                f.close()

        # child process run task
        if pid == 0:
            self.task()
            try:
                os.unlink(self.pid_file)
            except:
                return

    def stop(self):
        try:
            with open(self.pid_file, 'r') as f:
                pid = int(f.read())
                os.kill(pid, signal.SIGKILL)
                os.unlink(self.pid_file)
        except:
            logging.error('stop task failed')
