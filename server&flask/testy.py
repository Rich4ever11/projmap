import sqlite3
from getDB import DBSearch
import os
import datetime



tester = DBSearch()


tester.start()

a = datetime.datetime.now()

find = tester.findXY("id",'39.3505' ,'39.24', '-76.6886', '-76.5334')

b = datetime.datetime.now()

print(b-a)
a = datetime.datetime.now()
find2 = tester.findSomeXY("id",'gender', 'M',  '39.3505' ,'39.24', '-76.6886', '-76.5334')
b = datetime.datetime.now()
print(b-a)

print(len(find))

print(len(find2))

print("done")
tester.end()


#findSome is significantly faster than findAll
#increase findSome functionality

