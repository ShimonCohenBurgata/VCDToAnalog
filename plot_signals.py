import matplotlib.pyplot as plt
from itertools import cycle


class PlotSignals(object):
    """
    plot signal from vcd data base
    """

    # def __init__(self, signals_data_dict, signals_attri_dict):
    def __init__(self, plot_ob):
        """ Constructor """
        # self._signals_data_dict = signals_data_dict
        # self._signals_attri_dict = signals_attri_dict

        self._signals_data_dict = plot_ob[0]
        self._signals_attri_dict = plot_ob[1]

    def plot_signals(self):
        """
        Create rise and fall time, time steps
        adjust input and output values to vih and vil
        and plot the signals
        """

        # iterator for plot colr
        color_cycle = cycle('bgrcmky')

        # prepare the subplot number
        row_number = len(self._signals_data_dict)
        column_number = 1
        subplot_index = []
        for idx in range(row_number):
            subplot_index.append(row_number * 100 + column_number * 10 + idx + 1)

        # create time list and voltage list
        time_list = []
        voltage_list = []

        xlabel_flag = True

        # Loop to go over all the signals
        for key in self._signals_data_dict:
            signal = self._signals_data_dict[key]['tv']

            # Flag that remembers if the last signal was high or low
            flag = signal[0][1]

            for item in signal:

                # Get attributes from signals data base
                vih = self._signals_attri_dict[key].get_attri('vih')
                vil = self._signals_attri_dict[key].get_attri('vil')
                fall_time = self._signals_attri_dict[key].get_attri('tfall')
                rise_time = self._signals_attri_dict[key].get_attri('trise')

                # Create rise and fall time, time steps
                # signal changes from high to low
                if item[1] == '0' and flag == '1':
                    time_list.append(item[0])
                    voltage_list.append(vih)
                    time_list.append(item[0] + fall_time)
                    voltage_list.append(vil)
                    flag = '0'

                # signal stays low
                elif item[1] == '0' and flag == '0':
                    time_list.append(item[0])
                    voltage_list.append(vil)

                # signal changes from low to high
                elif item[1] == '1' and flag == '0':
                    time_list.append(item[0])
                    voltage_list.append(vil)
                    time_list.append(item[0] + rise_time)
                    voltage_list.append(vih)
                    flag = '1'

                # signal stays high
                else:
                    time_list.append(item[0])
                    voltage_list.append(vih)

            plt.subplot(subplot_index.pop())
            if xlabel_flag:
                plt.xlabel('time (ns)')
                xlabel_flag = False
            else:
                plt.xlabel('')
            plt.ylabel(key, rotation='horizontal', horizontalalignment='right')
            plt.plot(time_list, voltage_list, c=next(color_cycle))
            time_list.clear()
            voltage_list.clear()

        plt.show(block=True)
