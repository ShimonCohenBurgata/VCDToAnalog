import re
import time

bit = '18^'
bus = 'b10101 $('
mo_bit = re.search(r'^(0|1)(.+)$', bit)
mo_bus = re.search(r'^b(0|1).* (.+)$', bus)
# if mo_bit:
#     print(mo_bit.group(0))
#     print(mo_bit.group(1))
#     print(mo_bit.group(2))
#
# print('\n')
#
# if mo_bus:
#     print(mo_bus.group(0))
#     print(mo_bus.group(1))
#     print(mo_bus.group(2))

# t1 = time.time()
# with open(r'pd69201_vcd_dump_res_det_to_ovl.vcd', 'r') as fo:
#     file_list = fo.read().splitlines()
# print(len(file_list))
# print(time.time() - t1)

# dct = {'#': '1#', '^': '0^', '%': 'b0001 %'}
# if '#' in dct.keys():
#     print(dct['#'])


lst = ['\%', '\(']
st = r'1%'

mo = re.search(r'.*{}'.format(lst[0]), st)
if mo:
    print(mo.group(0))


start time is 1998.753561(1ms)
{1: '200002425400'}
