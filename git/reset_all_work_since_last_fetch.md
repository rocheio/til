# Reset all Work Since the Last Fetch

*from [Jefromi](http://stackoverflow.com/a/2846154)*

If you prototype out an idea you no longer want, or introduce some nasty bug you cannot solve, sometimes you should just start over. When this happens, you can reset your entire Git branch and history to a previous point in time using the `reset` command.

To reset your branch to the last version pushed to the origin, use `git reset --hard origin/dev` (or whatever branch you are using).

To reset __only__ the act of committing the previous commit, but leave the working files intact, use `git reset HEAD^`. `HEAD` refers to the current commit, and the `^` suffix means 'the commit before'.
