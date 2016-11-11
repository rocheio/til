# Create Random Alphanumeric String

*from [earthgecko](https://gist.github.com/earthgecko/3089509)*

Open the terminal, and use the `tr` command to pull from `/dev/urandom`:

```
cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1
```
