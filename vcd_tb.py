from vcd_generator import VCDToAnalog
from plot_signals import PlotSignals
import time


def main():
    # vcd_source = r'U:\shimonc\gen6\signal_crt_analog_3.vcd'
    # vcd_target = r'U:\shimonc\gen6\signal_crt_analog_3_new.vcd'
    # vcd_info = r'U:\shimonc\gen6\signal_crt_analog_3_info.info'

    vcd_source = r'signal_crt_analog_3.vcd'
    vcd_target = r'signal_crt_analog_3_new.vcd'
    vcd_info = r'signal_crt_analog_3_info.info'

    # vcd_source = r'pd69201_vcd_dump_res_det_to_ovl.vcd'
    # vcd_target = r'pd69201_new.vcd'
    # vcd_info = r'pd69201_info.info'

    db = VCDToAnalog(vcd_source, vcd_target, vcd_info)
    # db.get_signal_info('CLK_25MHZ')

    # db.show_start_time('1ns')
    # db.show_end_time('1ns')
    # db.show_sim_time('1ns')

    # db.generate_reduced_vcd()
    # db.generate_reduced_vcd('1us')

    # sig_dict = {'15MHz_CLK': {'300ns': '0', '350ns': '1'}, '5MHz_CLK': {'65000ps': '1', '133ns': '0'}}
    # sig_dict = {'5MHz_CLK': {'65ns': '1', '133ns': '0'}}
    # sig_dict = {'5MHz_CLK': {'420ns': '1', '450ns': '0'}}
    # sig_dict = {'accumulator[3:0]': {'400ns': 'b1010'}}
    #
    # db.change_signals_value(sig_dict)

    # db.slice_vcd('142ns', '472ns')
    # db.slice_vcd('142ns', '472ns', True, '170ns')
    # db.slice_vcd('142ns', '472ns', True, '1000ns')

    # attri_dict = {'trise': '10ns', 'tfall': '10ns', 'vih': 2.3, 'vil': 0.05, 'vol': 0.00001, 'voh': 2.5}
    # db.set_all_attributes(attri_dict)

    # db.set_signal_attributes('CLK_25MHZ', 'vih', 1.8)
    # db.set_signal_attributes('CLK_25MHZ', 'trise', '10000ps')
    # db.set_signal_attributes('CLK_25MHZ', 'trise', '10ns')

    # plot_ob = db.signals_to_plot('5MHz_CLK')
    # plot_ob = db.signals_to_plot('CLK_25MHZ', 'CLK_160MHZ', '15MHz_CLK', '5MHz_CLK')
    # pso = PlotSignals(plot_ob)
    # pso.plot_signals()

    # print(db.__repr__('CLK_25MHZ'))
    # print(db.__str__())

    # print(db.__repr__(r'vmode_vmeas_sel_d[1:0]'))

    # db.remove_consecutive_duplicates()

    seq_list = ['CLK_25MHZ', '1', '0']
    db.find_sequence(seq_dict)


if __name__ == "__main__":
    main()
