#!usr/bin/env python3
#open file in read mode
dnsfile= open("dnsservers.txt","r")
#create list of lines
dnslist = dnsfile.readlines()
#looping over lines
for svr in dnslist:
    #print and end wihtout a newline
    print(svr, end = "")
    #close your file
    dnsfile.close()



