import vcd_to_analog.Verilog_VCD as vcd
import re
from shutil import copyfile
from vcd_to_analog.signal_data import Signal
from collections import OrderedDict
from bisect import bisect_left
import ast


class VCDToAnalog(object):
    """
    Class for generating analog info file form VCD (Value Change Dump)
    For Cadence Analog Design Environment.
    The class also enable to change and manipulate VCD data
    """

    def __init__(self, vcd_path, vcd_output_path, info_path):
        """
        Constructor

        Args:
            vcd_path (str) - path of vcd file
            vcd_output_path (str) - path of vcd output path
            info_path (str) - path of info file
        """
        self._vcd_path = vcd_path
        self._vcd_output_path = vcd_output_path
        copyfile(self._vcd_path, self._vcd_output_path)
        self._vcd = {}
        self._signals = {}
        self._info_path = info_path
        self._set_vcd()
        self._timescale = vcd.get_timescale()
        self._simulation_start_time = self._start_time()
        self._simulation_end_time = self._end_time()
        self._total_simulation_time = self._simulation_end_time - self._simulation_start_time
        self._generate_info_file()

    def _set_vcd(self):
        """
        Generate vcd data base
        """
        try:
            self._vcd = vcd.parse_vcd(self._vcd_output_path, only_sigs=1)
        except FileNotFoundError as e:
            print('{}'.format(e))
        self._init_signals()

    def remove_consecutive_duplicates(self):
        """
         Remove consecutive duplicates from vcd data base
         and updates output file

        """
        # dictionary that contains all signals wildcards
        wildcard_dict = {}
        lst = []

        # initiate dictionary with empty string
        for wildcard_key in self._vcd:
            wildcard_dict[wildcard_key] = ''

        # put all lines in list
        with open(self._vcd_output_path, 'r') as fo:
            file_list = fo.read().splitlines()

        # loop over all list items
        for line in file_list:
            # try to match bit data line
            mo_bit = re.search(r'^(0|1)(.+)$', line)

            # try to match bus data line
            mo_bus = re.search(r'^b(0|1).* (.+)$', line)

            # match bit data line
            if mo_bit:
                # assign wildcard in var
                wildcard = mo_bit.group(2)

                # check if the line equal line stored in dictionary
                # line is duplicate
                if wildcard_dict[wildcard] == line:
                    # do not write line
                    pass
                # line is not duplicate
                else:
                    # write line
                    lst.append(line)

                    # change value in dictionary
                    wildcard_dict[wildcard] = line

            # match bus data line
            elif mo_bus:
                # assign wildcard in var
                wildcard = mo_bus.group(2)

                # check if the line equal line stored in dictionary
                # line is duplicate
                if wildcard_dict[wildcard] == line:
                    # do not write line
                    pass
                else:
                    # write line
                    lst.append(line)

                    # change value in dictionary
                    wildcard_dict[wildcard] = line
            # do not match
            else:
                # write line
                lst.append(line)

        # write list to output file
        fh = open(self._vcd_output_path, 'w')
        fh.write('\n'.join(lst))
        fh.close()

    def _init_signals(self):
        """
        Generate a dictionary of Signal instances.
        each instance is been set for all attributes
        for now only inputs are supported
        This is a private method
        """
        # loop over all signals
        for wildcard_key in self._vcd:
            # get signal name i.e. '5MHz_CLK'
            sig_name = self._vcd[wildcard_key]['nets'][0]['name']

            # set the signal to input. need to add output support
            sig_io = 'in'

            # get signal size
            sig_size = int(self._vcd[wildcard_key]['nets'][0]['size'])
            # get signal hierarchy
            sig_hier = self._vcd[wildcard_key]['nets'][0]['hier']

            # create list of Signal objects
            self._signals[sig_name] = Signal(wildcard_key, sig_name, sig_io, sig_size, sig_hier)

    def _generate_info_file(self):
        """
        Generate the the .info to be used by cadence spectre simulator
        """
        try:
            fh = open(self._info_path, 'w')
            # call object __str__()
            fh.write(str(self))
            fh.close()
        except FileNotFoundError as e:
            print('{}'.format(e))

    def get_signal_info(self, signal_name):
        """
        Signal information getter
        Args:
            signal_name (str) - The name of the signal for which we want to see the information

        #>>> db = VCDToAnalog('signal_crt_analog_3.vcd')
        #>>> print(db.get_signal_info('CLK_25MHZ'))

        #>>>
            .in CLK_25MHZ
            .vih 2.0 CLK_25MHZ
            .vil 0.0 CLK_25MHZ
            .trise 0.1 CLK_25MHZ
            .tfall 0.1 CLK_25MHZ
        """
        if signal_name not in self._signals.keys():
            raise KeyError('{} is not in signals list'.format(signal_name))
        # call Signal object __str__()
        print(self._signals[signal_name])

    def _extract_formated_time_scale(self, opt_time):
        """
        extract formatted time scale to value and units

        return:
            ts_val (int) - the integer value of opt time
            ts_units (str) - the units of opt time
        i.e.
        opt_time = '10ns'
        ts_val == 10
        ts_units = 'ns'

        """

        # match optional time variable
        mo = re.search(r'(\d+)(\w+)', opt_time)

        # if found match extract value in integer form and units in string form
        if mo:
            ts_val = int(mo.group(1))
            ts_unit = mo.group(2)

            # check that that the extracted units are part of the allowed values
            if ts_unit not in ['ps', 'ns', 'us', 'ms', 's']:
                raise ValueError(
                    '--> {} <-- is not a valid time unit allowed values are ps, ns, us, ms, s'.format(ts_unit))
            # raise exception if units are not part of the allowed values
            else:
                return ts_val, ts_unit
        # raise exception if optional time is not a valid input
        else:
            raise BaseException(
                '{} is not a valid time format an example for valid format is \'10ns\''.format(opt_time))

    def _time_scale_convertor(self, opt_time):
        """
        Time units convector

        Args:
             opt_time(str) - The user defined time scale. the options are
            'ps' --> Pico second = 1e-12 seconds
            'ns' --> Nano second = 1e-9 seconds
            'us' --> Micro second = 1e-6 seconds
            'ms' --> Milli second = 1e-3 seconds
            's' --> second

        return:
            opt_ts_val (int) - The optional time value
            opt_ts_units (str) - The optional time units
            def_ts_val (int) - The VCD database time value
            def_ts_units (str) - The VCD database time units
            factor (int) - The factor between user defined time unit and vcd default unit

        """
        # dict contains the relations between time units
        ts_dict = {'ps': 1e12, 'ns': 1e9, 'us': 1e6, 'ms': 1e3, 's': 1}

        # get the vcd default time scale
        def_ts_val, def_ts_units = self._extract_formated_time_scale(self._timescale)

        # get the optional user time scale
        opt_ts_val, opt_ts_units = self._extract_formated_time_scale(opt_time)

        # calculates factor between user and vcd default time scales
        factor = ts_dict[def_ts_units] / ts_dict[opt_ts_units]

        # return conversion and default values
        return opt_ts_val, opt_ts_units, def_ts_val, def_ts_units, factor

    def _start_time(self):
        """
        Return the simulation start time
        which is the first number after the wildcard #

        Return:
            st (int) - Simulation start time at VCD database time scale units
        """
        # zero the start time variable
        st = 0

        # open the output file search for first time step signature and break from the loop
        # i.e. #10
        with open(self._vcd_output_path, 'r') as fo:
            for line in fo:
                mo = re.search(r'^#(\d.*)$', line)
                if mo:
                    st = int(mo.group(1))
                    break
                else:
                    pass

        return st

    def _end_time(self):
        """
        Return the simulation end time
        which is the last number after the wildcard #

        Return:
            st (int) - Simulation end time at VCD database time scale units
        """

        # zero the end time variable
        et = 0

        # open the output file search for last time step signature
        # i.e. #10
        fh = open(self._vcd_output_path, 'r')
        for line in reversed(fh.readlines()):
            mo = re.search(r'^#(\d+)$', line)
            if mo:
                et = int(mo.group(1))
                fh.close()
                break
            else:
                pass
        fh.close()
        return et

    def _show_time(self, time, time_string, opt_time=''):
        """
        Shows the Simulation start time in user defined time unit
        If user leave optional time field empty the time units will be as defined in vcd file

        Args:
            time (int) - the time to show
            time_string (str) - string that represents the time tag (i.e. 'start', 'stop', 'simulation')
        kwargs:
            opt_time(str) - The user defined time scale. the options are
            'ps' --> Pico second = 1e-12 seconds
            'ns' --> Nano second = 1e-9 seconds
            'us' --> Micro second = 1e-6 seconds
            'ms' --> Milli second = 1e-3 seconds
            's' --> second

        return:
            (str) - String that represent simulation start time


        """
        # call _time_scale_convertor and get values from method
        opt_ts_val, opt_ts_units, def_ts_val, def_ts_units, factor = self._time_scale_convertor(opt_time)

        # return string with appropriate values and units per user request
        return '{} time is {}{}'.format(time_string, time * def_ts_val / (factor * opt_ts_val),
                                        '({}{})'.format(opt_ts_val, opt_ts_units))

    def show_start_time(self, opt_time=''):
        """
        Kwargs:
            opt_time (str) - optional time scale
        return:
            (str) - simulation start time in user defined time scale
        """

        # update object var _simulation_start_time
        self._simulation_start_time = self._start_time()

        # print the result bu calling object _show_time
        return self._show_time(self._simulation_start_time, 'start', opt_time)

    def show_end_time(self, opt_time):
        """
              Kwargs:
                  opt_time (str) - optional time scale
              return:
                  (str) - simulation end time in user defined time scale
              """
        # update object var _simulation_start_time
        self._simulation_end_time = self._end_time()

        # print the result bu calling object _show_time
        return self._show_time(self._simulation_end_time, 'end', opt_time)

    def show_sim_time(self, opt_time=''):
        """
              Kwargs:
                  opt_time (str) - optional time scale
              return:
                  (str) - total simulation time in user defined time scale
              """
        # update simulation start time
        self._simulation_start_time = self._start_time()

        # update simulation stop time
        self._simulation_end_time = self._end_time()

        # calculate total simulation time
        self._total_simulation_time = self._simulation_end_time - self._simulation_start_time

        # print the result by calling _show_time_method
        return self._show_time(self._simulation_end_time - self._simulation_start_time, 'simulation', opt_time)

    def generate_reduced_vcd(self, formatted_delay='0ns'):
        """
        Generate new vcd where the start time is 0 + delay
        Ignores the simulation time where signal are not dumped


        Kwargs:
            formatted_delay (str) - how much delay we want to add before signals are dumped
            i.e.:
                '1ns'
                '10ns'
                '100us'

        """

        # update simulation start time
        self._simulation_start_time = self._start_time()

        # get time scale conversion values
        ts_val, ts_units, def_ts_val, def_ts_units, factor = self._time_scale_convertor(formatted_delay)

        # calculate user request delay
        delay = int(ts_val * factor / def_ts_val)

        # open vcd output file
        with open(self._vcd_output_path, 'r') as fo:
            file_string = fo.read()

        # find all time steps and reduced the first time step and add delay
        st = re.sub(r'#(\d+)', lambda x: '#' + str(int(x.group(1)) - self._simulation_start_time + delay), file_string)

        # open vcd output file and write the manipulated string
        fo = open(self._vcd_output_path, 'w')
        fo.write(st)
        fo.close()

    def _change_signal_value(self, input_string, signal_name, opt_time, value):
        """
        Change a signal value in a specific time
        This function is private
        Args:
            input_string (str) - A string that represent the vcd file that
                                we want to change

            signal_name (str) - the name of the signal that we want to change

            opt_time (int) - The time where we want to change the signal value

            value (str) - the value of the signal that we want to change

        """
        # initiate list to contain the manipulated file
        lst = []

        # get the signal wildcard
        wildcard = self._signals[signal_name].get_wildcard()

        # var that represents the change to be done i.e. 10#
        value_time_string = value + wildcard

        # var for capturing the previous time step found
        prev_step = 0

        # flag for finding match
        done = True

        # wildcard flag check if wild card value already exists between 2 time steps
        wildcard_flag = False

        # get time scale conversion values
        ts_val, ts_units, def_ts_val, def_ts_units, factor = self._time_scale_convertor(opt_time)

        # calculate the time in default vcd file were we want to change the signal value
        time = int(ts_val * factor / def_ts_val)

        # in case that time is higher than VCD end time
        if time > self._simulation_end_time:
            return input_string + '#{}\n'.format(time) + value_time_string + '\n'

        # In case that time is within VCD time steps
        for line in input_string.splitlines():

            # run until done flag is false
            if done:

                # search time step matching
                mo = re.search(r'^#(\d+)', line)
                if mo:
                    # The time value at a line which have time step string
                    temp_step = int(mo.group(1))

                    # If the time step exists add the line
                    # and afterwards the add value wildcard string
                    # put True in the flag wildcard_flag in order to check if the signal
                    # exists between current time step and next time step
                    # put False in done flag we finished the value insertion
                    if temp_step == time:
                        lst.append(line + '\n')
                        lst.append(value_time_string + '\n')
                        done = False
                        wildcard_flag = True

                    # Set prev_step to the current time step
                    # this will enable us to set a signal value between
                    # 2 time steps
                    elif temp_step < time:
                        prev_step = temp_step
                        lst.append(line + '\n')

                    # Check that time is between current time step and previous time step
                    # Set new value in between
                    # Set done to False we finished the value insertion
                    elif temp_step > time > prev_step:
                        lst.append('#' + str(time) + '\n' + value_time_string + '\n')
                        lst.append(line + '\n')
                        done = False
                # we found no matching in the current line
                # write the line and continue
                else:
                    lst.append(line + '\n')
            # We placed the signal value
            # now we need to search if a value already exist
            # between current time step and next time step
            elif wildcard_flag:

                # Search if a signal already exist
                # mo1 = re.search(r'.*{}'.format('\\' + wildcard), line)

                # match  bit data line i.e. 1& or 0)
                mo_bit = re.search(r'^(0|1)(.+)$', line)

                # match bus data line i.e. b1010 ^ or b0000 *&
                mo_bus = re.search(r'^b(0|1).* (.+)$', line)

                # match bit data line and wildcard in line == wildcard in keys
                if mo_bit and mo_bit.group(2) == wildcard:
                    mo1 = True

                # match buss data line and wildcard in line == wildcard in keys
                elif mo_bus and mo_bus.group(2) == wildcard:
                    mo1 = True

                # don't match bit data line nor bus data line
                else:
                    mo1 = False

                # search the next time step
                mo2 = re.search(r'^#(\d+)', line)

                # If a signal exist do not add the line
                if mo1:
                    wildcard_flag = False

                # if we reached the next time step write the line
                # and set wildcard flag to False
                elif mo2:
                    lst.append(line + '\n')
                    wildcard_flag = False

                # No match at mo1 or mo2 write the line
                else:
                    lst.append(line + '\n')
            # We are finished to set the signal
            # and also remove the existing one if exist
            # write the rest of the lines
            else:
                lst.append(line + '\n')

        return ''.join(lst)

    def change_signals_value(self, signals_dict):
        """
        Change the value of a set of signals by user request.
        Each signal can be changed in a few time steps.
        Args:

            signals_dict (dict) - A dictionary that contains the signal name and the time:value pairs
                                    for each signal

        #>>> db = VCDToAnalog('signal_crt_analog_3.vcd')
        #>>> b.change_signals_value(r'signal_crt_analog_3.vcd', r'new_vcd.vcd',
                            {
                                'CLK_25MHZ':
                                         {
                                            40: '1', 110: '0'
                                         }
                                 ,
                                'CLK_160MHZ':
                                         {
                                         70: '0'
                                         }
                             }
                             )
        """
        # Check that all signals in dict exist
        for sig in signals_dict.keys():
            if sig not in self._signals:
                raise KeyError('{} is not in signals list'.format(sig))

        # Loop over the signals
        for sig in signals_dict.keys():

            # Loop over the signal time steps
            for time_key in signals_dict[sig].keys():

                # Update simulation end time
                self._simulation_end_time = self._end_time()

                # Clear strings
                st = ''

                # Copy file in to sting
                with open(self._vcd_output_path, 'r') as fo:
                    for line in fo:
                        st += line

                # Open output file for writing
                fh = open(self._vcd_output_path, 'w')

                # add space character in case that the signal is bus i.e. b1010 $
                var = signals_dict[sig][time_key]

                var_mo = re.search(r'^b.*', var)
                if var_mo:
                    var = var + ' '

                # Manipulate string
                st_out = self._change_signal_value(st, sig, time_key, var)
                fh.write(st_out)
                fh.close()

    def slice_vcd(self, formatted_tstart, formatted_tend, reduce=False, formatted_delay='0us'):
        """
        Slice the vcd file to a specific section
        This method allows to debug analog functionality with out the need
        to wait for the simulation to reach a specific time step
        Args:
            formatted_tstart (str) - from where to start slice i.e. '100ns'
            formatted_tend (str) - end time step i.e. '334ns'
            reduce (bool) - If true tstart will be zero
            formatted_delay (str) - how much delay to add if reduced is True
        """

        # calculate ratios between user optional time format and vcd default format
        time_convert_list = list(map(self._time_scale_convertor, [formatted_tstart, formatted_tend]))

        # Convert user time steps to vcd default time step values
        start_time = (time_convert_list[0][0] / time_convert_list[0][2]) * time_convert_list[0][4]
        stop_time = (time_convert_list[1][0] / time_convert_list[1][2]) * time_convert_list[1][4]

        # write the vcd output file into list
        with open(self._vcd_output_path) as fo:
            file_list = fo.read().splitlines()

        # List of all vcd time steps
        time_step_list = [int(item) for item in re.findall(r'#(\d+)', ' '.join(file_list))]

        # string representing first time step
        first_start_time = '#{}'.format(time_step_list[0])

        # string representing user start time step
        min_start_time = '#{}'.format(time_step_list[bisect_left(time_step_list, start_time) - 1])

        # string representing user stop time step
        max_stop_time = '#{}'.format(time_step_list[bisect_left(time_step_list, stop_time) + 1])

        # find the index in the vcd list of the first time step
        first_time_step_index = file_list.index(first_start_time)

        # write to list until vcd first time step
        lst = file_list[0:first_time_step_index]

        # find the index in the vcd list of the user start time step
        min_start_time_index = file_list.index(min_start_time)

        # find the index in the vcd list of the user stop time step
        max_stop_time_index = file_list.index(max_stop_time)

        # add the user requested section to the list

        lst.extend(file_list[min_start_time_index: max_stop_time_index + 1])

        # If reduced, reduced the manipulated data to #0 and add delay
        if reduce:
            self.generate_reduced_vcd(formatted_delay)

        # If not reduced write the data as is
        else:
            fw = open(self._vcd_output_path, 'w')
            fw.write('\n'.join(lst))
            fw.close()

    def find_bit_change(self, signal_name, value, opt_time):
        """
        return dictionary of time steps where signal is changing to value
        bus not supported(yet)
        Args:
            signal_name (str)
            value (str) '0' or '1'
            opt_time (str) 'ps', 'ns', 'us', 'ms', 's'
        Return:
            dictionary with keys as occurrence number and value as time step value
        """

        # time unit conversion dictionary
        ts_dict = {'ps': 1e12, 'ns': 1e9, 'us': 1e6, 'ms': 1e3, 's': 1}

        # default vcd time scale
        def_ts_val, def_ts_units = self._extract_formated_time_scale(self._timescale)

        # read output file
        with open(self._vcd_output_path, 'r') as fo:
            lines = fo.read().splitlines()

        # get the wildcard for the signal name
        wildcard = self._signals[signal_name].get_wildcard()

        # time step dictionary
        # time_step_dict = {}
        time_step_dict = OrderedDict()

        # keys for dictionary
        count = 1

        # loop over all the output file lines
        for line in lines:

            # search for time step match
            mo = re.search(r'^#(\d.*)', line)

            # if match set time step value
            if mo:
                time_step = mo.group(1)

            # search for bit match i.e 1^ or 0&
            mo_bit = re.search(r'^(0|1)(.+)$', line)

            # if find bit match and the value == input value and the match is for signal name
            if mo_bit and mo_bit.group(1) == value and mo_bit.group(2) == wildcard:
                # add the value to the output dictionary
                time_step_dict[count] = str(
                    ts_dict[opt_time] * int(time_step) * def_ts_val / ts_dict[def_ts_units]) + opt_time
                # change key value
                count += 1

        return time_step_dict

    def set_all_attributes(self, attri_dict):
        """
        Change attributes to all signal
        Args:
            dictionary of attribute name and attribute value pairs
            for example:
            {'trise': 0.1, 'tfall': 0.1, 'vih': 2.0, 'vil': 0.0, 'vol': 0.00001, 'voh': 1.6}
        """
        for key in attri_dict.keys():

            # convert '10ns' kind of format to vcd default time
            if key == 'trise' or key == 'tfall':
                time_convert_list = list(self._time_scale_convertor(attri_dict[key]))
                # Convert user time steps to vcd default time step values
                attri_dict[key] = time_convert_list[0] * time_convert_list[2] * time_convert_list[4]

            # loop over all signal anf change their attributes
            for signal in self._signals.keys():
                self._signals[signal].set_attri(key, attri_dict[key])
        # update the info file
        self._generate_info_file()

    def set_signal_attributes(self, signal_name, attributes, val):
        """
        Change a signal attribute
        Args:
            signal_name (str) - the name of the signal
            attributes (str) - the name of the attribute options are 'trise', 'tfall', 'vih', 'vil', 'voh', 'vol'
            val (int) - the attribute value/

        """
        # convert '10ns' kind of format to vcd default time
        if attributes == 'trise' or attributes == 'tfall':
            time_convert_list = list(self._time_scale_convertor(val))
            # Convert user time steps to vcd default time step values
            val = time_convert_list[0] * time_convert_list[2] * time_convert_list[4]

        # change the signal attribute
        self._signals[signal_name].set_attri(attributes, val)

        # update the info file
        self._generate_info_file()

    def set_signals(self, set_signal_file):
        """
        Set a signal to a value for all simulation time
        specially useful to disable oscillating signals if they are not needed in simulation

        Args:
            a file contains a dictionary with the following arguments
            key = signal name
            value = list with two argumnets
                1. 'change' or 'no_change' select which signals to change and which not
                2. value '0' or '1'
                i.e.
                '{'CLK_25MHZ': ['change', '0'], 'CLK_160MHZ': ['no_change', ''], '5MHz_CLK': ['no_change', ''], '15MHz_CLK': ['no_change', '']}'
        """

        # convert a String representation of a dictionary to a dictionary
        with open(set_signal_file, 'r') as fo:
            set_signal_dict = ast.literal_eval(fo.read())

        # read output file
        with open(self._vcd_output_path, 'r') as fo:
            st = fo.read()

        # create a dictionary where the keys are the signal manes and the value is the wildcard
        name_dict = {self._vcd[key]['nets'][0]['name']: key for key in self._vcd}

        # loop over all signals
        for signal in set_signal_dict:

            # check if the signal need to be changed
            if set_signal_dict[signal][0] == 'change':

                # get the wildcard representation of the signal
                wildcard = name_dict[signal]

                # add \ for special characters
                if wildcard in ['^', '(', ')', '$', '+', '.', '*', '?']:
                    wildcard = re.escape(wildcard)

                # get the value of the signal to be changed to
                def_val = set_signal_dict[signal][1]

                # change the signal value in the string representation of the output file
                st = re.sub(r'([0|1])({})'.format(wildcard), lambda x: def_val + x.group(2), st)

        # write the manipulated string to the output file
        with open(self._vcd_output_path, 'w') as fo:
            fo.write(st)

    def signals_to_plot(self, *args):
        """
        generate data for plot object
        Args:
            *args (str) - signal names
        Return:
            2 item list
                1. dictionary of signal time step values
                2. dictionary of signal attribute objects
        """
        # dictionary for signals data value
        sig_data_dict = OrderedDict()

        # dictionary for attributes value
        sig_attri_dict = OrderedDict()

        # update vcd data base
        # needed if manipulation method was called before this method
        self._set_vcd()

        # loop over all user request signals
        for name in args:
            # get wildcard for signal == name
            wc = self._signals[name].get_wildcard()

            # update data dict with values from vcd data base
            sig_data_dict[name] = self._vcd[wc]

            # update attributes with values from signals
            sig_attri_dict[name] = self._signals[name]

        return [sig_data_dict, sig_attri_dict]

    def __repr__(self, signal_name=''):
        """
        Represent the VCD data base
        For debug purposes
        """
        # update vcd data base
        # needed if manipulation method was called before this method
        self._set_vcd()

        # initiate empty string
        st = ''

        # in case that all signals are required to be present
        if signal_name != '':
            wc = self._signals[signal_name].get_wildcard()
            st += '' + wc + '\n'
            st += '  ' * 2 + str(self._vcd[wc]['nets']) + '\n'
            st += '  ' * 2 + str(self._vcd[wc]['tv']) + '\n'

        # in case that specific signals are required
        else:
            for wildcard_key in self._vcd:
                st += wildcard_key + '\n'
                for key in self._vcd[wildcard_key]:
                    st += '\t' + key + '\n'
                    if key == 'nets':
                        st += '\t' * 2 + str(self._vcd[wildcard_key][key]) + '\n'
                    else:
                        st += '\t' * 2 + str(self._vcd[wildcard_key][key]) + '\n'

        return st

    def __str__(self):
        """
        Structure of analog info file
        """

        # make spectre understand vcd parenthesis form
        st = '.alias *[*] *<*>' + '\n'

        # start with signals in top level hierarchy
        for name in self._signals:
            if self._signals[name].get_hier() == '':
                st += str(self._signals[name]) + '\n'

        # continue with signals in lower hierarchy's
        for name in self._signals:
            if self._signals[name].get_hier() != '':
                st += str(self._signals[name]) + '\n'

        return st
