#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import re

class GetTemperatureCommand:
    # Executes the command
    def execute(self):
        sensorData = self.getSensorData()
        sensorData = self.format(sensorData)

        return sensorData

    # Runs shell command via suprocess
    def getSensorData(self):
        sensorsCmd = subprocess.Popen('sensors', shell=False, stdout=subprocess.PIPE)
        sensorsGrep = subprocess.Popen(['grep', 'Core'], shell=False, stdin=sensorsCmd.stdout, stdout=subprocess.PIPE).stdout.read()

        return sensorsGrep

    # Formats input data and returns it as a list
    def format(self, data):
        dataString = re.sub(r'\s{2,}', ' ', data)
        rawValues = re.findall(r'(?<=:\s\+).*?(?=°)', dataString)

        rawValues = [int(float(value)) for value in rawValues]

        return {'string': dataString.strip(), 'values': rawValues}
