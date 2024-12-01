import sqlite3

# Initialize database
def init_db():
    conn = sqlite3.connect("fitfusion.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        health_goals TEXT,
        dietary_preferences TEXT,
        fitness_level TEXT,
        medical_conditions TEXT
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        date TEXT,
        weight REAL,
        calories_consumed INTEGER,
        steps INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)
    
    conn.commit()
    conn.close()

# Add a user
def add_user(name, email, health_goals, dietary_preferences, fitness_level, medical_conditions):
    conn = sqlite3.connect("fitfusion.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO users (name, email, health_goals, dietary_preferences, fitness_level, medical_conditions)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, email, health_goals, dietary_preferences, fitness_level, medical_conditions))
    conn.commit()
    conn.close()

# Query user progress
def get_user_progress(user_id):
    conn = sqlite3.connect("fitfusion.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM progress WHERE user_id = ?", (user_id,))
    data = cursor.fetchall()
    conn.close()
    return data
