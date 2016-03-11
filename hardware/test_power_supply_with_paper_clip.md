Test a Computer Power Supply with a Paper Clip
==============================================

When a desktop computer will not turn on at all, or is experiencing weird boot cycles[1], one of the first pieces of hardware to check should be the power supply. Here is [the guide](http://dodji.seketeli.com/downloads/shuttle-psu-paper-clip-test.pdf) I used to test my power supply, summarized below:

1. Shut down the computer
2. Unplug it from the electrical outlet and flip battery switch to 'off'
3. Remove all power cables from other computer components
4. Plug the now standalone power supply back into the wall
5. Get the 24-Pin ATX power cable (the big one) that connects the battery to the motherboard
6. Identify the green pin (pin 16 - power supply ON) and any black grounding pin (pin 17 right next to it)
7. Bend a paperclip into a 'U' shape, and put the ends into those two pins

If the fan on the power supply starts, then it is working properly, and the issue is almost certainly another piece of hardware.


[1]: In my recent experience, my computer would boot for 10 seconds, almost enough to enter the boot loader, then turn off and reboot itself. This occured right after installing a new solid state drive, and ended up being caused by a bad motherboard.
