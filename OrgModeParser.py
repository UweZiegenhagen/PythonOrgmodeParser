# -*- coding: utf-8 -*-
"""
@author: Uwe Ziegenhagen, ziegenhagen@gmail.com
"""

import re
 
def parseEmacsOrgmode(s):
    r = '^([\*]+)?\s?(TODO|PROGRESSING|FEEDBACK|VERIFY|POSTPONED|DELEGATED|CANCELLED|DONE)?\s?(\[#[A|B|C]\])?\s?(.*?)\s*(:(.*):)?$'    
    m = re.search(r,s)
    level = m.group(1)
    if (level is not None):
        level = len(level)
    prio = m.group(3)
    if (prio is not None):
        prio = prio[2:3]
    tags = []
    a = m.group(5)
    if a != None:
        b = len(a)-1
        a= a[1:b]
        a = a.split(':')
    tags.append(a)
    return(level, m.group(2), prio, m.group(4), tags)
 
with open("./testfiles/minimal.org", "r") as ins:
    for line in ins:
        level, status, priority, task, tags = parseEmacsOrgmode(line)
        if level is not None:        
            print('Level:', level)
            print('Status:', status)
            print('Priority:', priority)
            print('Task:', task)
            print('Tags:',tags,'\n\n')