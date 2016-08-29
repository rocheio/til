# View All Changes to a File

*from [Dan Moulding](http://stackoverflow.com/a/5493663) and [the Git docs](https://git-scm.com/docs/git-reset)*

To view the entire history of a file, including renames and merges, use the command `git log --follow -p -- <file>`.

This is very useful if a recent merge (probably by another developer) accidentally loses your changes to the void, and the basic `git log` commands cannot find your original commit.

Once you identify the commit with the version of the file you want, you can use `git reset --soft <commit>` to see all the changes that have been applied since that commit. If you need to edit or undo some of those changes, do so now. Once all changes are made and the edits are complete, you can recommit the (now corrected) changes using `git commit -a -c ORIG_HEAD`.
