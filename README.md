![alt_text](https://imgs.xkcd.com/comics/automation.png)

# pycommit
The tool you never expected and yet will save you entire seconds, maybe minutes of your developer lifetime.
Autoformat my commit messages. 

# usage
to work you just need a git repository
Add this to your bashrc
```
export PATH="$PATH:$HOME/path/to/pycommit/"
```
In a git repository, type:
```
pycommit.py "adding doc to the vision module" 
```
Which will all git commit with the following message:
```
"[branch_name][CLEAN] adding doc to the vision module"


