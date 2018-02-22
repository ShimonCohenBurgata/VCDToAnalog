# import re
#
# wildcard = '"'
# first_flag = True
# sentinel = ''
# with open('signal_crt_analog_3.vcd') as fo:
#     st = ''
#     for line in fo:
#         mo = re.search(r'(\d+){}'.format(wildcard), line)
#
#         if mo and first_flag:
#             st += line
#             sentinel = mo.group(1)
#             first_flag = False
#
#         elif mo and not first_flag:
#             if mo.group(1) == sentinel:
#                 pass
#             else:
#                 st += line
#                 sentinel = mo.group(1)
#         else:
#             st += line

# print(st)

# data_reduced = []
# for wildcard in self._vcd.keys():
#     data = self._vcd[wildcard]['tv']
#     idx = 1
#     sentinel = data[0]
#     data_reduced.append(data[0])
#     while idx <= len(data) - 1:
#         if data[idx][1] != sentinel[1]:
#             data_reduced.append(data[idx])
#             sentinel = data[idx]
#             idx += 1
#         else:
#             sentinel = data[idx]
#             idx += 1
#
#     self._vcd[wildcard]['tv'][:] = data_reduced
#     data_reduced.clear()

import re
line = '1^#'
wildcard = '('
# mo = re.search(r'(\d+){}'.format(wildcard), line)
mo = re.search(r'^(\d+)(.*)$'.format(wildcard), line)
if mo:
    print(mo.group(1))
    print(type(mo.group(2)))
