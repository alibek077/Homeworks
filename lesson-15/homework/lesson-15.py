# 1:

import sqlite3

conn = sqlite3.connect("starfleet.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")
conn.commit()




#2

cursor.execute("INSERT INTO Roster VALUES ('Benjamin Sisko', 'Human', 40)")
cursor.execute("INSERT INTO Roster VALUES ('Jadzia Dax', 'Trill', 300)")
cursor.execute("INSERT INTO Roster VALUES ('Kira Nerys', 'Bajoran', 29)")
conn.commit()



# 3

cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")
conn.commit()



# 4:
cursor.execute("""
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran'
""")
results = cursor.fetchall()

for name, age in results:
    print(f"{name} is {age} years old")

