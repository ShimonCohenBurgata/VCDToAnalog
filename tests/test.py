import re
import time
import os

bit = '18^'
bus = 'b10101 $('
mo_bit = re.search(r'^(0|1)(.+)$', bit)
mo_bus = re.search(r'^b(0|1).* (.+)$', bus)

