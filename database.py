import sqlite3 as lite
con = lite.connect('getting_started.db')

with con:    

    cur = con.cursor()    
    cur.execute("DROP TABLE IF EXISTS cities")
    cur.execute("DROP TABLE IF EXISTS weather")
    cur.execute("CREATE TABLE cities (name text, state text)")
    cur.execute("INSERT INTO cities (name, state) VALUES 'New York City', 'NY'), ('Boston', 'MA'), ('Chicago', 'IL'), ('Miami', 'FL'), ('Dallas', 'TX'), ('Seattle', 'WA'), ('Portland', 'OR'), ('San Francisco', 'CA'), ('Los Angeles', 'CA')")
    cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
    cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
    cities = (('Las Vegas', 'NV'),
                    ('Atlanta', 'GA'))
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)                