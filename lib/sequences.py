#!/usr/bin/env python3

def print_fibonacci(length):
    filist=[]
    while len(filist)<length and length!=0:
        if len(filist)==0:
            filist.append(0)
        elif len(filist)==1:
            filist.append(1)
        else:
            i=filist[len(filist)-1]
            j=filist[len(filist)-2]
            filist.append(i+j)
    print(filist)