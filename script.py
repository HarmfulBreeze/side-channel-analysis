#!/usr/bin/env python3



#stm32f4_hal.c

import chipwhisperer as cw
import matplotlib.pyplot as plt
import re
import time

start_pat = re.compile('.*={4,}\n', re.DOTALL)
end_pat = re.compile('#\n', re.DOTALL)


#init scope
scope = cw.scope(scope_type=cw.scopes.OpenADC)
scope.default_setup()


#init target
target = cw.target(scope)

#capture trace
ktp = cw.ktp.Basic()
key, pt = ktp.new_pair()
#trace = cw.capture_trace(scope, target, pt, key)

def reset_target(scope):
    scope.io.nrst = 'low'
    time.sleep(0.05)
    scope.io.nrst = 'high'
    time.sleep(0.05)

def cap_pass_trace(pass_guess):
    # reset_target(scope)
    # num_char = target.in_waiting()
    # while num_char > 0:
    #     target.read(num_char, 10)
    #     time.sleep(0.01)
    #     num_char = target.in_waiting()

    scope.arm()
    ret = scope.capture()
    if ret:
        print('Timeout happened during acquisition')

    trace = scope.get_last_trace()
    return trace


reset_target(scope)

data = ''
# Wait for the first equal sign
while '=' not in data:
    data += target.read()
# Wait for the end of the equal delimiter
match = None
while match is None:
    data += target.read()
    print(data)
    match = start_pat.match(data)


trace = cap_pass_trace("azertyuiop")

plt.figure()
plt.plot(trace)
plt.xlim([0, 100])
plt.show()
