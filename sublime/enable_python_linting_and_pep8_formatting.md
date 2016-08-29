# Enable Python Linting and PEP-0008 Formatting in Sublime Text 3

Because [Sublime Text 3](https://www.sublimetext.com/3) has a robust plugin ecosystem and package manager, it is quite easy to turn your favorite text editor into a full-fledged Python IDE.

If you don't have it already, you must first install the [Package Control](https://packagecontrol.io/installation#st3) plugin for Sublime. Copy the code for Sublime Text 3 from that link, open the Sublime console using ``ctrl + ` ``, paste and run the code in Sublime, then restart the program.

Once Package Control is available, access it using `ctrl + shift + p` in Sublime. Search for and select _'Package Control: Install Package'_, then search for and install the [Anaconda](http://damnwidget.github.io/anaconda/) package. Restart the program.

To test your new linter and styler, open up a `.py` file in Sublime, hit `ctrl + shift + p`, then search and select _'Anaconda: show error list'_.

To autoformat your PEP-0008 errors, you can simply hit `ctrl + alt + r` from within a `.py` file.
