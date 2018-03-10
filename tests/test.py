import re
import os
import tests.set_signals as set_signal

os.path.abspath(os.chdir('..' + r'\vcd_and_info_files'))
vcd_source = r'sim.vcd'
with open(vcd_source, 'r') as fo:
    st = fo.read()

wildcard_dict = {'!': 'CLK_25MHZ', '"': 'CLK_160MHZ', '^': '5MHz_CLK', '\(': '15MHz_CLK', }
value_dict = {value: key for key, value in wildcard_dict.items()}

def_val = '0'

fh = set_signal.set_signals()
for signal in fh:
    if fh[signal][0] == 'change':
        wildcard = value_dict[signal]
        def_val = fh[signal][1]
        st = re.sub(r'([0|1])({})'.format(wildcard), lambda x: def_val + x.group(2), st)
print(st)

