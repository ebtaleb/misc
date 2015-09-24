# Miscellaneous Cheatsheet

## Git

```sh
# 
$ git format-patch -N
$ git am < patch 

# all changes from the current branch against master in a patch
$ git format-patch master --stdout > fix_empty_poster.patch

# remove N last commits 4ever
$ git reset --hard HEAD~N

# uncommit (keep changes)
$ git reset HEAD^

#
$ git log --grep <re>

# avoid merge commits resulting from git pull
$ git pull --rebase

# run this before pushing set of commits
$ git rebase -i @{u}
```

- on feature: to make feature compatible
- on master: to ship a feature:  ``` git merge --no-ff feature```

```sh
(git rev-list --reverse master~3..master | while read rev; do git checkout $rev; python runtests.py; done)
```

## Vim

```sh
$ vim +/search-term file
$ vim +N file
```

## Shell

### Subshells

Pass output of command as a parameter
- $() capture stdout of subshell
- <()/>() process redirection/substitution : feeds output of process into stdin of another

## SSH

```sh
$ ssh-keygen -b 4096 -t rsa
$ ssh-agent sh -c 'ssh-add </dev/null'
```

```sh
# forwards port 12345 to local ssh port
$ ssh -R 12345:localhost:22 -N server.com
$ ssh -R 12345:localhost:22 server.com "server 1000; exit"
# then.....
$ ssh localhost -p 12345
```

```sh
# connect to remote through 10000
$ ssh -L 10000:localhost:8090 remote
```

## RSync

```sh

```

## Linux

```sh
# save trace of each child in sep file
$ strace -ff -ttt -o file_rep cmd

# profile shell scripts
$ strace -c -f ...
```

### IPtables

```sh
$ iptables INPUT -s # REMOTE
$ iptables INPUT -d # LOCAL (me) INCOMING
$ iptables OUTPUT -s # LOCAL (me) OUTCOMING
$ iptables OUTPUT -d # REMOTE
```

- Convert tab to spaces : expand

Named pipes : mkfifo

- make char device accessible with mknod

```sh
$ su - $USERNAME
$ su - $USERNAME -c 'ls'
```

logger - enter messages into the system log
```sh

```

## Qemu
```sh
$ qemu-system vdisk.img -m 448 -enable-kvm

# add or delete snapshot
$ qemu-img snapshot -c $(snapname)
$ qemu-img snapshot -d $(snapname)

# applies snapshot
$ qemu-img snapshot -a $(imgfile)
# list snapshots
$ qemu-img snapshot -l $(imgfile)
```

