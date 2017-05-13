# Prune local branches

*From [Schleis on StackOverflow](http://stackoverflow.com/a/17029936)*

After deleting branches from the origin, you'll want to prune the same
branches from your local machines.

```bash
git remote prune origin
```

Then to actually delete all the local branches that have since been
merged up to develop / master:

```
git branch -r | awk '{print $1}' | egrep -v -f /dev/fd/0 <(git branch -vv | grep origin) | awk '{print $1}' | xargs git branch -d
```
