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

    # vcd_source = r'sim.vcd'
    # vcd_target = r'sim_new.vcd'
    # vcd_info = r'sim_info.info'
    # set_signal_file = r'C:\Users\shcohen\PycharmProjects\VCDToAnalog\tests\set_signal_file.txt'

    # vcd_source = r'C:\pd69201_top_recordings\pd69201_vcd_dump_res_det_to_ovl.vcd'
    # vcd_target = r'C:\pd69201_top_recordings\sim_new.vcd'
    # vcd_info = r'C:\pd69201_top_recordings\sim_info.info'

    # line detection script
    # vcd_source = r'U:\shimonc\gen6\pd69201_top_recordings\pd69201_vcd_dump_res_det_to_ovl.vcd'
    # vcd_target = r'U:\shimonc\gen6\pd69201_top_recordings\res_det\sim_new.vcd'
    # vcd_info = r'U:\shimonc\gen6\pd69201_top_recordings\res_det\sim_info.info'
    # set_signal_file = r'U:\shimonc\gen6\pd69201_top_recordings\res_det\set_signal_file.txt'
    # db = VCDToAnalog(vcd_source, vcd_target, vcd_info)
    # # print(db.find_bit_change('class_en_d', '1', 'ms'))
    # db.slice_vcd('0ms', '2505ms', True, '20ms')
    # db.set_signals(set_signal_file)
    # attri_dict = {'trise': '10ns', 'tfall': '10ns', 'vih': 5, 'vil': 0.0, 'vol': 0.0, 'voh': 5}
    # db.set_all_attributes(attri_dict)

    # short on start up script
    # vcd_source = r'U:\shimonc\gen6\pd69201_top_recordings\pd69201_vcd_short_on_su.vcd'
    # vcd_target = r'U:\shimonc\gen6\pd69201_top_recordings\start_up_to_short\sim_new.vcd'
    # vcd_info = r'U:\shimonc\gen6\pd69201_top_recordings\start_up_to_short\sim_info.info'
    # set_signal_file = r'U:\shimonc\gen6\pd69201_top_recordings\start_up_to_short\set_signal_file.txt'
    # db = VCDToAnalog(vcd_source, vcd_target, vcd_info)
    # db.generate_reduced_vcd()
    # print(db.show_start_time('1ms'))
    # print(db.show_end_time('1ms'))
    # print(db.show_sim_time('1ms'))
    # print(db.find_bit_change('port_off_d', '1', 'ms'))
    # print(db.find_bit_change('port_off_d', '0', 'ms'))
    # print(db.find_bit_change('class_en_d', '1', 'ms'))
    # print(db.find_bit_change('class_en_d', '0', 'ms'))
    # db.set_signals(set_signal_file)
    # attri_dict = {'trise': '10ns', 'tfall': '10ns', 'vih': 5, 'vil': 0.0, 'vol': 0.0, 'voh': 5}
    # db.set_all_attributes(attri_dict)

    # short on class monitor script
    vcd_source = r'U:\shimonc\gen6\pd69201_top_recordings\pd69201_vcd_dump_res_det_to_ovl.vcd'
    vcd_target = r'U:\shimonc\gen6\pd69201_top_recordings\cls_mntr\sim_new.vcd'
    vcd_info = r'U:\shimonc\gen6\pd69201_top_recordings\cls_mntr\sim_info.info'
    set_signal_file = r'U:\shimonc\gen6\pd69201_top_recordings\cls_mntr\set_signal_file.txt'
    db = VCDToAnalog(vcd_source, vcd_target, vcd_info)
    db.generate_reduced_vcd()
    db.slice_vcd('476ms', '600ms', True)
    sig_dict = {'port_off_d': {'0ns': '1'}, 'class_en_d': {'0ns': '0'}, 'res_det_block_en_d': {'0ns': '1'}}
    db.change_signals_value(sig_dict)

    # print(db.show_start_time('1ms'))
    # print(db.show_end_time('1ms'))
    # print(db.show_sim_time('1ms'))
    # print(db.find_bit_change('port_off_d', '1', 'ms'))
    # print(db.find_bit_change('port_off_d', '0', 'ms'))
    # print(db.find_bit_change('class_en_d', '1', 'ms'))
    # print(db.find_bit_change('class_en_d', '0', 'ms'))
    # print(db.find_bit_change('res_det_block_en_d', '1', 'ms'))
    # print(db.find_bit_change('res_det_block_en_d', '0', 'ms'))
    # db.set_signals(set_signal_file)
    attri_dict = {'trise': '10ns', 'tfall': '10ns', 'vih': 5, 'vil': 0.0, 'vol': 0.0, 'voh': 5}
    db.set_all_attributes(attri_dict)

    # plot_ob = db.signals_to_plot('class_en_d', 'port_off_d', 'res_det_block_en_d')
    # pso = PlotSignals(plot_ob)
    # pso.plot_signals()

    # short after port on
    # vcd_source = r'U:\shimonc\gen6\pd69201_top_recordings\pd69201_vcd_short.vcd'
    # vcd_target = r'U:\shimonc\gen6\pd69201_top_recordings\port_on_short\sim_new.vcd'
    # vcd_info = r'U:\shimonc\gen6\pd69201_top_recordings\port_on_short\sim_info.info'
    # set_signal_file = r'U:\shimonc\gen6\pd69201_top_recordings\port_on_short\set_signal_file.txt'
    # db = VCDToAnalog(vcd_source, vcd_target, vcd_info)
    # db.generate_reduced_vcd()
    # print(db.show_start_time('1ms'))
    # print(db.show_end_time('1ms'))
    # print(db.show_sim_time('1ms'))
    # print(db.find_bit_change('port_off_d', '1', 'ms'))
    # print(db.find_bit_change('port_off_d', '0', 'ms'))
    # print(db.find_bit_change('class_en_d', '1', 'ms'))
    # print(db.find_bit_change('class_en_d', '0', 'ms'))
    # db.set_signals(set_signal_file)
    # attri_dict = {'trise': '10ns', 'tfall': '10ns', 'vih': 5, 'vil': 0.0, 'vol': 0.0, 'voh': 5}
    # db.set_all_attributes(attri_dict)

    # start up from mark
    # vcd_source = r'U:\shimonc\gen6\pd69201_top_recordings\pd69201_vcd_su_from_mark.vcd'
    # vcd_target = r'U:\shimonc\gen6\pd69201_top_recordings\start_up_from_mark\sim_new.vcd'
    # vcd_info = r'U:\shimonc\gen6\pd69201_top_recordings\start_up_from_mark\sim_info.info'
    # set_signal_file = r'U:\shimonc\gen6\pd69201_top_recordings\start_up_from_mark\set_signal_file.txt'
    # db = VCDToAnalog(vcd_source, vcd_target, vcd_info)
    # db.generate_reduced_vcd()
    # print(db.show_start_time('1ms'))
    # print(db.show_end_time('1ms'))
    # print(db.show_sim_time('1ms'))
    # print(db.find_bit_change('port_off_d', '1', 'ms'))
    # print(db.find_bit_change('port_off_d', '0', 'ms'))
    # print(db.find_bit_change('class_en_d', '1', 'ms'))
    # print(db.find_bit_change('class_en_d', '0', 'ms'))
    # db.set_signals(set_signal_file)
    # attri_dict = {'trise': '10ns', 'tfall': '10ns', 'vih': 5, 'vil': 0.0, 'vol': 0.0, 'voh': 5}
    # db.set_all_attributes(attri_dict)

    # start up
    # vcd_source = r'U:\shimonc\gen6\pd69201_top_recordings\pd69201_vcd_dump_res_det_to_ovl.vcd'
    # vcd_target = r'U:\shimonc\gen6\pd69201_top_recordings\startup\sim_new.vcd'
    # vcd_info = r'U:\shimonc\gen6\pd69201_top_recordings\startup\sim_info.info'
    # set_signal_file = r'U:\shimonc\gen6\pd69201_top_recordings\startup\set_signal_file.txt'
    # db = VCDToAnalog(vcd_source, vcd_target, vcd_info)
    # db.generate_reduced_vcd()
    # print(db.show_start_time('1ms'))
    # print(db.show_end_time('1ms'))
    # print(db.show_sim_time('1ms'))
    # print(db.find_bit_change('port_off_d', '1', 'ms'))
    # print(db.find_bit_change('port_off_d', '0', 'ms'))
    # print(db.find_bit_change('class_en_d', '1', 'ms'))
    # print(db.find_bit_change('class_en_d', '0', 'ms'))
    # db.set_signals(set_signal_file)
    # attri_dict = {'trise': '10ns', 'tfall': '10ns', 'vih': 5, 'vil': 0.0, 'vol': 0.0, 'voh': 5}
    # db.set_all_attributes(attri_dict)

    # ovt
    # vcd_source = r'U:\shimonc\gen6\pd69201_top_recordings\pd69201_vcd_ovt.vcd'
    # vcd_target = r'U:\shimonc\gen6\pd69201_top_recordings\ovt\sim_new.vcd'
    # vcd_info = r'U:\shimonc\gen6\pd69201_top_recordings\ovt\sim_info.info'
    # set_signal_file = r'U:\shimonc\gen6\pd69201_top_recordings\ovt\set_signal_file.txt'
    # db = VCDToAnalog(vcd_source, vcd_target, vcd_info)
    # db.generate_reduced_vcd()
    # print(db.show_start_time('1ms'))
    # print(db.show_end_time('1ms'))
    # print(db.show_sim_time('1ms'))
    # print(db.find_bit_change('port_off_d', '1', 'ms'))
    # print(db.find_bit_change('port_off_d', '0', 'ms'))
    # print(db.find_bit_change('class_en_d', '1', 'ms'))
    # print(db.find_bit_change('class_en_d', '0', 'ms'))
    # db.set_signals(set_signal_file)
    # attri_dict = {'trise': '10ns', 'tfall': '10ns', 'vih': 5, 'vil': 0.0, 'vol': 0.0, 'voh': 5}
    # db.set_all_attributes(attri_dict)

    # sectional ams
    # vcd_source = r'U:\shimonc\gen6\pd69201_top_recordings\pd69201_vcd_dump_res_det_to_ovl.vcd'
    # vcd_target = r'U:\shimonc\gen6\pd69201_top_recordings\sectional_ams\sim_new.vcd'
    # vcd_info = r'U:\shimonc\gen6\pd69201_top_recordings\sectional_ams\sim_info.info'
    # set_signal_file = r'U:\shimonc\gen6\pd69201_top_recordings\sectional_ams\set_signal_file.txt'
    # db = VCDToAnalog(vcd_source, vcd_target, vcd_info)
    # db.generate_reduced_vcd('20ms')
    # print(db.show_start_time('1ms'))
    # print(db.show_end_time('1ms'))
    # print(db.show_sim_time('1ms'))
    # print(db.find_bit_change('port_off_d', '1', 'ms'))
    # print(db.find_bit_change('port_off_d', '0', 'ms'))
    # print(db.find_bit_change('class_en_d', '1', 'ms'))
    # print(db.find_bit_change('class_en_d', '0', 'ms'))
    # db.set_signals(set_signal_file)
    # attri_dict = {'trise': '10ns', 'tfall': '10ns', 'vih': 5, 'vil': 0.0, 'vol': 0.0, 'voh': 5}
    # db.set_all_attributes(attri_dict)

    # print(db.find_bit_change('res_det_block_en_d', '1', 'ps'))
    # print(db.find_bit_change('generate_slope_d', '1', 'ms'))
    # print(db.find_bit_change('port_off_d', '0', 'ms'))
    # print(db.find_bit_change('accumulator[3:0]', 'b1010', 'ns'))

    # attri_dict = {'trise': '10ns', 'tfall': '10ns', 'vih': 5, 'vil': 0.0, 'vol': 0.0, 'voh': 5}
    # db.set_all_attributes(attri_dict)
    #
    # db.slice_vcd('2550ms', '2630ms')
    # db.set_signals(set_signal_file)
    # db.generate_reduced_vcd()
    # #

    # plot_ob = db.signals_to_plot('class_en_d', 'generate_slope_d')
    # pso = PlotSignals(plot_ob)
    # pso.plot_signals()

    # db.remove_consecutive_duplicates()

    # db.get_signal_info('CLK_25MHZ')
    # db.get_signal_info('accumulator[3:0]')
    # db.remove_consecutive_duplicates()

    # db.generate_reduced_vcd()
    # db.generate_reduced_vcd('1ms')
    # print(db.find_bit_change('res_det_block_en_d', '1', 'ms'))
    # print(db.find_bit_change('class_en_d', '1', 'ms'))
    # db.slice_vcd('0ms', '510ms')
    # db.set_signals(set_signal_file)

    # sig_dict = {'15MHz_CLK': {'300ns': '0', '350ns': '1'}, '5MHz_CLK': {'65000ps': '1', '133ns': '0'}}
    # sig_dict = {'5MHz_CLK': {'65ns': '1', '133ns': '0'}}
    # sig_dict = {'5MHz_CLK': {'420ns': '1', '450ns': '0'}}
    # sig_dict = {'accumulator[3:0]': {'400ns': 'b1010'}}

    # db.change_signals_value(sig_dict)

    # db.slice_vcd('142ns', '472ns')
    # db.slice_vcd('125ns', '220ns')
    # db.slice_vcd('142ns', '472ns', True, '170ns')

    # db.slice_vcd('2000024254000ps', '2504023254000ps')
    # db.set_signals(set_signal_file)

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

    # help(db)
    # help(db.remove_consecutive_duplicates)


if __name__ == "__main__":
    main()
