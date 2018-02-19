from vcd_generator import VCDToAnalog


def main():
    # sig_dict1 = {'CLK_160MHZ': {'5ns': '1'}}
    # sig_dict2 = {'CLK_25MHZ': {'520ns': '0'}}
    sig_dict = {'CLK_160MHZ': {'520ns': '1', '540ns': '0'}, 'CLK_25MHZ': {'520ns': '0'}}
    vcd_source = r'signal_crt_analog_3.vcd'
    vcd_target = r'signal_crt_analog_3_new.vcd'
    vcd_info = r'signal_crt_analog_3_info.info'

    db = VCDToAnalog(vcd_source, vcd_target, vcd_info)
    # db.get_signal_info('CLK_25MHZ')
    # print(db.get_signal_info('CLK_25MHZ'))
    # db.generate_reduced_vcd('10ns')
    # db.change_signals_value(sig_dict)
    # db.slice_vcd('130ns', '380ns', True, '100ns')

    # db.show_start_time('1ns')
    # db.show_end_time('shimon')
    # db.show_sim_time('1ns')

    # db.set_signal_attributes('CLK_25MHZ', 'vih', 2.5)
    # db.set_signal_attributes('CLK_25MHZ', 'trise', 10)
    # db.set_signal_attributes('CLK_25MHZ', 'tfall', 10)


if __name__ == "__main__":
    main()
