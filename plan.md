# 0k

- [ ] 

# in

- ~~look in `.co-authors`~~
- look in `.co-authors.history`
- ~~look in `~/.co-authors`~~
- ~~automatically add our files to `.gitignore`~~
- ~~search current local repo history `git log --all ...`~~
  - ~~look for authors _and_ co-authors~~
- ~~all these could be merged, `uniq` (DRY) and `take(50)` (don't explode the context)~~
- spinner while AI is generating text
- a router for human text - is it a strict enum? let's start with yes - a strict enum
- Q - how to `git --messgae-template`
  - could be a hook - an interactive hook?
    - this is stronger than a msg template, because you can't override it with `git commit -m "no template"`
    - could become interactive after some while, like a debounce
    - meaning - right after we approve, it'll stay quiet and do its job; but after a while it'll ask for approval again
  - could be a commit msg template - let's start with that
    - a message template can be passed on the cli
    - better to use `git config commit.template .co-authors`
      - first see if a template exists...

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

