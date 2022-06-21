import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

sl_conn = sqlite3.connect('northwind_small.sqlite3')
sl_curs = sl_conn.cursor()

# Query the northwind database

# 1. what are the 10 most expensive items in the database?
expensive_items = curs.execute('''
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
''')
expensive_items = curs.fetchall()
print(expensive_items)


# 2. What is the average age of an employee at the time of their hiring?
avg_hire_age = curs.execute('''
SELECT AVG(HireDate - BirthDate)
FROM Employee;''')
avg_hire_age = curs.fetchall()
print(avg_hire_age)

# 3. What are the 10 most expensive items in the database & their suppliers?

ten_most_expensive = curs.execute('''
SELECT prod.ProductName, prod.UnitPrice, sup.CompanyName
FROM Product AS prod
JOIN Supplier AS sup
ON sup.ID = prod.SupplierID
ORDER BY prod.UnitPrice DESC
LIMIT 10;
''')
ten_most_expensive = curs.fetchall()
print(ten_most_expensive)


# 4. what is the largest category (by number of unique products in it)?

largest_category = curs.execute('''
SELECT cat.CategoryName, COUNT(prod.CategoryID)
FROM Product AS prod
INNER JOIN Category AS cat
ON prod.CategoryID = cat.ID
GROUP BY prod.CategoryID
ORDER BY COUNT(prod.CategoryID) DESC
LIMIT 1;
''')
largest_category = curs.fetchall()
print(largest_category)
