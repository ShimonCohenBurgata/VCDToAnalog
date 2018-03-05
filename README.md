This project is under construction
!!!!! Not stable yet !!!!!!!


# VCDToAnalog
Generate analog info file from digital VCD (Value Changed Dump)

This code can also manipulate the data.
this allows to simulate the circuit with some changes compered to the original vcd.
New methods for data manipulation and data presentation will add in the future

an example on how to work with the code can be seen in vcd_tb.py file.

following is an instruction on how to work with the methods.

-------Action-----------------
Created an VCDTo analog object
create copied vcd file
create info file

-------Command--------------------
>>> vcd_source = r'signal_crt_analog_3.vcd'
>>> vcd_target = r'signal_crt_analog_3_new.vcd'
>>> vcd_info = r'signal_crt_analog_3_info.info'
>>> db = VCDToAnalog(vcd_source, vcd_target, vcd_info)

--------------Start stop and simulation time presentation-------------------
Shows the simulation start end and simulation time
the input is the time scale units.
the string part can be one of the following option ps, ns, us, ms, s
the integer part can be anything although 1 is the most used value

-------Action----------------
1. Show simulation start time in 1 nano second units
2. Show simulation end time in 1 nano second units
3. Show simulation time in 100 pico seconds units
4. Show simulation time in 1 nano second units


------Command----------------
>>> db.show_start_time('1ns')
>>> db.show_end_time('1ns')
>>> db.show_sim_time('100ps')
>>> db.show_sim_time('1ns')

------Results----------------
>>> start time is 0.0(1ns)
>>> end time is 500.0(1ns)
>>> simulation time is 5000.0(100ps)
>>> simulation time is 500.0(1ns)

--------------Reduce vcd start time simulation-------------------------------------
In some of the vcd files the dump is been done in times different than 0
generate_reduced_vcd can scale all the time steps to zero while the duration between time steps is not changing
on the contrary if the dump vars start at 0 and the user want to add delay he can do it with this function.
It also possible to combine the operations first the reduce the vcd file and than add some delay
the input can left blank which means no delay will be added
if delay is need it can be add in the following way
the string part can be one of the following option ps, ns, us, ms, s
the integer part can be any integer
Lets see some example

------ Action---------------
reduce vcd so that start time is 0

------Command----------------
db.generate_reduced_vcd()

------Before change----------
#10
$dumpvars
1!
0"
1^
0(
$end
#20
------After change------------
#0
$dumpvars
1!
0"
1^
0(
$end
#10

---------Action--------------
reduced vcd so that start time is 5 nano seconds

------Command----------------
db.generate_reduced_vcd('5ns')

------After change------------
#5
$dumpvars
1!
0"
1^
0(
$end
#15

----------- Change signal values -------------------
If the user want to change the signal value at a specific time
he can do it using the method change_signals_value
the input to this method is a dictionary with signal names as keys
an additional dictionary as values.
the values dictionary contain pairs of time steps and signal values
the string part can be one of the following option ps, ns, us, ms, s
the integer part can be any integer
for example:

>>> sig_dict = {'CLK_160MHZ': {'520ns': '1', '540ns': '0'}, 'CLK_25MHZ': {'520ns': '0'}}

---------Action--------------
change the signal CLK_25MHZ at 20ns from '0' to '1'
at this example the wildcard of signal CLK_25MHZ is !

$var wire 1 ! CLK_25MHZ $end

----------Command-------------
db.change_signals_value({'CLK_25MHZ': {'20ns': '1'}})

------Before change----------
#20
0!
0"
1^

------After change----------
#20
1!
0"
1^

---------Action--------------
add value to  signal CLK_25MHZ at 24ns
24ns is not part of the original vcd file
at this example the wildcard of signal CLK_25MHZ is !
$var wire 1 ! CLK_25MHZ $end

----------Command-------------
db.change_signals_value({'CLK_25MHZ': {'24ns': '1'}})

--------------After change -------------------------
#20     |
0!      |
0"      |
1^      |
#24   <-|
1!
#40
1!
0"
0^

---------Action--------------
change few signals at few time steps

----------Command-------------
>>> sig_dict = {'CLK_160MHZ': {'520ns': '1', '540ns': '0'}, 'CLK_25MHZ': {'520ns': '0'}}
>>> db.change_signals_value(sig_dict)


------------------ Slicing the vcd file----------------------------
In case that the user wants to run a specific section of the vcd
with out the need to wait for the simulation to reach this point
the method slice_vcd can be used.
the inputs to this method are:
arg 1 (str) --> slice start time
arg 2 (str) --> slice end time
arg 3 (bool) --> if reduction to zero is wanted
arg4 (str) --> if reduction to zero + delay is wanted

---------Action--------------
>>> slice vcd from '20ns' to '40ns'

---------Command--------------
>>> db.slice_vcd('20ns', '40ns')

------Before change----------
#10
$dumpvars
1!
0"
1^
0(
$end
#20
0!
0"
1^
#40
1!
0"
0^
#60
0!
1"
0^

------After change----------
#20
0!
0"
1^
#40

---------Action--------------
>>> slice vcd from '20ns' to '40ns' and then reduce to zero

---------Command--------------
>>> db.slice_vcd('20ns', '40ns', True)

-----------After change---------------
#0
0!
0"
1^
#20

---------Action--------------
>>> slice vcd from '20ns' to '40ns' reduce to zero and add '5ns'

---------Command--------------
>>> db.slice_vcd('20ns', '40ns', True, '5ns')

----------After change--------------------
#5
0!
0"
1^
#25

-----------------Change signal attributes -------------------
each signal has 6 attributes
trise - signal rise time
tfall - signal fall time
vil - input low voltage value
vih - input high voltage value
vol - output low voltage value
voh - output high voltage value.
the default values are:
{'trise': 0.1, 'tfall': 0.1, 'vih': 2.0, 'vil': 0.0, 'vol': 0.00001, 'voh': 1.6}
the user can change the attributes of a specific signal using the method set_signal_attributes
the input to this method are
arg 1 (str) - signal name
arg 2 (str) - signal attribute
arg 3 (float) - attribute value

---------------------Action------------------
Change the input low voltage value of signal CLK_25MHZ from default 2.0
to 1.8

-------------------Command-----------------------
>>> db.set_signal_attributes('CLK_25MHZ', 'vih', 1.8)

-----------------Before change-------------------
.in CLK_25MHZ
.vih 2.0 CLK_25MHZ

------------After change-----------------------
.in CLK_25MHZ
.vih 1.8 CLK_25MHZ

---------------------Action------------------
find the times where a value of a signal is been set in the vcd file

-------------------Command-----------------------
print(db.find_bit_change('5MHz_CLK', '1', 'ns'))



-------------Change attribute to all signals -------------
the default signals attributes are:
{'trise': 0.1, 'tfall': 0.1, 'vih': 2.0, 'vil': 0.0, 'vol': 0.00001, 'voh': 1.6}
if the user want to change the atrributes to the entire data base he can use the method
set_all_attributes
the input to this method is the same dictionary with different value
the dictionary can contain 1 or more attributes, it doesnt need to contain all attributes

--------Action----------------------------
change the entire data base to the next attributes
{'trise': 0.2, 'tfall': 0.2, 'vih': 3.3, 'vil': 0.05, 'vol': 0.00001, 'voh': 2.5}

--------Command---------------------------------
>>> attri_dict = {'trise': 0.2, 'tfall': 0.2, 'vih': 3.3, 'vil': 0.05, 'vol': 0.00001, 'voh': 2.5}
>>> db.set_all_attributes(attri_dict)

------------- Before change-----------------------------
.in CLK_25MHZ
.vih 2.0 CLK_25MHZ
.vil 0.0 CLK_25MHZ
.trise 0.1 CLK_25MHZ
.tfall 0.1 CLK_25MHZ

.in CLK_160MHZ
.vih 2.0 CLK_160MHZ
.vil 0.0 CLK_160MHZ
.trise 0.1 CLK_160MHZ
.tfall 0.1 CLK_160MHZ

----------After change------------------------------
.in CLK_160MHZ
.vih 3.3 CLK_160MHZ
.vil 0.05 CLK_160MHZ
.trise 0.2 CLK_160MHZ
.tfall 0.2 CLK_160MHZ

.in CLK_25MHZ
.vih 3.3 CLK_25MHZ
.vil 0.05 CLK_25MHZ
.trise 0.2 CLK_25MHZ
.tfall 0.2 CLK_25MHZ

------------data base representation-----------------
it is possible to see the data base representation using
the __repr__() method
it also possible to represent a signal data

----------Action----------------
see the data base representation

-------Command -----------------
print(db.__repr__())

----------Results---------------
"
	tv
		[(5, '0')]
	nets
		[{'size': '1', 'hier': '', 'name': 'CLK_160MHZ', 'type': 'wire'}]
^
	tv
		[(5, '1')]
	nets
		[{'size': '1', 'hier': 'I1', 'name': '5MHz_CLK', 'type': 'wire'}]
(
	nets
		[{'size': '1', 'hier': 'I1.I13', 'name': '15MHz_CLK', 'type': 'wire'}]
!
	tv
		[(5, '0')]
	nets
		[{'size': '1', 'hier': '', 'name': 'CLK_25MHZ', 'type': 'wire'}]

-------Action-------------------
See the representation of signal CLK_25MHZ

-------Command -----------------
 print(db.__repr__('CLK_25MHZ'))

----------Results---------------
!
    [{'size': '1', 'name': 'CLK_25MHZ', 'hier': '', 'type': 'wire'}]
    [(5, '0')]


------Action----------------------
Plot the signals CLK_25MHZ, CLK_160MHZ, 15MHz_CLK

-------Command -----------------
>>> plot_ob = db.signals_to_plot('CLK_25MHZ', 'CLK_160MHZ', '15MHz_CLK')
>>> pso = PlotSignals(plot_ob)
>>> pso.plot_signals()












