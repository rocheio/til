# Find the Version of a Specific Pip Module

To find the specific name and version of a module in pip,
pipe the contents of `pip freeze` into `grep`

```bash
$ pip3 freeze | grep -i soup
beautifulsoup4==4.4.1
```
