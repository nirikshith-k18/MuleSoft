import sqlite3

#creating database
conn = sqlite3.connect('movies.db')

c = conn.cursor()

#creating table
c.execute(""" CREATE TABLE movies (
            mname text,
            actor text,
            year integer,
            director text
          ) """)

#inserting data into table
c.execute("INSERT INTO movies VALUES('Iron Man 1', 'Robert Downey Jr.', 2008, 'Jon Favreau')")
c.execute("INSERT INTO movies VALUES('Iron Man 2', 'Robert Downey Jr.', 2010, 'Jon Favreau')")
c.execute("INSERT INTO movies VALUES('Iron Man 3', 'Robert Downey Jr.', 2013, 'Shane Black')")
c.execute("INSERT INTO movies VALUES('Black Panther', 'Chadwick Boseman', 2018, 'Ryan Coogler')")
c.execute("INSERT INTO movies VALUES('Ant Man', 'Paul Rudd', 2015, 'Peyton Reed')")

#selecting all data from table
c.execute("SELECT * FROM movies")

#selecting required data from table
c.execute("SELECT * FROM movies WHERE actor = 'Robert Downey Jr.'")

print(c.fetchall())


conn.commit()
conn.close()