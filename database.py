import sqlite3

def create_connection():
    return sqlite3.connect('trip_planner.db')

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL)
            """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trip (
            id INTEGER PRIMARY KEY,
            destination TEXT,
            start_date TEXT,
            end_date TEXT)
            """)
    connection.commit()
    connection.close()  
    
def insert_activity(name):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO activities (name)
        VALUES(?)  
        """,(name,)
        )
    connection.commit()
    activity_id = cursor.lastrowid
    connection.close() 
    return activity_id

def get_activities():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id, name
        FROM activities
    """)
    activities = cursor.fetchall()
    connection.close()
    
    return activities     
    
def delete_activity(activity_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        DELETE FROM activities
        WHERE id = ?
    """, (activity_id,))
    connection.commit()
    connection.close()
        
def save_trip(destination, start_date, end_date):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO trip (id,destination, start_date, end_date)
        VALUES (1, ?, ?, ?)
    """, (destination, start_date, end_date))
    connection.commit()
    connection.close()
    
def get_trip():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT destination, start_date, end_date
        FROM trip
        WHERE id =1
    """)
    
    trip = cursor.fetchone()
    connection.close()
    return trip    