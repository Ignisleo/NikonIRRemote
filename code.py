# IR Remote control for a Nikon DSLR
# implemented on an Adafruit Circuit Playground Express
# written by Oliver von Sehlen, 2018
# MIT license, see LICENSE file
# ===================================
# When button A on the Circuit Playground Express is pressed,
# the program transmits a shutter command to the DSLR using
# the onboard IR LED.
# Possible improvement: Use an external pin to drive an external
# high-power IR LED for improved range.

# Library imports
# Pin definitions
import board
# pulse train generation
import pulseio
# digital in- and output
import digitalio
# generic timing functions, necessary for time.sleep
import time
# array handling to store the pulse train
import array

# Trigger switch
shutter_switch = digitalio.DigitalInOut(board.BUTTON_A)
shutter_switch.direction = digitalio.Direction.INPUT
shutter_switch.pull = digitalio.Pull.DOWN

# The carrier signal, 38400 Hz, 50% duty cycle and the pulseout object
pwm = pulseio.PWMOut(board.IR_TX, duty_cycle=2 ** 15, frequency=38400)
ir_out = pulseio.PulseOut(pwm)
# The pulse train, according to alanmacek.com/nikon
shutter_cmd = array.array('H', [2000, 27800, 500, 1500, 500, 3500, 500,
63000, 2000, 27800, 500, 1500, 500, 3500, 500])

while True:
    if shutter_switch.value:
        ir_out.send(shutter_cmd)
        print("Shutter cmd sent!")
        time.sleep(0.1)