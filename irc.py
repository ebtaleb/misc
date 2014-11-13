#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
import string

host = "irc.nanami.fr"
port = 6667
chan = "#test"
nick = "duck"

s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))

s.send("NICK %s\r\n" % nick)
s.send("USER %s %s bla: %s\r\n" % (nick, host, nick))
s.send("JOIN %s\r\n" % chan)

readbuffer = ""

s.send("PRIVMSG %s :%s\r\n" % (chan, "hello"))

try:
    while 1:
        readbuffer = s.recv(1024)
        print(readbuffer)
        temp = string.split(readbuffer, '\n')
        readbuffer = temp.pop()

        for line in temp:
            line = string.rstrip(line)
            line = string.split(line)

        if line[0] == "PING":
            s.send("PONG %s\r\n" % line[1])

        if line[2] == ":!eatbun":
            s.send("PRIVMSG %s kyaaa!" % chan)

except KeyboardInterrupt:
    print("got ya Ctrl+C m8")
finally:
    s.send("QUITTING\r\n")
    s.close()
