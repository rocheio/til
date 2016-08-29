# Count Number of Words in a String

To count the number of words in a string (e.g. a section from an article online), pipe together the `echo` and `wc` commands.

```bash
$ echo -n '<here is a string>' | wc --words
4
```

For other useful counts, replace `--words` with `--chars`, `--lines` or `--bytes`.
