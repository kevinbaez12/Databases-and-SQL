import sqlite3

# open a connection to a new blank database
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()


# execute an appropriate CREATE_TABLE statement to accept the data
DROP_TABLE = '''DROP TABLE IF EXISTS demo;'''
conn.execute(DROP_TABLE)
conn.commit()

CREATE_TABLE = '''
CREATE TABLE IF NOT EXISTS demo (
    s TEXT,
    x INT,
    y INT
);
'''
curs.execute(CREATE_TABLE)
conn.commit()


# execute an appropriate INSERT_INTO statement to add data to the database

INSERT_INTO_TABLE = '''
    INSERT INTO demo(s,x,y)
    VALUES("g", 3, 9),
    ("v", 5, 7),
    ("f", 8, 7)'''
# commit to save data in database
curs.execute(INSERT_INTO_TABLE)
conn.commit()
# Query data to make sure data has been saved to database


# 1. How many rows are in the table?
row_count = curs.execute('''SELECT COUNT(*) FROM demo;''')
row_count = curs.fetchall()
print(row_count)
# 2. How many rows are there where both x & y are at least 5?
xy_at_least_5 = curs.execute('''
SELECT COUNT(*) FROM demo
WHERE demo.x >=5 AND demo.y >= 5;
''')
xy_at_least_5 = curs.fetchall()
print(xy_at_least_5)
# 3. How many unique values of y are there?
unique_y = curs.execute('''
SELECT COUNT(DISTINCT(demo.y))
FROM demo;
''')
unique_y = curs.fetchall()
print(unique_y)
