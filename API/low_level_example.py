# import pyrpl library
import pyrpl

# create an interface to the Red Pitaya
r = pyrpl.Pyrpl(config='',hostname='192.168.6.100').redpitaya

r.hk.led = 0b10101010  # change led pattern

# measure a few signal values
print("Voltage at analog input1: %.3f" % r.sampler.in1)
print("Voltage at analog output2: %.3f" % r.sampler.out2)
print("Voltage at the digital filter's output: %.3f" % r.sampler.iir)

# output a function U(t) = 0.5 V * sin(2 pi * 10 MHz * t) to output2
r.asg0.setup(waveform='sin',
             amplitude=0.5,
             frequency=10e6,
             output_direct='out2')

# demodulate the output signal from the arbitrary signal generator
r.iq0.setup(input='asg0',   # demodulate the signal from asg0
            frequency=10e6,  # demodulaltion at 10 MHz
            bandwidth=1e5)  # demodulation bandwidth of 100 kHz

# set up a PID controller on the demodulated signal and add result to out2
r.pid0.setup(input='iq0',
             output_direct='out2',  # add pid signal to output 2
             setpoint=0.05, # pid setpoint of 50 mV
             p=0.1,  # proportional gain factor of 0.1
             i=100,  # integrator unity-gain-frequency of 100 Hz
            #  input_filter = [3e3, 10e3]
             )  # add 2 low-passes (3 and 10 kHz)

# modify some parameters in real-time
r.iq0.frequency += 2.3  # add 2.3 Hz to demodulation frequency
r.pid0.i *= 2  # double the integrator unity-gain-frequency

# take oscilloscope traces of the demodulated and pid signal
data = r.scope.curve(input1='iq0', input2='pid0',
                     duration=1.0, trigger_source='immediately')