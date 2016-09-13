# Print a Specific Line from a File

*from [anubhava on StackOverflow](http://stackoverflow.com/a/6022431)*

To print the content of a specific line from a file (e.g. from a large CSV file) in Bash, use the `sed` tool.

```bash
$ sed '147267q;d' large_csv_file.csv
Some,Values,Printed,Here
```
