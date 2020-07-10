#!/usr/bin/env python3

# open org-domain.txt and erase all current contents
with open("org-domain.txt", "w") as srvfile:
    srvfile.truncate(0)

# open com-domain.txt and erase all current contents
with open("com-domain.txt", "w") as srvfile:
    srvfile.truncate(0)



with open("dnsservers.txt", "r") as dnsfile:
    for svr in dnsfile:
        svr= svr.rstrip('\n')
        # if the string svr end with org
        if svr.endswith("org"):
            with open("org-domain.txt", "a") as srvfile:
                srvfile.write(svr+"\n")
                # else if the string start with com
        elif svr.endswith("com"):
            with open("com-domain.txt","a") as srvfile:
                srvfile.write(svr+"\n")

print("Script sucessfuly ran")
                
