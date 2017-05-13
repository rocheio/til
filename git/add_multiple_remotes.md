# Add Multiple Remotes

To add another remote Git location to your current, just:

```bash
git remote add <name> git@github.com:rocheio/til.git
```

Default Git commands (`git pull`, `git push`) will still work against the current remote (probably `origin`), but you can just add the `<name>` of the new remote to any of them to interact with it instead.
