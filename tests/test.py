import time
from collections import deque
import re
from bisect import bisect_left, bisect_right

vcd_source = r'U:\shimonc\gen6\pd69201_top_recordings\pd69201_vcd_dump_res_det_to_ovl.vcd'

with open(vcd_source) as fo:
    file_list = fo.read().splitlines()
file_list = deque(file_list)

# t1 = time.process_time()
# # Find all time steps in vcd output file and stores them in a list
# for arg in file_list:
#     mo = re.search(r'^#(\d.*)', arg)
#     if mo:
#         time_step_list.append(int(mo.group(1)))
# print(time.process_time() - t1)


# t2 = time.process_time()
# # Find all time steps in vcd output file and stores them in a list
# lst = [item for item in file_list if re.search(r'^#(\d.*)', item)]
# print(time.process_time() - t2)
# print(lst[0:24])

# t2 = time.process_time()
time_step_list = [int(item) for item in re.findall(r'#(\d+)', ' '.join(file_list))]
# print(time.process_time() - t2)

t2 = time.process_time()
i = bisect_left(time_step_list, 246523962800)
print(time.process_time() - t2)

print(i)
