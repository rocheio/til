Make Terminal Auto-Complete Case-Insensitive
============================================

*From [bodhi.zazen and mwfearnley](http://askubuntu.com/questions/87061/can-i-make-tab-auto-completion-case-insensitive-in-the-terminal)*

First, make sure you have a `~./inputrc` file set as your input configuration file. Then, put the command `set completion-ignore-case On` in that file to make the auto-complete feature case-insensitive.

```bash
# If ~./inputrc doesn't exist yet, first include the original /etc/inputrc so we don't override it
if [ ! -a ~/.inputrc ]; then echo "\$include /etc/inputrc" > ~/.inputrc; fi

# Add option to ~/.inputrc to enable case-insensitive tab completion
echo "set completion-ignore-case On" >> ~/.inputrc
```