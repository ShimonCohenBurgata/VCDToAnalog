import time
from collections import deque
import re
from bisect import bisect_left, bisect_right
import vcd_to_analog.Verilog_VCD as vcd
import os

# vcd_source = r'C:\pd69201_top_recordings\pd69201_vcd_dump_res_det_to_ovl.vcd'
# test_file = r'C:\pd69201_top_recordings\test.vcd'

os.path.abspath(os.chdir('..' + r'\vcd_and_info_files'))
vcd_source = r'sim.vcd'
print(vcd.parse_vcd(vcd_source,only_sigs=1))