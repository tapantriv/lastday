#!/usr/bin/env python3

import sqlite3
#create DB
conn = sqlite3.connect('test.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE IF NOT EXISTS GAME
 (ID INT PRIMARY KEY     NOT NULL,
 NAME           TEXT    NOT NULL,
 COST            INT     NOT NULL,
 CONDITION      CHAR(50));''')
print("Table created successfully")
conn.close()

#create Db Test1
conn = sqlite3.connect('test.db')
print("Opened database test1.db successfully")
#Insert Data in to db
conn.execute("INSERT INTO GAME (ID,NAME,COST,CONDITION) VALUES (1, 'MI1', 5, 'NEW' )")

conn.execute("INSERT INTO GAME (ID,NAME,COST,CONDITION) VALUES (2, 'MI2', 3, 'OLD' )")

conn.execute("INSERT INTO GAME (ID,NAME,COST,CONDITION) VALUES (3, 'MI3',10, 'NEW' )")

conn.execute("INSERT INTO GAME (ID,NAME,COST,CONDITION) VALUES (4, 'MI4', 15, 'NEW' )")

conn.execute("INSERT INTO GAME (ID,NAME,COST,CONDITION) VALUES (5, 'MI5', 1, 'BAD' )")
conn.commit()
print("Records created successfully")
conn.close()




