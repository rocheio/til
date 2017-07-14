# Grep with Color

When using grep, most systems have color highlighting enabled by default. But since Git Bash on Windows does not, force it using the `--color` flag.

```bash
$ pip freeze | grep -i py --color
```
