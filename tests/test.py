import time
from collections import deque
import re
from bisect import bisect_left, bisect_right

vcd_source = r'C:\pd69201_top_recordings\pd69201_vcd_dump_res_det_to_ovl.vcd'
test_file = r'C:\pd69201_top_recordings\test.vcd'

with open(vcd_source) as fo:
    file_list = fo.read().splitlines()

t1 = time.time()
time_step_list = [int(item) for item in re.findall(r'#(\d+)', ' '.join(file_list))]
print(time.time() - t1)

t1 = time.time()
r = re.compile(r'#\d+')
time_step_list2 = list(filter(r.search, file_list))
print(time.time() - t1)


