idea - a small cli, with natural language interface, to create a commit message template with co-authors

```shell
$ co-authors set to Nitsan, Diana, Gregor, Michael, Joel
👍 you got it

try triggering a commit like this:

    git commit --allow-empty

would you like me to try now? [Y/n] n

$ co-authors Ringo, Paul, John, George
I can't find them locally, would you like me to look on github? [Y/n/detail] I think they're on the python approvals repo
Found them!

$ co-authors who are the co-authors now?
The co-authors are Nitsan and Gregor

$ co-authors rm Nitsan
👍 Nitsan removed, we're left with only Gregor as co-author
```
- idea - keep a co-authors db under ~/.co-authors
- idea - use git commit message template for the thing...

