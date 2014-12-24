#!/usr/bin/env python
# -*- coding: utf-8 -*-

class State:
    STATE_NORMAL = 0
    STATE_WARNING = 1
    STATE_CRITICAL = 2
    THRESHOLD_WARNING = 65
    THRESHOLD_CRITICAL = 80

    def __init__(self):
        self.state = self.STATE_NORMAL
        self.stateMessage = None
        self.command = None
    
    # Returns current state as array
    def getState(self):
        self.update()
        return {'state': self.state, 'message': self.message}

    # Sets the command object
    def setCommand(self, command):
        self.command = command

    # Updates current state
    def update(self):
        data = self.command.execute()

        self.message = data['string']

        values = []

        for value in data['values']:
            values.append(value)

        maxValue = max(values)

        if maxValue >= self.THRESHOLD_CRITICAL:
            self.state = self.STATE_CRITICAL 
            return

        if maxValue >= self.THRESHOLD_WARNING:
            self.state = self.STATE_WARNING 
            return

        self.state = self.STATE_NORMAL
        return
