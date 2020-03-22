#!/usr/bin/env python
# -*- coding: utf-8 -*-
# run service

from src import service, async_task, helpers
import logging
import xbmc

# set logging to xbmc.log
def set_logging():
    class Handler(logging.Handler):
        def __init__(self):
            logging.Handler.__init__(self)
        def emit(self, record):
            message = self.format(record)
            xbmc.log(message, level=xbmc.LOGNOTICE)

    logger = logging.getLogger()
    logger.addHandler(Handler())

if __name__ == '__main__':
    set_logging()
    config = helpers.get_config()

    def run_service():
        if not config['server']:
            return
        service.run(config)

    task = async_task.AsyncTask(run_service, config['pid-file'])

    # try stop existing process,
    # on normal case it not required
    task.stop()
    task.start()

    monitor = xbmc.Monitor()
    while not monitor.abortRequested():
        if monitor.waitForAbort(10):
            task.stop()
            break
