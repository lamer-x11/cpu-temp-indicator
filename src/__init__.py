#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import gtk
from indicator import Indicator
from state import State
from temperature import GetTemperatureCommand

class TempNotificator:
    # Daemonizes the process
    def deamonize(self):

        self.fork()

        os.chdir('/')
        os.setsid()
        os.umask(0)

        self.fork()

        nullfile = getattr(os, 'devnull', '/dev/null')

        sys.stdout.flush()
        sys.stderr.flush()
        null = open(nullfile, 'r')
        os.dup2(null.fileno(), sys.stdin.fileno())

    # Forks the process
    def fork(self):
        try:
            pid = os.fork()
            if pid > 0:
                os._exit(0)
        except OSError:
            return

    # Starts the indicator
    def start(self):
        indicator = Indicator()
        command = GetTemperatureCommand()
        state = State()

        state.setCommand(command)
        indicator.setState(state)

        indicator.start()
        gtk.main()

# init
def main():
    notificator = TempNotificator()
    notificator.deamonize()
    notificator.start()
