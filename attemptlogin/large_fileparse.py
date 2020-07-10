#!/usr/bin/python3
loginfail=0
keystone_file =open("/home/student/mycode/attemtlogin/keystone.common.wsgin","r")
for line in keystone_file:
    if "-----] Authorization failed" in line:
        loginfail +=1
        print("Thenumber of failed log in attempts is", loginfail)
        keystone_file.close()

        
