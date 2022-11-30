import sys
import linuxcnc


c = linuxcnc.command()

c.teleop_enable(0)
c.wait_complete() # wait until the teleop mode is disable
c.unhome(4)
c.wait_complete() # wait until joint 0 is unhomed
c.home(4)
c.wait_complete() # wait until joint 0 is homed
c.teleop_enable(1)
