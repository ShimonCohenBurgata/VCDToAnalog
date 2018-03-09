import pytest
from vcd_to_analog.vcd_generator import VCDToAnalog
import os
from collections import OrderedDict
import re

os.chdir('vcd_and_info_files')
file_path = os.getcwd()


# @pytest.mark.skip(reason="stam")
def test_remove_consecutive_duplicates():
    vcd_source = os.path.join(file_path, 'sim_cons.vcd')  # path to file with consecutive duplicates
    vcd_target = os.path.join(file_path, 'sim_new.vcd')  # path to file after cleaning consecutive duplicates
    vcd_info = os.path.join(file_path, 'sim_info.info')  # path to info file
    db_cons = VCDToAnalog(vcd_source, vcd_target, vcd_info)  # generate vcd to analog object
    vcd_expected = os.path.join(file_path, 'sim_no_cons.vcd')  # path to comparision file
    db_cons.remove_consecutive_duplicates()  # remove consecutive duplicates
    fh_result = open(vcd_target, 'r')  # read result file
    fh_expected = open(vcd_expected, 'r')  # read comparison file
    assert fh_result.read().splitlines() == fh_expected.read().splitlines()  # assert that files are equal
    fh_expected.close()  # close files
    fh_result.close()


# @pytest.mark.skip(reason="stam")
def test_show_start_time():
    vcd_source = os.path.join(file_path, 'sim.vcd')  # path to vcd file
    vcd_target = os.path.join(file_path, 'sim_new.vcd')  # path to new vcd file
    vcd_info = os.path.join(file_path, 'sim_info.info')  # path to info file
    db_show_time = VCDToAnalog(vcd_source, vcd_target, vcd_info)  # generate vcd to analog object
    assert db_show_time.show_start_time('1ns') == 'start time is 4.0(1ns)'
    assert db_show_time.show_end_time('1ns') == 'end time is 500.0(1ns)'
    assert db_show_time.show_sim_time('1ns') == 'simulation time is 496.0(1ns)'


# @pytest.mark.skip(reason="stam")
def test_generate_reduced_vcd():
    vcd_source = os.path.join(file_path, 'sim.vcd')  # path to vcd file
    vcd_target = os.path.join(file_path, 'sim_new.vcd')  # path to new vcd file
    vcd_info = os.path.join(file_path, 'sim_info.info')  # path to info file
    vcd_expected = os.path.join(file_path, 'sim_reduced.vcd')  # path to comparision file
    db_reduced = VCDToAnalog(vcd_source, vcd_target, vcd_info)  # generate vcd to analog object
    db_reduced.generate_reduced_vcd()
    fh_result = open(vcd_target, 'r')  # read result file
    fh_expected = open(vcd_expected, 'r')  # read comparison file
    assert fh_result.read().splitlines() == fh_expected.read().splitlines()  # assert that files are equal
    fh_expected.close()  # close files
    fh_result.close()


# @pytest.mark.skip(reason="stam")
def test_generate_reduced_delay_vcd():
    vcd_source = os.path.join(file_path, 'sim.vcd')  # path to vcd file
    vcd_target = os.path.join(file_path, 'sim_new.vcd')  # path to new vcd file
    vcd_info = os.path.join(file_path, 'sim_info.info')  # path to info file
    vcd_expected = os.path.join(file_path, 'sim_reduced_delay.vcd')  # path to comparision file
    db_reduced = VCDToAnalog(vcd_source, vcd_target, vcd_info)  # generate vcd to analog object
    db_reduced.generate_reduced_vcd('14ns')
    fh_result = open(vcd_target, 'r')  # read result file
    fh_expected = open(vcd_expected, 'r')  # read comparison file
    assert fh_result.read().splitlines() == fh_expected.read().splitlines()  # assert that files are equal
    fh_expected.close()  # close files
    fh_result.close()


# @pytest.mark.skip(reason="stam")
def test_change_signals_value():
    vcd_source = os.path.join(file_path, 'sim.vcd')  # path to vcd file
    vcd_target = os.path.join(file_path, 'sim_new.vcd')  # path to new vcd file
    vcd_info = os.path.join(file_path, 'sim_info.info')  # path to info file
    vcd_expected = os.path.join(file_path, 'sim_change.vcd')  # path to comparision file
    db_change = VCDToAnalog(vcd_source, vcd_target, vcd_info)  # generate vcd to analog object
    sig_dict = {'15MHz_CLK': {'300ns': '0', '350ns': '1'}, '5MHz_CLK': {'65000ps': '1', '133ns': '0'}}
    db_change.change_signals_value(sig_dict)
    fh_result = open(vcd_target, 'r')  # read result file
    fh_expected = open(vcd_expected, 'r')  # read comparison file
    assert fh_result.read().splitlines() == fh_expected.read().splitlines()  # assert that files are equal
    fh_expected.close()  # close files
    fh_result.close()


# @pytest.mark.skip(reason="stam")
def test_slice():
    vcd_source = os.path.join(file_path, 'sim.vcd')  # path to vcd file
    vcd_target = os.path.join(file_path, 'sim_new.vcd')  # path to new vcd file
    vcd_info = os.path.join(file_path, 'sim_info.info')  # path to info file
    vcd_expected = os.path.join(file_path, 'sim_slice.vcd')  # path to comparision file
    db_slice = VCDToAnalog(vcd_source, vcd_target, vcd_info)  # generate vcd to analog object
    db_slice.slice_vcd('125ns', '220ns')
    fh_result = open(vcd_target, 'r')  # read result file
    fh_expected = open(vcd_expected, 'r')  # read comparison file
    assert fh_result.read().splitlines() == fh_expected.read().splitlines()  # assert that files are equal
    fh_expected.close()  # close files
    fh_result.close()


# @pytest.mark.skip(reason="stam")
def test_find_bit_change():
    vcd_source = os.path.join(file_path, 'sim.vcd')  # path to vcd file
    vcd_target = os.path.join(file_path, 'sim_new.vcd')  # path to new vcd file
    vcd_info = os.path.join(file_path, 'sim_info.info')  # path to info file
    db_find_bit_change = VCDToAnalog(vcd_source, vcd_target, vcd_info)  # generate vcd to analog object

    od_expected = OrderedDict()
    od_expected[1] = '4.0ns'
    od_expected[2] = '20.0ns'
    od_expected[3] = '200.0ns'
    od_expected[4] = '220.0ns'
    od_expected[5] = '400.0ns'
    od_expected[6] = '420.0ns'

    od_result = db_find_bit_change.find_bit_change('5MHz_CLK', '1', 'ns')
    for key in od_expected.keys():
        assert od_expected[key] == od_result[key]


# @pytest.mark.skip(reason="stam")
def test_set_all_attributes():
    vcd_source = os.path.join(file_path, 'sim.vcd')  # path to vcd file
    vcd_target = os.path.join(file_path, 'sim_new.vcd')  # path to new vcd file
    vcd_info = os.path.join(file_path, 'sim_info.info')  # path to info file
    db_set_all_attributes = VCDToAnalog(vcd_source, vcd_target, vcd_info)  # generate vcd to analog object
    test_dict = {'trise': '10ns', 'tfall': '10ns', 'vih': 2.4, 'vil': 0.05, 'vol': 0.00001, 'voh': 2.5}
    db_set_all_attributes.set_all_attributes(test_dict)
    with open(vcd_info, 'r') as fo:
        lines = fo.read().splitlines()

    for line in lines:
        mo = re.search(r'^\.({}) (.+) (.*)'.format('trise|tfall|vih|vil|vol|voh'), line)
        if mo:
            assert test_dict[mo.group(1)] == float(mo.group(2))


