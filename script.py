#!/usr/bin/env python3



#stm32f4_hal.c

import chipwhisperer as cw
import matplotlib.pyplot as plt
import re
import time
import numpy as np

start_pat = re.compile('.*={4,}', re.DOTALL)
end_pat = re.compile('#\n', re.DOTALL)


#init scope
scope = cw.scope(scope_type=cw.scopes.OpenADC)
scope.default_setup()
scope.adc.timeout = 60


#init target
target = cw.target(scope)

def reset_target(scope):
    scope.io.nrst = 'low'
    time.sleep(0.05)
    scope.io.nrst = 'high'
    time.sleep(0.05)

def cap_pass_trace():
    scope.arm()
    ret = scope.capture()
    if ret:
        print('Timeout happened during acquisition')

    trace = scope.get_last_trace()
    return trace

def avg_trace(ntrace, nnoise):
    arr = []
    for i in range(ntrace):
        res = []
        for j in range(nnoise):
            res += [cap_pass_trace()]
        arr += [np.average(res, axis=0)]
    return arr

def separate_trace(ntrace, nnoise):
    arr = []
    for i in range(ntrace):
        for j in range(nnoise):
            arr += [cap_pass_trace()]
    return arr

reset_target(scope)

plt.figure()

arr = avg_trace(2, 15)
# arr = separate_trace(1, 5)
for i in arr:
    plt.plot(i)

scope.dis()
target.dis()
plt.show()
