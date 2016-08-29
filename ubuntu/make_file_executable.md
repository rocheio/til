# Make a File Executable from Command Line

*from [fge](http://stackoverflow.com/a/8779980)*

So far, this has been one of my favorite tricks since switching to Linux. To make a file executable, just add a *sha-bang* line (`#/bin/bash`) as the very first line in a script. Then, make the file executable with the command `chmod u+x script.sh`.

Now, you can run the script just by navigating to the folder, and using `./script.sh`.
