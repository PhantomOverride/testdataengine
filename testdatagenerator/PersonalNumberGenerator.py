#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        pass

    def pnr(self):
        year = str(randint(0, 99))
        month = str(randint(1, 12))
        day = str(randint(1, 28))
        pnr = year.zfill(2) + month.zfill(2) + day.zfill(2) + "-"
        pnr += str(randint(0, 999)).zfill(3)

        sum = 0
        odd = False
        for s in pnr:
            if s == "-":
                continue
            odd = not odd
            if odd:
                temp = str(int(s) * 2)
                for i in temp:
                    sum += int(i)
            else:
                sum += int(s)
        sum = str(sum)
        luhn = int(sum[len(sum) - 1])
        luhn = luhn if luhn == 0 else 10 - luhn
        pnr = ("19" if int(year) > 18 else "20") + pnr
        return pnr + str(luhn)

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
            callbacks.setExtensionName("Intruder PersonalNumberGenerator")

            # register ourselves as a message editor tab factory
            callbacks.registerIntruderPayloadGeneratorFactory(self)

            return

        def getGeneratorName(self):
            return "1000 Personal Numbers"

        def createNewInstance(self, attack):
            # return a new IIntruderPayloadGenerator to generate payloads for this attack
            return IntruderPayloadGenerator()


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
