import time
from collections import deque
import re
from bisect import bisect_left, bisect_right

vcd_source = r'C:\pd69201_top_recordings\pd69201_vcd_dump_res_det_to_ovl.vcd'
test_file = r'C:\pd69201_top_recordings\test.vcd'

# with open(vcd_source) as fo:
#     file_list = fo.read().splitlines()
#
# t1 = time.time()
# time_step_list = [int(item) for item in re.findall(r'#(\d+)', ' '.join(file_list))]
# print(time.time() - t1)


# lst = []
#
# t1 = time.time()
# # open vcd output file
# with open(vcd_source, 'r') as fo:
#     for line in fo:
#
#         # match time step signature
#         mo = re.search(r'^#(\d.*)$', line)
#
#         # if match was found change the time step accordingly with regards to delay
#         if mo:
#             lst.append('#{}\n'.format(int(mo.group(1)) - first_time))
#
#         # if match was not found write the line without change it
#         else:
#             lst.append(line)
#
# # create string from string
# st = ''.join(lst)
#
# # open vcd output file and write the manipulated string
# fo = open(test_file, 'w')
# fo.write(st)
# fo.close()

first_time = 199875356100

# with open(vcd_source) as fo:
#     file_list = fo.read()
t1 = time.time()
with open(vcd_source) as fo:
    file_list = fo.read()
print(time.time() - t1)


test = re.sub(r'#(\d+)', lambda x: '#' + str(int(x.group(1)) - first_time), file_list)
fo = open(test_file, 'w')
fo.write(test)
fo.close()


# st = '#1234'
# st = re.sub(r'#(\d+)', lambda x: str(int(x.group(1))), st)
# print(st)
