from vcd_to_analog.vcd_generator import VCDToAnalog
from vcd_to_analog.plot_signals import PlotSignals
import time
from collections import OrderedDict
import os


def main():
    """
    Naive test later will be replaced with pytest

    """
    # os.path.abspath(os.chdir('..' + r'\vcd_and_info_files'))
    #
    # vcd_source = r'sim.vcd'
    # vcd_target = r'sim_new.vcd'
    # vcd_info = r'sim_info.info'
    # set_signal_file = r'C:\Users\shcohen\PycharmProjects\VCDToAnalog\tests\set_signal_file.txt'

    vcd_source = r'U:\shimonc\gen6\pd69201_top_recordings\pd69201_vcd_dump_res_det_to_ovl.vcd'
    vcd_target = r'U:\shimonc\gen6\pd69201_top_recordings\sim_new.vcd'
    vcd_info = r'U:\shimonc\gen6\pd69201_top_recordings\sim_info.info'
    set_signal_file = r'U:\shimonc\gen6\pd69201_top_recordings\set_signal_file.txt'

    # vcd_source = r'C:\pd69201_top_recordings\pd69201_vcd_dump_res_det_to_ovl.vcd'
    # vcd_target = r'C:\pd69201_top_recordings\sim_new.vcd'
    # vcd_info = r'C:\pd69201_top_recordings\sim_info.info'

    db = VCDToAnalog(vcd_source, vcd_target, vcd_info)

    # db.remove_consecutive_duplicates()

    # db.get_signal_info('CLK_25MHZ')
    # db.get_signal_info('accumulator[3:0]')
    # db.remove_consecutive_duplicates()

    # print(db.show_start_time('1ms'))
    # print(db.show_end_time('1ms'))
    # print(db.show_sim_time('1ms'))

    # db.generate_reduced_vcd()
    # db.generate_reduced_vcd('1us')

    # sig_dict = {'15MHz_CLK': {'300ns': '0', '350ns': '1'}, '5MHz_CLK': {'65000ps': '1', '133ns': '0'}}
    # sig_dict = {'5MHz_CLK': {'65ns': '1', '133ns': '0'}}
    # sig_dict = {'5MHz_CLK': {'420ns': '1', '450ns': '0'}}
    # sig_dict = {'accumulator[3:0]': {'400ns': 'b1010'}}

    # db.change_signals_value(sig_dict)

    # db.slice_vcd('142ns', '472ns')
    # db.slice_vcd('125ns', '220ns')
    # db.slice_vcd('142ns', '472ns', True, '170ns')

    # t1 = time.time()
    # db.slice_vcd('2000024000000ps', '2504023000000ps')
    db.slice_vcd('2000024254000ps', '2504023254000ps')
    db.set_signals(set_signal_file)
    # print(time.time() - t1)

    # attri_dict = {'trise': '10ns', 'tfall': '10ns', 'vih': 2.3, 'vil': 0.05, 'vol': 0.00001, 'voh': 2.5}
    # db.set_all_attributes(attri_dict)

    # attribute_dict = OrderedDict()
    # attribute_dict['trise'] = '10ns'
    # attribute_dict['tfall'] = '8ns'
    # attribute_dict['vih'] = 2.3
    # attribute_dict['vil'] = 0.05
    # attribute_dict['vol'] = 0.00001
    # attribute_dict['voh'] = 2.5
    # db.set_all_attributes(attribute_dict)

    # db.set_signal_attributes('CLK_25MHZ', 'vih', 1.8)
    # db.set_signal_attributes('CLK_25MHZ', 'trise', '10000ps')
    # db.set_signal_attributes('CLK_25MHZ', 'trise', '10ns')
    # db.get_signal_info('CLK_25MHZ')

    # plot_ob = db.signals_to_plot('5MHz_CLK')
    # plot_ob = db.signals_to_plot('CLK_25MHZ', 'CLK_160MHZ', '15MHz_CLK', '5MHz_CLK')
    # pso = PlotSignals(plot_ob)
    # pso.plot_signals()
    #
    # print(db.__repr__('CLK_25MHZ'))
    # print(str(db))
    # print(repr(db))

    # print(db.find_bit_change('res_det_block_en_d', '1', 'ps'))
    # print(db.find_bit_change('class_en_d', '1', 'ps'))
    # print(db.find_bit_change('accumulator[3:0]', 'b1010', 'ns'))

    # help(db)
    # help(db.remove_consecutive_duplicates)


if __name__ == "__main__":
    main()
