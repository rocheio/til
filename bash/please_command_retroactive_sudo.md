Add a Please Command to Retroactively Sudo
==========================================

**After further reading, I found that `sudo !!` works even better, and is native**

*from [jpschorr](http://unix.stackexchange.com/a/158480)*

If you find yourself forgetting to use the `sudo` command often, you can add a `please` command that will retroactively `sudo` the last command that you attempted to run.

Using the `fc -ln -1` command will return the last command you ran in the terminal as text. Using the `$()` wrapper will run anything inside it in a subshell and return that value. Add this command to the `~./bash_aliases` file and restart the terminal to use your new `please` command.

```bash
sudo nano ~/.bash_aliases
# alias please='sudo $(fc -ln -1)'
```
