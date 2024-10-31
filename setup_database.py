import sqlite3

def create_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        review_title TEXT,
        review_text TEXT,
        style_name TEXT,
        color TEXT,
        verified_purchase TEXT,
        rating INTEGER
    )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
