from vcd_generator import VCDToAnalog


def main():
    # sig_dict1 = {'CLK_160MHZ': {'5ns': '1'}}
    # sig_dict2 = {'CLK_25MHZ': {'520ns': '0'}}

    vcd_source = r'signal_crt_analog_3.vcd'
    vcd_target = r'signal_crt_analog_3_new.vcd'
    vcd_info = r'signal_crt_analog_3_info.info'

    db = VCDToAnalog(vcd_source, vcd_target, vcd_info)
    # db.get_signal_info('CLK_25MHZ')
    # print(db.get_signal_info('CLK_25MHZ'))

    # db.generate_reduced_vcd()
    # db.generate_reduced_vcd('5ns')

    # sig_dict = {'CLK_160MHZ': {'520ns': '1', '540ns': '0'}, 'CLK_25MHZ': {'520ns': '0'}}
    # db.change_signals_value(sig_dict)
    # db.change_signals_value({'CLK_25MHZ': {'24ns': '1'}})
    # db.slice_vcd('20ns', '40ns', True, '5ns')
    db.slice_vcd('20ns', '40ns', True, '5ns')

    # db.show_start_time('1ns')
    # db.show_end_time('1ns')
    # db.show_sim_time('100ps')
    # db.show_sim_time('1ns')

    # attri_dict = {'trise': 0.2, 'tfall': 0.2, 'vih': 3.3, 'vil': 0.05, 'vol': 0.00001, 'voh': 2.5}
    # db.set_all_attributes(attri_dict)

    # db.set_signal_attributes('CLK_25MHZ', 'vih', 1.8)
    # db.set_signal_attributes('CLK_25MHZ', 'trise', 10)
    # db.set_signal_attributes('CLK_25MHZ', 'tfall', 10)

    print(db.__repr__('CLK_25MHZ'))


if __name__ == "__main__":
    main()
