import sqlite3 as lite
import pandas as pd
con = lite.connect('getting_started.db')

with con:    

    cur = con.cursor() 
    #Drop the cities and weather tables if they exist since we're re-creating them   
    cur.execute("DROP TABLE IF EXISTS cities")
    cur.execute("DROP TABLE IF EXISTS weather")
    
    #Create the cities and weather tables
    cur.execute("CREATE TABLE cities (name text, state text)")
    cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)")
    
    #Add data to the cities table in a couple of different ways
    cur.execute("INSERT INTO cities (name, state) VALUES ('New York City', 'NY'), ('Boston', 'MA'), ('Chicago', 'IL'), ('Miami', 'FL'), ('Dallas', 'TX'), ('Seattle', 'WA'), ('Portland', 'OR'), ('San Francisco', 'CA'), ('Los Angeles', 'CA')")
    cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
    cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
    cities = (('Las Vegas', 'NV'),
                    ('Atlanta', 'GA'))
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    
    #Add data to the weather table in a couple of different ways
    cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January', 68)")
    cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January', 77)")
    cur.execute("INSERT INTO weather (city, year, warm_month, cold_month, average_high) VALUES ('New York City', 2013, 'July', 'January', 62),('Boston', 2013, 'July', 'January', 59), ('Chicago', 2013, 'July', 'January', 59), ('Miami', 2013, 'August', 'January', 84), ('Dallas', 2013, 'July', 'January', 77), ('Seattle', 2013, 'July', 'January', 61), ('Portland', 2013, 'July', 'December', 63), ('San Francisco', 2013, 'September', 'December', 64), ('Los Angeles', 2013, 'September', 'December', 75)") 
    weather = (('Las Vegas', 2013, 'July', 'December', 80),('Atlanta', 2013, 'July', 'January', 71))
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
    
    #Join two tables and store in a data frame
    #what was the point of this other than practicing with pandas?  Or is there a way to do the query directly with the data frame?
    df = pd.read_sql("SELECT name, state, year, warm_month, cold_month, average_high FROM cities INNER JOIN weather ON name = city", con)
    
    #Query to get city, state that are warmest in July
    cur.execute("SELECT name, state FROM cities INNER JOIN weather ON name = city WHERE warm_month = 'July'")
    #Gets all the rows from that query so we can do something with them
    rows = cur.fetchall()
    
    #a string to start the sentence
    result = "The cities that are warmest in July are: "
    
    #for each of the rows in the result set, add the city and state to the sentence
    for row in rows:
        result = result + " " + row[0] + ", " + row[1] + ","
    
    #get rid of the trailing comma and add a period to make it a proper sentence
    result = result[:-1]
    result += '.'
    #print the sentence
    print result    
	

	    
