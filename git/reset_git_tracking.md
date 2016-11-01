# Reset Git Tracking on Entire Repo

*from [takeshin](http://stackoverflow.com/a/1139797)*

You might be creating a new `.gitignore` for a legacy repo, and need to update tracking of many files.

```git
git rm -r --cached .
git add .
git commit -m 'update git tracking'
```
