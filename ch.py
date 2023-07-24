#!/usr/bin/python
# -*- coding: UTF-8 -*-
import myscr2 as sc
#import ipdb; ipdb.set_trace()
while True:
		c=sc.getch();
		if (c==10): sc.say('enter'); break
		sc.say(c)