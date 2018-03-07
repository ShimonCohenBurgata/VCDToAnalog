import re

vcd_info = r'C:\Users\shcohen\PycharmProjects\VCDToAnalog\vcd_and_info_files\sim_info.info'
attribute_dict = {'trise': '10ns', 'tfall': '10ns', 'vih': 2.3, 'vil': 0.05, 'vol': 0.00001, 'voh': 2.5}
with open(vcd_info, 'r') as fo:
    lines = fo.read().splitlines()

for line in lines:
    mo = re.search(r'^\.({}) (.+) (.*)'.format('trise|tfall|vih|vil|vol|voh'), line)
    if mo:

        print('{} {}'.format(attribute_dict[mo.group(1)], float(mo.group(2))))
    else:
        pass
