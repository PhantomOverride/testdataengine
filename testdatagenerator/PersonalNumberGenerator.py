#!/usr/bin/env python
# -*- coding: utf-8 -*-

from testdatagenerator.Utilities import luhn
from faker import Faker
from random import randint
try:
    from burp import IBurpExtender                          # Required for all extensions
    from burp import IIntruderPayloadGeneratorFactory       # For burp intruder payload generation
    from burp import IIntruderPayloadProcessor              # For burp intruder payload generation
    from burp import IIntruderPayloadGenerator              # For burp intruder payload generation
    __burp = True
    import sys                                              # Used to write exceptions for exceptions_fix.py debugging
except ImportError:
    __burp = False
try:                                                    # Try to load, not required
    from exceptions_fix import FixBurpExceptions        # Used to make the error messages easier to debug
except ImportError:
    pass


class PersonalNumberGenerator:
    def __init__(self):
        self.faker = Faker()

    def pnr(self):
        date = self.faker.date_time()
        pnr = date.strftime("%y%m%d-")
        pnr += str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
        return pnr + str(luhn(pnr))

    def generator(self):
        return self.pnr()

######################## Burp Intruder Code ##############################
if __burp:
    class BurpExtender(IBurpExtender, IIntruderPayloadGeneratorFactory, IIntruderPayloadProcessor):
        ''' Implements IBurpExtender for hook into burp and inherit base classes.
            This tool will generate 1000 personal numbers for burp
        '''
        def registerExtenderCallbacks(self, callbacks):

            # required for debugger: https://github.com/securityMB/burp-exceptions
            sys.stdout = callbacks.getStdout()

            # keep a reference to our callbacks object
            self._callbacks = callbacks

            # obtain an extension helpers object
            # This method is used to obtain an IExtensionHelpers object, which can be used by the extension to perform numerous useful tasks
            self._helpers = callbacks.getHelpers()

            # set our extension name
            callbacks.setExtensionName("Intruder PersonalNumber")

            # register ourselves as a message editor tab factory
            callbacks.registerIntruderPayloadGeneratorFactory(self)

            return

        def getGeneratorName(self):
            return "1000 Personal Numbers"

        def createNewInstance(self, attack):
            # return a new IIntruderPayloadGenerator to generate payloads for this attack
            return IntruderPayloadGenerator()

        #
        # implement IIntruderPayloadProcessor
        #

        def getProcessorName(self):
            return "Serialized input wrapper"

        def processPayload(self, currentPayload, originalPayload, baseValue):
            # decode the base value
            dataParameter = self._helpers.bytesToString(
                    self._helpers.base64Decode(self._helpers.urlDecode(baseValue)))

            # parse the location of the input string in the decoded data
            start = dataParameter.index("input=") + 6
            if start == -1:
                return currentPayload

            prefix = dataParameter[0:start]
            end = dataParameter.index("&", start)
            if end == -1:
                end = len(dataParameter)

            suffix = dataParameter[end:len(dataParameter)]

            # rebuild the serialized data with the new payload
            dataParameter = prefix + self._helpers.bytesToString(currentPayload) + suffix
            return self._helpers.stringToBytes(
                    self._helpers.urlEncode(self._helpers.base64Encode(dataParameter)))

    class IntruderPayloadGenerator(IIntruderPayloadGenerator):
        def __init__(self):
            self._pnr = PersonalNumberGenerator()
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
    except:
        pass
