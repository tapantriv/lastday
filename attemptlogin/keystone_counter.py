#!/usr/bin/python3
loginfail = 0
keystone_file = open("/home/student/mycode/attemtlogin/keystone.common.wsgi","r")
keystone_file_lines = keystone_file.readlines()
for line in keystone_file_lines:
    if"-----] Authorizatio failed" in line:
        liginfail +=1
    print("The number of failed log in attempts is", loginfail)
    keystone_file.close()
