# ボタンAをおすとうなづく

from m5stack import *
from m5ui import *
from uiflow import *
import machine
import time

setScreenColor(0x222222)

# Describe this function...
def agree():
  PWM0 = machine.PWM(2, freq=50, duty=7.5, timer=0)
  wait_ms(1000)
  PWM0 = machine.PWM(2, freq=50, duty=6, timer=0)
  wait_ms(1000)
  PWM0 = machine.PWM(2, freq=50, duty=7.5, timer=0)
  wait_ms(1000)
  PWM0 = machine.PWM(2, freq=50, duty=6, timer=0)
  wait_ms(1000)
  PWM0 = machine.PWM(2, freq=50, duty=7.25, timer=0)


def buttonA_wasPressed():
  # global params
  agree()
  pass
btnA.wasPressed(buttonA_wasPressed)


PWM2 = machine.PWM(5, freq=50, duty=7.25, timer=0)
PWM0 = machine.PWM(2, freq=50, duty=7.25, timer=0)
