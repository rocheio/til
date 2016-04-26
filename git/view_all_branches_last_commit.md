View all Branches by Last Commit Date
=====================================

**from [shweta](http://stackoverflow.com/a/30574636)**

In a large Git repo with many contributors, there will likely come a time when you want to purge unused branches from the origin[1].

To begin the search for unused branches, run the following command in the Git repo (use Git Bash if running on Windows):

```bash
for branch in `git branch -r | grep -v HEAD`;do echo -e `git show --format="%ci %cr" $branch | head -n 1` \\t$branch; done | sort -r
```

[1]: This is especially true when using Git with Visual Studio / Team Foundation Server. With TFS, every pull request creates a new unique branch in the origin, which does not always get deleted (as it should...) after the pull request is accepted.
