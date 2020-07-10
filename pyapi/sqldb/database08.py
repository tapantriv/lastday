#!/usr/bin/env python3:

import sqlite3
# Print all
conn = sqlite3.connect('test.db')
print("Opened database successfully")
cursor = conn.execute("SELECT id, name, cost, condition from GAME")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("COST = ", row[2])
    print("CONDITION = ", row[3], "\n")

print("Operation done successfully")
conn.close()

# Print condition is new
conn = sqlite3.connect('test.db')
print("Opened database successfully - WORKS!")
cursor = conn.execute("SELECT id, name, cost, condition from GAME WHERE instr(condition, 'NEW') > 0")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("COST = ", row[2])
    print("CONDITION = ", row[3], "\n")

print("Operation done successfully")
conn.close()


# Print cost greater than $5
conn = sqlite3.connect('test.db')
print("Opened database successfully - WORK IN PROGRESS")
cursor = conn.execute("SELECT id, name, cost, condition from GAME WHERE cost>5")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("COST = ", row[2])
    print("CONDITION = ", row[3], "\n")

print("Operation done successfully- END")

# Print cost less than $5
conn = sqlite3.connect('test.db')
print("Printing cost is less than 5  Begin")
cursor = conn.execute("SELECT * from GAME where cost < 5")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("COST = ", row[2])
    print("CONDITION = ", row[3], "\n")

print("End of cost less than 5")

conn.close()

#Update  price where name is MI2
conn = sqlite3.connect('test.db')
print("------------------Updating-------------------")
print("Updating price.... for MI2")
conn.execute("UPDATE GAME set COST= 7 WHERE ID = 2")
conn.commit()
print("Total number of rows updated:", conn.total_changes)
cursor= conn.execute("SELECT * from GAME")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("COST = ", row[2])
    print("CONDITION = ", row[3], "\n")

print("Updade Operation is done")

conn.close()
#Inserting Data for Delete
print("------------Inserting in to Db----------------")
conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO GAME (ID,NAME,COST,CONDITION) VALUES (8, 'MI0', 32, 'NEW' )")

conn.commit()
print("Records Inserted successfully")
conn.close()

#Delete Above Entry from DB
conn = sqlite3.connect('test.db')
print("------------------Delete-------------------")
print("DELETE.... for MI2")
conn.execute("DELETE from GAME WHERE ID = 7")
conn.commit()

cursor= conn.execute("SELECT * from GAME")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("COST = ", row[2])
    print("CONDITION = ", row[3], "\n")

print("DELETED Operation is done")

conn.close()
