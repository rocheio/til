Remove all files of a certain type
===================================

**from [benzittlau](https://gist.github.com/benzittlau/956122)**

If you need to remove all files matching a given type from your git repo, chain commands with `grep`:

```git
git ls-files | grep '\.pyc$' | xargs git rm
```

This was useful when I accidentally added a bunch of *.pyc files to my repo using `git add -A .` before having a `.gitignore` in place.
