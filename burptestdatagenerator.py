#!/usr/bin/env python
# -*- coding: utf-8 -*-

from burp import IBurpExtender                          # Required for all extensions
from burp import IIntruderPayloadGeneratorFactory       # For burp intruder payload generation
from burp import IIntruderPayloadProcessor              # For burp intruder payload generation
from burp import IIntruderPayloadGenerator              # For burp intruder payload generation
import sys                                              # Used to write exceptions for exceptions_fix.py debugging
try:                                                    # Try to load, not required
    from exceptions_fix import FixBurpExceptions        # Used to make the error messages easier to debug
except ImportError:
    pass
from testdatagenerator import PersonalNumberGenerator


class BurpExtender(IBurpExtender):
    def registerExtenderCallbacks(self, callbacks):
        # required for debugger: https://github.com/securityMB/burp-exceptions
        sys.stdout = callbacks.getStdout()

        # keep a reference to our callbacks object
        self._callbacks = callbacks

        # obtain an extension helpers object
        # This method is used to obtain an IExtensionHelpers object, which can be used by the extension to perform numerous useful tasks
        self._helpers = callbacks.getHelpers()

        # set our extension name
        callbacks.setExtensionName("TestDataEngine")

        # register the IntruderPayloadFactory
        callbacks.registerIntruderPayloadGeneratorFactory(IntruderPayloadGeneratorFactory('PNR-'))
        callbacks.registerIntruderPayloadGeneratorFactory(IntruderPayloadGeneratorFactory('PNR'))

        return


class IntruderPayloadGeneratorFactory(IIntruderPayloadGeneratorFactory):
    '''
        
    '''
    def __init__(self, generatorType):
        if generatorType == 'PNR-':
            self.generatorDescriptor = "1000 Personal Numbers (YYYYMMDD-XXXX)"
            self.generatorClass = PnrIntruderPayloadGenerator
            self._dashSeparator = True
        elif generatorType == 'PNR':
            self.generatorDescriptor = "1000 Personal Numbers (YYYYMMDDXXXX)"
            self.generatorClass = PnrIntruderPayloadGenerator
            self._dashSeparator = False
        else:
            raise ValueError

    def getGeneratorName(self):
        return self.generatorDescriptor

    def createNewInstance(self, attack):
        # return a new IIntruderPayloadGenerator to generate payloads for this attack
        if self.generatorClass == PnrIntruderPayloadGenerator:
            return self.generatorClass(self._dashSeparator)
        else:
            return self.generatorClass()


class PnrIntruderPayloadGenerator(IIntruderPayloadGenerator):
    def __init__(self, dashSeparator=True):
        self._pnr = PersonalNumberGenerator.PersonalNumberGenerator(dashSeparator)
        self._reported = []

    def hasMorePayloads(self):
        # Will  generate 1000 Personal Numbers
        return len(self._reported) < 1000

    def getNextPayload(self, baseValue):
        while True:
            current = self._pnr.generator()
            if current in self._reported:
                continue
            else:
                self._reported.append(current)
                return current

    def reset(self):
        self._reported = []


try:
    FixBurpExceptions()
except NameError:
    pass
