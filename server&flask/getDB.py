import sqlite3
import os

class DBSearch:
    def __init__(self):
        self.database = os.path.dirname(os.path.realpath(__file__)) + "/crime.db"


    def start(self):
        self.conn = sqlite3.connect(self.database)
        self.cur = self.conn.cursor()
    
    def findAll(self, column):
        self.cur.execute("SELECT {id} FROM crime".\
            format(id=column))
        wierdList = self.cur.fetchall()
        goodList = []
        for i in wierdList:
            if i[0] is not None:
                goodList.append(i[0])
        return goodList
    
    def findSome(self, column, where, equals):
        self.cur.execute("SELECT %s FROM crime where %s=?" % (column, where), (equals,))
        wierdList = self.cur.fetchall()
        goodList = []
        for i in wierdList:
            if i[0] is not None:
                goodList.append(i[0])
        return goodList


    #first arguments are return values, followed by the string "FROM" then followed by 
    #where and equal values. can select unlimited return values, where, and equal values
    #EXAMPLE findSomeVar("id","xCord", "FROM", "weapon","HANDGUN", "gender", "M")
    #EXAMPLE RETURN: all ids and xCords where weapon is a handgun and gender is a male

    def findSomeVar(*args):
        total = len(args)
        returns = []
        isReturn = True
        wheres = []
        isWhere = False
        equals = []
        for i in total:
            if i is "FROM":
                isReturn = False
                isWhere = True
            if isReturn:
                returns.append(i)
            

    
    def findXY(self, column, up, down, left, right):
        x = "xCord"
        y = "yCord"
        self.cur.execute("SELECT %s FROM crime where %s>? AND %s<? AND %s>? AND %s<?" % (column, y, y, x, x), (down, up, left, right, ))
        wierdList = self.cur.fetchall()
        goodList = []
        for i in wierdList:
            if i[0] is not None:
                goodList.append(i[0])
        return goodList

    def findSomeXY(self, column, where, equals, up, down, left, right):
        x = "xCord"
        y = "yCord"
        self.cur.execute("SELECT %s FROM crime where %s>? AND %s<? AND %s>? AND %s<? AND %s = ?" % (column, y, y , x, x, where), (down, up, left, right, equals, ))
        wierdList = self.cur.fetchall()
        goodList = []
        for i in wierdList:
            if i[0] is not None:
                goodList.append(i[0])
        return goodList


    def end(self):
        self.cur.close()
        self.conn.close()




