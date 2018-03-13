# import sys
# from vcd import VCDWriter
#
# with VCDWriter(sys.stdout, date='today') as vcd:
#     var2 = vcd.register_var('aaa.bbb', 'nn0', 'integer', 8, init='z', ident='$')
#     var3 = vcd.register_var('aaa.bbb', 'nn1', 'integer', 8, ident='(')
#     for timestep, value in enumerate(range(10, 20, 2)):
#         vcd.change(var2, timestep, value)
#     vcd.change(var3, 30, 8)
#     vcd.dump_off(3)
#
# # print([chr(i) for i in iter(range(127))][33:127])
from collections import OrderedDict

lst = [(0, 'x'), (0, 'x'), (10, '1'), (20, '0'), (30, '1')]
lst = list(OrderedDict.fromkeys(lst))
# lst = [(lambda x: x[0], lambda x: '0' if x[1] != '0' or x[1] != '1' else x[1]) for item in lst]
lst = [(item[0], item[1]) for item in lst if item[1] == '1' or item[1] == '0']
print(lst)
