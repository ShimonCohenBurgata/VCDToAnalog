import os

path = r'signal_crt_analog_3_new_a.vcd'
if not os.path.exists(path):
    raise FileNotFoundError('{} is not a valid path'.format(path))
