# View a Concise History of Commits by Author

I wanted a quick way to share my recent work history with my managers, so I created a Git command that would layout my recent work in a nice format. Replace the author name with your own, then paste the following command in the Git repo you want to get a summary for.  

```git
git log -10 --pretty=format:'%cd - Committed %h:%n    %s%n' --author="<Name>"
```
