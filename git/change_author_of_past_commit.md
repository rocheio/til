Change Author of a Past Commit
==============================

As a Git project grows, there will likely be a time when an author commits code from a new computer, forgetting to first configure their name/email to be identical to the name/email used in previous commits.

To fix this, you can use the `git rebase -i` interactive, but I found it easier to edit the commit history directly following [this guide on StackOverflow](http://stackoverflow.com/a/28845565).

First, identify and checkout the commit that needs modification. Then re-commit those changes with the `--amend --author` flags.

```git
git log
git checkout 03f482d6
git commit --amend --author "New Author <author@email.com>"
```

Then, replace the original commit with the newly amended commit, and change back over to the master branch.

```git
git replace 03f482d6 42627abe
git checkout master
```

Finally, rewrite historical commits to reflect the newly amended commit, sanity check the changes you made, and push the amended history.

```git
git filter-branch -- --all
git log
git push -f
```