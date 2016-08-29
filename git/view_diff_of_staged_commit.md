# View the Differences of a Staged Commit

To view the differences between the last commit and the current working copy, simply use `git diff`.

However, if you just staged the commit using `git add .`, then `git diff` will return nothing. Instead, you need to use `git diff --staged`, which will return the diff as expected, including newly added files.
