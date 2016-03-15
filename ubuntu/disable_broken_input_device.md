Disable a Broken Input Device
=============================

If you are having trouble with an input device[1], the following steps will help identify and disable it (assuming you have access to a working keyboard).

Open a terminal window using the keyboard shortcut `ctrl + alt + t`. List all current input devices using `xinput --list`. Identify a device that could be causing your issues, let's say it's '12', and examine it further using `xinput --list 12`.

There will be a lot of crazy stuff about 'Valuators', but look for a line at the top that reads 'This device is disabled' above the line 'Reporting # classes:'. If the device is not disabled and you do not want to use it, disable it using `xinput --disable 12`.


[1] I had a PS3 controller adapter plugged into my computer, which works on Windows, but not Ubuntu. At some point this activated as a pointing device, causing a jittery mouse effect that fought against my normal mouse movements.