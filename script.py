#!/usr/bin/env python3



#stm32f4_hal.c

import chipwhisperer as cw
import matplotlib.pyplot as plt
import re
import time
import numpy as np

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
    # if scope.adc.state:
        # print("capture is incomplete! increase decimate")
        # exit(1)

    print("trigger high sample count:", scope.adc.trig_count)

    trace = scope.get_last_trace()
    # return trace[:scope.adc.trig_count // scope.adc.decimate]
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

#init scope
scope = cw.scope(scope_type=cw.scopes.OpenADC)
scope.default_setup()
scope.adc.basic_mode = "high"
scope.adc.timeout = 30
scope.adc.samples = 90000
scope.adc.decimate = 500 # 307 par seconde

reset_target(scope)

plt.figure()
arr = avg_trace(1, 1)
# arr = separate_trace(1, 5)
for i in arr:
    plt.plot(i)
outfile = "trace_dilithium_1_15.npy"
np.save(outfile, arr)
scope.dis()
plt.show()
