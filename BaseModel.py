import sqlite3

# import DataBaseManager


class BaseModel:
    def __init__(self) -> None:
        pass

    def Select(self):
        pass

    def Insert(nameDataBase, tableName, valueInsert):
        a = str(nameDataBase) + ".db"
        con = sqlite3.connect(a)
        cur = con.cursor()
        firstParth = "INSERT INTO {} "
        x = str(list(valueInsert.keys()))
        x = x[1 : (len(x) - 1)]
        s = ""
        for i in x:
            if i != "'":
                s += i
        firstParth += "({}) VALUES "
        x = str(list(valueInsert.values()))
        x = x[1 : (len(x) - 1)]
        firstParth += "({})"
        firstParth = firstParth.format(tableName, s, x)
        cur.execute(firstParth)
        con.commit()
        con.close()

    def Delete(self):
        pass


qwa = BaseModel
qwa.Insert(
    "TEstDB",
    "Students",
    {"StudentId": 2, "FirstName": "Big", "LastName": "Smoke", "BirthDate": "2.3.1990"},
)
