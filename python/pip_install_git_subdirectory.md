# Pip Install from a Branch or Subdirectory of a Git Repo

*from [Dennis Golomazov on StackOverflow](https://stackoverflow.com/a/19516714)*

When setting up continuous integration, or even basic deployment scripts, you might need to remotely install a Python package from a Git branch and/or subdirectory.

```bash
pip install -e 'git+https://git.repo/some_repo.git@<branch>#egg=<subdir>&subdirectory=<subdir>'
```
